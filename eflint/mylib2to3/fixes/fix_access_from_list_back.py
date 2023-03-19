"""配列の後ろからの参照を簡略化する

* Change

    x = _list[len(_list)-1]

into

    x = _list[-1]
"""


from .. import fixer_base
from ..fixer_util import Return
from ..msg_container import build_message


class FixAccessFromListBack(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    power< id0=any trailer< '[' arith_expr< len=power< 'len' trailer< '(' id1=any ')' > > '-' any > ']' > >
    """

    CODE = 'X0001'
    MESSAGE = '配列の後ろからの参照はより簡潔に記述することができます．'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        old_node = node.clone()
        results["len"].remove()
        node.prefix = ''
        msg = build_message(self, old_node, replacement=node)
        return node, msg

    def match(self, node):
        r = super().match(node)
        if r and r["id0"] == r["id1"]:
            return r
        return None
