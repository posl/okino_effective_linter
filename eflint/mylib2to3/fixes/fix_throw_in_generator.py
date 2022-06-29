"""Fixer for throw in generator."""


from .. import fixer_base
from ..msg_container import build_message


class FixThrowInGenerator(fixer_base.BaseFix):

    BM_compatible = False

    # it.throw()と同時使用を条件に入れるべき
    PATTERN = """
        try_stmt<
            'try' ':'
                suite< any any simple_stmt< yield_expr< 'yield' any > any > any >
            except_clause ':'
                suite
            [ 'else' ':' suite ]
            [ 'finally' ':' suite ]
        >
    """

    CODE = 'ef035'
    MESSAGE = 'throwで状態遷移するな'
    SEVERITY = 1
    CORRECTABLE = 0
    DOCSURL = ''

    def transform(self, node, results):

        msg = build_message(self, node)

        return None, msg
