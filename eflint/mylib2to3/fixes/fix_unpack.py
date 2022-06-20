"""Fixer match test."""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixUnpack(fixer_base.BaseFix):

    # bmでない = リピート*+[]を含む？要検証 多分計算量が多い

    # '\n'などを含む場合はr文字列にする必要あり
    # 最小マッチングなので足りない
    # 要改善
    PATTERN = r"""
        any<
            any*
            stmt1=simple_stmt< expr_stmt< any '=' power< id1=any trailer< '[' any ']' > > > '\n' >
            (simple_stmt< expr_stmt< any '=' power< any trailer< '[' any ']' > > > '\n' >)*
            stmt2=simple_stmt< expr_stmt< any '=' power< id2=any trailer< '[' any ']' > > > '\n' >
            (not simple_stmt< expr_stmt '\n' >)
            any*
        >
    """

    CODE = 'ef006'
    MESSAGE = '複数代入アンパックを使え'
    SEVERITY = 2
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = MessageContainer(
            results['stmt1'].get_lineno()-1,
            results['stmt1'].get_columnno(),
            results['stmt2'].get_end_lineno(is_logical=True)-1,
            results['stmt2'].get_end_columnno(is_logical=True),
            results['stmt2'].get_end_lineno()-1,
            results['stmt2'].get_end_columnno(),
            self.CODE,
            self.MESSAGE,
            self.SEVERITY,
            self.CORRECTABLE,
            None
        )

        return None, msg

    def match(self, node):
        r = super(FixUnpack, self).match(node)
        if r:
            if r["id1"] == r["id2"]:
                return r
            return None
        return r
