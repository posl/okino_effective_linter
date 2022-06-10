"""Fixer match test."""

from .. import fixer_base


class FixUnpack(fixer_base.BaseFix):

    # bmでない = リピート*+[]を含む？要検証 多分計算量が多い

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
        return None

    def match(self, node):
        r = super(FixUnpack, self).match(node)
        if r:
            if r["id1"] == r["id2"]:
                return r
            return None
        return r
