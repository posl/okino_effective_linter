import json


def main():
    d = {
        'uri': 'test.py',
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

    j = json.dumps(d, ensure_ascii=False)
    print(j)
