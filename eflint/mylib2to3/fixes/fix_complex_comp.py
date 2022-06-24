"""Fixer for complex comprehension."""


from .. import fixer_base
from ..msg_container import build_message
from ..fixer_util import is_comp_for,  is_comp_if


class FixComplexComp(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
        list=atom< '[' listmaker ']' >
    """

    CODE = 'ef028'
    MESSAGE = '内包表記内で3式以上使うな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, node)

        return None, msg

    def match(self, node):
        r = super(FixComplexComp, self).match(node)
        if r:
            count = 0
            for _node in r['list'].post_order():
                if is_comp_for(_node) or is_comp_if(_node):
                    count += 1
                if count >= 3:
                    return r
            return None
        return r
