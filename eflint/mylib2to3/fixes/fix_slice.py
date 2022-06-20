"""Fixer for slice"""


from .. import fixer_base
from ..refactor import MessageContainer


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
