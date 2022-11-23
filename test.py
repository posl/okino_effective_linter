"""デバッグ実行のためのファイル"""

from eflint.mylib2to3.main import main

main('eflint.mylib2to3.fixes', ['-f', 'to_fstr', 'sample.py'])
