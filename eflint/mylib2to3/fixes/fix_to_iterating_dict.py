"""辞書のキーではなく，辞書そのものをイテレートするように変換する

* Change

    for key in dict.keys():
        print(key)

into

    for key in dict:
        print(key)
"""


from .. import fixer_base
from ..fixer_util import Test, Assign
from ..msg_container import build_message


class FixToIteratingDict(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    for_stmt< 'for' any 'in' keys=power< dict=any trailer< '.' 'keys' > trailer< '(' ')' > > ':'
        any+
    >
    """

    CODE = 'C0201'
    MESSAGE = '辞書はそのままイテレートできる'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        old_node = node.clone()
        _dict = results["dict"].clone()
        results["keys"].replace(_dict)
        node.prefix = ''

        msg = build_message(self, old_node, replacement=node)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
