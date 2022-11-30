"""空のリストの初期化を簡単な記法に変換する

* Change

    x = list()

into

    x = []
"""


from .. import fixer_base
from ..fixer_util import EmptyList
from ..msg_container import build_message


class FixListLiteral(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    power< 'list' trailer< '(' ')' > >
    """

    CODE = 'R1734'
    MESSAGE = '空のリストの初期化を簡単な記法にする'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        new = EmptyList()
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
