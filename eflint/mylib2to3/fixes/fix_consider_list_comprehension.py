"""リスト内包表記を用いた処理に変換する

* Change

    x = []
    for e in y:
        x.append(e**2)

into

    x = [e**2 for e in y]
"""


from .. import fixer_base
from ..msg_container import build_message
from ..fixer_util import ListComp, Assign


class FixConsiderListComprehension(fixer_base.BaseFix):

    BM_compatible = False

    # TODO: if文にも対応する
    PATTERN = r"""
        any<
            any*
            stmt0=simple_stmt< expr_stmt< new_it0=any '=' atom< '[' ']' > > any >
            stmt1=for_stmt< 'for' fp=any 'in' it=any ':'
                suite< '\n' any
                    simple_stmt< power< new_it1=any trailer< '.' 'append' > trailer< '(' xp=any ')' > > '\n' > any
                >
            >
            any*
        >
    """

    CODE = 'X0003'
    MESSAGE = 'リスト内包表記を使うと，より簡潔にリストを作成することができます．'
    SEVERITY = 3
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        xp = results['xp'].clone()
        fp = results['fp'].clone()
        new_it = results['new_it0'].clone()
        it = results['it'].clone()

        list_comp = ListComp(xp, fp, it)
        new = Assign(new_it, list_comp)
        msg = build_message(self, results['stmt0'], end_node=results['stmt1'], replacement=new)

        return None, msg

    def match(self, node):
        r = super().match(node)
        if r:
            if r['new_it0'] == r['new_it1']:
                return r
            return None
        return r
