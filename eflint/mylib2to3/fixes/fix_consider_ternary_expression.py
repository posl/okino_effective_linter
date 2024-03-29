"""三項演算子を用いた処理に変換する

* Change

    if bool:
        x = a
    else:
        x = b

into

    x = a if bool else b
"""


from .. import fixer_base
from ..fixer_util import Test, Assign
from ..msg_container import build_message


class FixConsiderTernaryExpression(fixer_base.BaseFix):

    BM_compatible = True

    # TODO: anyで誤魔化している改行や空白をなんとかする
    PATTERN = r"""
    if_stmt<
        'if' bool=any ':'
            suite< any any simple_stmt< expr_stmt< id0=any '=' val0=any > any > any >
        'else' ':'
            suite< any any simple_stmt< expr_stmt< id1=any '=' val1=any > any > any >
    >
    """

    CODE = 'W0160'
    MESSAGE = ''
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        true_val = results["val0"].clone()
        false_val = results["val1"].clone()
        condition = results["bool"].clone()
        target = results["id0"].clone()

        test = Test(true_val, condition, false_val)
        new = Assign(target, test)

        msg = build_message(self, node, replacement=new)
        return new, msg

    def match(self, node):
        r = super().match(node)
        if r and r["id0"] == r["id1"]:
            return r
        return None
