"""ループ内で辞書の要素をitems()から取得する変換

* Change

    for key in dict:
        print(dict[key])

into

    for key, val in dict.items():
        print(val)
"""


from .. import fixer_base
from ..fixer_util import Return
from ..msg_container import build_message


class FixUsingDictItems(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    for_stmt<
        'for' key=any 'in' dict=any ':' suite
    >
    """

    CODE = 'C0206'
    MESSAGE = '辞書の要素をitems()を用いて取得する'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        msg = build_message(self, node, replacement=node)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
