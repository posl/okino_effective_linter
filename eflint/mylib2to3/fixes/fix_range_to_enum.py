"""Fixer for range to enumerate."""

from .. import fixer_base


class FixRangeToEnum(fixer_base.BaseFix):

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
        return None
