import argparse
import json

from .mylib2to3.main import main as mylib

parser = argparse.ArgumentParser(
    prog='eflint',
    usage='how to use',
    description='linter for effective python.',
)


def main():
    # args = parser.parse_args()

    messages = mylib('eflint.mylib2to3.fixes', ['--no-diffs', '-'])
    params = [{"messages": []}]
    for msg in messages:
        linter_msg = {
            'lineStart': msg.line_start,
            'columnStart': msg.column_start,
            'lineEnd': msg.line_end,
            'columnEnd': msg.column_end,
            'code': msg.code,
            'message': msg.message,
            'severity': msg.severity,
            'source': 'eflint',
            'correctable': msg.correctable,
            'docsUrl': 'https://code.visualstudio.com/api'
        }

        if msg.correctable:
            linter_msg["inlineFix"] = {
                'replacement': msg.replacement,
                'start': {
                    'column': msg.column_start,
                    'line': msg.line_start
                },
                'end': {
                    'column': msg.column_end,
                    'line': msg.line_end
                }
            }

        params[0]["messages"].append(linter_msg)

    j = json.dumps(params, ensure_ascii=False)
    print(j)
