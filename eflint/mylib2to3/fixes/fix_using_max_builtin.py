"""標準のmaxを使用する変換

* Change

    if x < a:
        x = a

into

    x = max(x, a)
"""


from .. import fixer_base
from ..fixer_util import Assign, Call, Name
from ..msg_container import build_message


class FixUsingMaxBuiltin(fixer_base.BaseFix):

    BM_compatible = True

    # TODO: なぜか関数内だとマッチしない．パターンはかわらないはずだが．．．
    PATTERN = r"""
    if_stmt<
        'if' comparison< id0=any '<' val0=any > ':'
            suite< '\n' any simple_stmt< expr_stmt< id1=any '=' val1=any > '\n' > any >
    >
    """

    CODE = 'R1703'
    MESSAGE = '標準のmax()を使用する'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        _id = results["id0"].clone()
        val = results["val0"].clone()
        new = Assign(_id, Call(Name('max'), args=[_id, val]))
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        if r and r["id0"] == r["id1"] and r["val0"] == r["val1"]:
            return r
        return None
