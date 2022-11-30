"""冗長な条件式を簡略化する変換

* Change

    if x > 1:
        return True
    else:
        return False

into

    return x > 1
"""


from .. import fixer_base
from ..fixer_util import Return
from ..msg_container import build_message


class FixSimplifiableIfStmt(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    if_stmt<
        'if' condition=any ':'
            suite< '\n' any simple_stmt< return_stmt< 'return' 'True' > '\n' > any >
        'else' ':'
            suite< '\n' any simple_stmt< return_stmt< 'return' 'False' > '\n' > any >
    >
    """

    CODE = 'R1703'
    MESSAGE = '冗長な条件式を簡単にする'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        condition = results["condition"].clone()
        new = Return(condition)
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
