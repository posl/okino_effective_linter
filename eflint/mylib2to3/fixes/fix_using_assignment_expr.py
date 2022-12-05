"""Walrus演算子を用いて簡潔にする

* Change

    x = 1
    if x:
        print(x)

into

    if x := 1:
        print(x)
"""


from .. import fixer_base
from ..fixer_util import Walrus, Parens
from ..msg_container import build_message


class FixUsingAssignmentExpr(fixer_base.BaseFix):

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
        target = results["id1"].clone()
        assign = results["id2"].clone()

        for leaf in results["ids"].leaves():
            if leaf.value == results["id1"].value:
                walrus = Walrus(target, assign, prefix=leaf.prefix)

                # 子ノードが存在するならカッコをつける
                if results["ids"].children:
                    walrus.prefix = ''
                    leaf.replace(Parens(walrus, prefix=' '))
                else:
                    leaf.replace(walrus)
                break

        results["stmt1"].remove()
        # suiteの最後の空行のコメントを無視する
        # ちょっと強引なので直したい
        results["stmt2"].children[-1].children[-1].prefix = ''
        msg = build_message(self, results["stmt1"], results["stmt2"], replacement=str(results["stmt2"]))

        return None, msg

    def match(self, node):
        r = super().match(node)
        if r:
            values = [v.value for v in r["ids"].leaves()]
            if r["id1"].value in values:
                return r
            return None
        return r
