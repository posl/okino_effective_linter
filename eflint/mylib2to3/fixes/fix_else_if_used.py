"""elseとifを合体する変換

* Change

    if x > 0:
        print(x)
    else:
        if x < 0:
            print(-x)

into

    if x > 0:
        print(x)
    elif x < 0:
        print(-x)
"""


from .. import fixer_base
from ..fixer_util import Elif, If, dedent
from ..msg_container import build_message


class FixElseIfUsed(fixer_base.BaseFix):

    BM_compatible = False

    PATTERN = r"""
    if_stmt<
        'if' if_cond=any ':' if_suite=suite
        'else' ':'
            suite< '\n' any
                if_stmt<
                    'if' elif_cond=any ':' elif_suite=suite
                > any
            >
    >
    """

    CODE = 'R5501'
    MESSAGE = 'elseとifを合体する'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        if_cond = results["if_cond"].clone()
        if_suite = results["if_suite"].clone()
        elif_cond = results["elif_cond"].clone()
        elif_suite = results["elif_suite"].clone()
        dedent(elif_suite)
        _elif = Elif(elif_cond, elif_suite)
        new = If(if_cond, if_suite, _elif)
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
