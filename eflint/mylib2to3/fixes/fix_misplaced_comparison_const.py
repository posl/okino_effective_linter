"""比較式の左側にある定数と右側の変数を入れ替える変換

* Change

    if 1 > x:
        return x

into

    if x < 1:
        return x
"""


from .. import fixer_base
from .. import pytree
from ..pgen2 import token
from ..fixer_util import is_number, is_string, Comparison
from ..msg_container import build_message


class FixMisplacedComparisonConst(fixer_base.BaseFix):

    BM_compatible = False

    PATTERN = r"""
    comparison< const=any comp=any val=any >
    """

    CODE = "C2201"
    MESSAGE = "比較の左に定数を置くな"
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ""

    def transform(self, node, results):
        const = results["const"].clone()
        val = results["val"].clone()
        comp = results["comp"].clone()
        new = Comparison(val, self.invert_op(comp), const)
        new.prefix = ""
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        if (
            r
            and (is_number(r["const"]) or is_string(r["const"]))
            and not (is_number(r["val"]) or is_string(r["val"]))
        ):
            return r
        return None

    def invert_op(self, op):
        if op.value == "<":
            return pytree.Leaf(token.GREATER, ">", prefix=" ")
        if op.value == ">":
            return pytree.Leaf(token.LESS, "<", prefix=" ")
        if op.value == "<=":
            return pytree.Leaf(token.GREATEREQUAL, ">=", prefix=" ")
        if op.value == ">":
            return pytree.Leaf(token.LESSEQUAL, "<=", prefix=" ")
        return op
