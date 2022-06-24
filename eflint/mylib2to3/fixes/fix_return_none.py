"""Fixer for return None."""

from .. import fixer_base
from ..msg_container import build_message


class FixReturnNone(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        try_stmt<
            'try' ':' suite
            except_clause ':' suite< any any simple_stmt< return=return_stmt any > any >
        >
    """

    CODE = 'ef020'
    MESSAGE = 'Noneを返すな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, results['return'])

        return None, msg

    def match(self, node):
        r = super(FixReturnNone, self).match(node)
        if r:
            _return = [leaf.value for leaf in r["return"].leaves()]
            if 'None' in _return:
                return r
            return None
        return r
