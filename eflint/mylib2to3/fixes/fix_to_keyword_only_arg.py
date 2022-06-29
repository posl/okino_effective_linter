"""Fixer to keyword only argument."""


from .. import fixer_base
from ..msg_container import build_message


class FixToKeywordOnlyArg(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        funcdef< 'def' any
            parameters< '(' args=typedargslist ')' > ':'
            suite
        >
    """

    CODE = 'ef025'
    MESSAGE = 'キーワード専用引数を使え'
    SEVERITY = 1
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):

        msg = build_message(self, node)

        return None, msg

    def match(self, node):
        r = super(FixToKeywordOnlyArg, self).match(node)
        if r:
            args = str(r['args'])
            if '=' in args and '*' not in args:
                return r
            return None
        return r
