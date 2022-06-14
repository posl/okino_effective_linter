"""Fixer match test."""

from .. import fixer_base
from ..refactor import MessageContainer  # 移動したい


class FixMatchTest(fixer_base.BaseFix):

    # BMとそうでないやつの見分け方を確認しておく
    # BM_compatible = True

    # '\n'などを含む場合はr文字列にする必要あり
    PATTERN = r"""
        sorted=any<
            any*
            simple_stmt<
              expr_stmt< id1=any '='
                         power< list='list' trailer< '(' (not arglist<any+>) any ')' > >
              >
              '\n'
            >
            sort=
            simple_stmt<
              power< id2=any
                     trailer< '.' 'sort' > trailer< '(' ')' >
              >
              '\n'
            >
            next=any*
        >
        |
        sorted=any<
            any*
            simple_stmt< expr_stmt< id1=any '=' expr=any > '\n' >
            sort=
            simple_stmt<
              power< id2=any
                     trailer< '.' 'sort' > trailer< '(' ')' >
              >
              '\n'
            >
            next=any*
        >
    """

    CODE = 'test'
    MESSAGE = 'マッチしたよ'
    SEVERITY = 1
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
