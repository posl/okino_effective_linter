"""Fixer for else after for"""

from .. import fixer_base
from ..msg_container import build_message


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
        msg = build_message(self, node)

        return None, msg
