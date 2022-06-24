"""Fixer for range to enumerate."""

from .. import fixer_base
from ..msg_container import build_message


class FixZip(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
              for_stmt<
                'for' any 'in' power< 'range' trailer< '(' power< 'len' trailer< '(' any ')' > > ')' > > ':' suite 
              >
              """

    CODE = 'ef008'
    MESSAGE = 'zipを使え'
    SEVERITY = 2
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, node)

        return None, msg
