"""Fixer match test."""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixUnpack(fixer_base.BaseFix):

    # bmでない = リピート*+[]を含む？要検証 多分計算量が多い

    # 今の実装のままだと全体にマッチしてしまうため，ファイル全体に下線を引いてしまう，要修正
    # '\n'などを含む場合はr文字列にする必要あり
    PATTERN = r"""
        any<
            any*
            simple_stmt< expr_stmt< any '=' power< id1=any trailer< '[' any ']' > > > '\n' >
            simple_stmt< expr_stmt< any '=' power< id2=any trailer< '[' any ']' > > > '\n' >
            next = any*
        >
    """

    CODE = 'ef006'
    MESSAGE = '複数代入アンパックを使え'
    SEVERITY = 2
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):
        msg = MessageContainer(
            node.get_lineno()-1,
            node.get_columnno(),
            node.get_end_lineno()-1,
            node.get_end_columnno(),
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
