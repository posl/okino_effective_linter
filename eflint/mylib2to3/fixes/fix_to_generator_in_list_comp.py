"""Fixer to generator in list comprehension."""


from .. import fixer_base
from ..fixer_util import Parens
from ..msg_container import build_message


class FixToGeneratorInListComp(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        atom< '[' gen=listmaker< any comp_for< 'for' any 'in' power< 'open' trailer > > > ']' >
    """

    CODE = 'ef032'
    MESSAGE = 'ジェネレータにしたほうがいいかも'
    SEVERITY = 1
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        gen = results['gen'].clone()
        new = Parens(gen)

        msg = build_message(self, node, replacement=str(new))

        return None, msg
