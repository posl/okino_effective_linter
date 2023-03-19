"""空の辞書の初期化を簡単な記法に変換する

* Change

    x = dict()

into

    x = {}
"""


from .. import fixer_base
from ..fixer_util import EmptyDict
from ..msg_container import build_message


class FixUseDictLiteral(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    power< 'dict' trailer< '(' ')' > >
    """

    CODE = 'R1735'
    MESSAGE = ''
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        new = EmptyDict()
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
