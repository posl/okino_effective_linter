"""空のリストとの比較を暗黙的な比較に変換する

* Change

    if x == []:
        print(x)

into

    if x:
        print(x)
"""


from .. import fixer_base
from ..msg_container import build_message


class FixImplicitBooleanessNotComparison(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    comparison< id=any '==' atom< '[' ']' > >
    """

    CODE = 'C1803'
    MESSAGE = ''
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        new = results["id"].clone()
        new.prefix = ''
        msg = build_message(self, node, replacement=new)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
