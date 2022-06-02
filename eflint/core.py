import argparse
import json


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
                        'correctable': 0
                    }
                ]
            }
        ]

        j = json.dumps(params, ensure_ascii=False)
        print(j)
