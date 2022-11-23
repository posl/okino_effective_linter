import argparse
import json
import subprocess
import sys

from .mylib2to3.main import main as mylib

parser = argparse.ArgumentParser(
    prog='eflint',
    usage='how to use',
    description='linter for effective python.',
)


def main():
    # args = parser.parse_args()
    params = [{"messages": []}]
    code = sys.stdin.read()

    # mylib
    lib2to3_msgs = mylib(
        fixer_pkg='eflint.mylib2to3.fixes',
        code=code,
        args=['--no-diffs', '-']
        )

    for msg in lib2to3_msgs:
        linter_msg = {
            'lineStart': msg.line_start,
            'columnStart': msg.column_start,
            'lineEnd': msg.line_logical_end,
            'columnEnd': msg.column_logical_end,
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
                    'column': msg.column_logical_end,
                    'line': msg.line_logical_end
                }
            }

        params[0]["messages"].append(linter_msg)

    # pylint
    with subprocess.Popen(["echo", code], stdout=subprocess.PIPE) as pipe:
        pylint_output = subprocess.run(
            ["pylint", "--from-stdin", "stdin", "-f", "json"],
            stdin=pipe.stdout,
            capture_output=True,
            text=True,
            check=False,
        ).stdout
    pylint_msgs = json.loads(pylint_output)

    for msg in pylint_msgs:
        linter_msg = {
            'lineStart': msg['line']-1,
            'columnStart': msg['column'],
            'lineEnd': msg['endLine'] or msg['line']-1,
            'columnEnd': msg['endColumn'] or msg['column']+1,
            'code': msg['message-id'],
            'message': msg['message'] + '<eflint>',
            'severity': 2,
            'source': 'eflint',
            'correctable': 0,
            'docsUrl': 'https://code.visualstudio.com/api'
        }

        params[0]["messages"].append(linter_msg)

    result = json.dumps(params, ensure_ascii=False)
    print(result)
