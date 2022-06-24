"""Fixer for walrus"""


from .. import fixer_base
from ..fixer_util import Walrus, Parens
from ..msg_container import build_message


class FixToWalrus(fixer_base.BaseFix):

    PATTERN = r"""
        any<
            any*
            stmt1=simple_stmt< expr_stmt< id1=any '=' id2=any > '\n' >
            stmt2=if_stmt< 'if' ids=any ':' suite >
            next=any*
        >
    """

    CODE = 'ef010'
    MESSAGE = 'walrus演算子を使え'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):

        # ifブロック内で使われていて，ifより外で使用されていない，という条件があってもいいかも
        # 置き換えるのはコピーしてから，要修正

        for leaf in results["ids"].leaves():
            if leaf.value == results["id1"].value:
                # 子ノードが存在するならカッコをつける
                if results["ids"].children:
                    walrus = Walrus(results["id1"], results["id2"])
                    leaf.replace(Parens(walrus, prefix=leaf.prefix))
                else:
                    leaf.replace(Walrus(results["id1"], results["id2"], prefix=leaf.prefix))

                break

        results["stmt1"].remove()
        msg = build_message(self, results["stmt1"], results["stmt2"], replacement=str(results["stmt2"]))

        return None, msg

    def match(self, node):
        r = super(FixToWalrus, self).match(node)
        if r:
            values = [v.value for v in r["ids"].leaves()]
            if r["id1"].value in values:
                return r
            return None
        return r
