"""不要なelseを削除する変換

* Change

    if x > 1:
        break
    else:
        x = 2

into

    if x > 1:
        break x
    x = 2
"""


from .. import fixer_base
from ..fixer_util import If, dedent
from ..msg_container import build_message


class FixNoElseBreak(fixer_base.BaseFix):

    BM_compatible = True

    # TODO: elseの行が空白行として残る問題の修正
    PATTERN = r"""
    if_stmt<
        'if' condition=any ':'
            if_suite=suite< '\n' any simple_stmt< 'break' '\n' > any >
        'else' ':'
            else_suite=any
    >
    """

    CODE = 'R1723'
    MESSAGE = ''
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        condition = results["condition"].clone()
        if_node = results["if_suite"].clone()
        else_node = results["else_suite"].clone()
        new = If(condition, if_node)
        dedent(else_node)
        msg = build_message(self, node, replacement=str(new)+str(else_node))
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
