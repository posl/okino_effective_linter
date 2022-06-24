"""Fixer for slice"""


from .. import fixer_base
from ..msg_container import build_message


class FixSlice(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        power< any trailer< '[' subscript< any ':' any sliceop< ':' any > > ']' > >
    """

    CODE = 'ef012'
    MESSAGE = 'スライスとストライドを同時に使うな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, node)

        return None, msg
