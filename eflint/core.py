import argparse
import json
import sys

parser = argparse.ArgumentParser(
    prog='eflint',
    usage='how to use',
    description='linter for effective python.',
)
parser.add_argument('--mock', action='store_true', help='return test json.')


def main():
    args = parser.parse_args()
    code = ''.join(sys.stdin.readlines())

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
                        'message': f'ごみコード（{code[0:5]}）です',
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

        j = json.dumps(params, ensure_ascii=False)
        print(j)
