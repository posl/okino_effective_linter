"""Fixer for walrus"""


from .. import fixer_base
from ..msg_container import build_message


class FixToWalrusInComp(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        atom< '['
            listmaker< func0=any comp_for< 'for' fp=any 'in' it=any comp_if< 'if' func1=any > > >
        ']' >
    """

    CODE = 'ef029'
    MESSAGE = '内包表記内でwalrus演算子を使え'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, node)

        return None, msg

    def match(self, node):
        r = super(FixToWalrusInComp, self).match(node)
        if r:
            if r["func0"] == r["func1"]:
                return r
            return None
        return r
