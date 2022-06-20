"""Fixer for else after for"""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixElseAfterFor(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
              for_stmt< 'for' any 'in' any ':' suite 'else' ':' suite >
              |
              while_stmt< 'while' any ':' suite 'else' ':' suite >
              """

    CODE = 'ef009'
    MESSAGE = 'elseブロックを使うな'
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
