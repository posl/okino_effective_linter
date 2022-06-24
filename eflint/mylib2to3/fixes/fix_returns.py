"""Fixer match test."""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixReturns(fixer_base.BaseFix):

    PATTERN = """
        return_stmt< 'return' returns=testlist_star_expr >
        |
        expr_stmt< returns=testlist_star_expr '=' any >
    """

    CODE = 'ef019'
    MESSAGE = '4変数以上をアンパックするな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = MessageContainer(
            node.get_lineno()-1,
            node.get_columnno(),
            node.get_end_lineno(is_logical=True)-1,
            node.get_end_columnno(is_logical=True),
            node.get_end_lineno()-1,
            node.get_end_columnno(),
            self.CODE,
            self.MESSAGE,
            self.SEVERITY,
            self.CORRECTABLE,
            None
        )

        return None, msg

    def match(self, node):
        r = super(FixReturns, self).match(node)
        if r:
            returns = [leaf.value for leaf in r["returns"].leaves() if leaf.value != ',' and leaf.value != '*']
            if len(returns) >= 4:
                return r
            return None
        return r
