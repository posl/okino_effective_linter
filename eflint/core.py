import argparse
import json

from .mylib2to3.main import main as mylib

parser = argparse.ArgumentParser(
    prog='eflint',
    usage='how to use',
    description='linter for effective python.',
)
parser.add_argument('--mock', action='store_true', help='return test json.')


def main():
    args = parser.parse_args()

    if args.mock:
        params = [
            {
                "messages": [
                    {
                        'lineStart': 0,
                        'columnStart': 0,
                        'lineEnd': 0,
                        'columnEnd': 5,
                        'code': 'ep000',
                        'message': 'ごみコードです',
                        'severity': 2,
                        'source': 'eflint',
                        'correctable': 1,
                        'docsUrl': 'https://code.visualstudio.com/api',
                        'inlineFix': {
                            'replacement': 'replaced',
                            'start': {
                                'column': 0,
                                'line': 0
                            },
                            'end': {
                                'column': 5,
                                'line': 0
                            }
                        }
                    }
                ]
            }
        ]

    else:
        messages = mylib('eflint.mylib2to3.fixes', ['--no-diffs', '-'])
        params = [{"messages": []}]
        for msg in messages:
            params[0]["messages"].append(
                {
                    'lineStart': msg['lineStart'],
                    'columnStart': msg['columnStart'],
                    'lineEnd': msg['lineEnd'],
                    'columnEnd': msg['columnEnd'],
                    'code': msg['code'],
                    'message': msg['message'],
                    'severity': msg['severity'],
                    'source': 'eflint',
                    'correctable': msg['correctable'],
                    'docsUrl': 'https://code.visualstudio.com/api',
                    'inlineFix': {
                        'replacement': msg['replacement'],
                        'start': {
                            'column': msg['columnStart'],
                            'line': msg['lineStart']
                        },
                        'end': {
                            'column': msg['columnEnd'],
                            'line': msg['lineEnd']
                        }
                    }
                }
            )

    j = json.dumps(params, ensure_ascii=False)
    print(j)
