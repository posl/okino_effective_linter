"""Fixer for it.send()."""


from .. import fixer_base
from ..msg_container import build_message


class FixItSend(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        expr_stmt< any '=' yield_expr< 'yield' any > >
    """

    CODE = 'ef034'
    MESSAGE = 'ジェネレータにデータを注入するな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):

        msg = build_message(self, node)

        return None, msg
