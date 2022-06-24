"""Fixer match test."""

from .. import fixer_base
from ..msg_container import build_message


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
        msg = build_message(self, node)

        return None, msg

    def match(self, node):
        r = super(FixReturns, self).match(node)
        if r:
            returns = [leaf.value for leaf in r["returns"].leaves() if leaf.value != ',' and leaf.value != '*']
            if len(returns) >= 4:
                return r
            return None
        return r
