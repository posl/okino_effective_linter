"""Fixer for range to enumerate."""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixEnumerate(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
              for_stmt< 'for' any 'in' power< 'range' trailer< '(' power< 'len' trailer< '(' any ')' > > ')' > > ':' suite >
              """

    CODE = 'ef007'
    MESSAGE = 'enumerateを使え'
    SEVERITY = 2
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
