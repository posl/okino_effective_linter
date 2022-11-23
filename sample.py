"""エラーを出すためのファイル"""

x = 1.4142
y = 'a'
li = [1, 2, 3]
di = {'key': 'val'}

# ef004: to_fstr
print('%f %s %s' % (x, str(x), ' y'))

# ef006: unpack
a = li[0]
b = li[1]
c = li[2]

# ef007: enumerate
# ef008: zip
for i in range(len([1, 2])):
    pass

# ef009: else_after_for
for i in range(3):
    pass
else:
    # breakされなければ実行される
    pass

# ef010: to_walrus
count = pow(2, 2)
if count > 3:
    pass

# 全体にマッチしてしまう変換（複数文にわたる変換）は
# 同じ部分に同じ変換をしないようにする処理の都合で
# ↑を変換するまでエラーとして認識できない
count = pow(2, 2)
if count:
    print(count)

# ef011: slice
t = li[2:2]
t = li[::2]
t = li[2:2:2]

# ef016: key_error
if y in di:
    count = di[y]
else:
    count = 0

# ef016
try:
    count = di['key']
except KeyError:
    count = 0


# ef019: returns
def func():
    return 1, 2, 3, 4


a, b, c, d = func()
a, b, *other = func()


# ef020: return_none
def devide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# ef025: to_keyword_only_arg
def func2(x, y=False):
    return 0


def func3(x, *, y=False):
    return 0


# ef027: to_list_comp
a = []
for elem in li:
    a.append(elem**2)


# ef028: complex_comp
[y for x in a for y in x if y % 2 == 0]

# ef029: to_walrus_in_comp
a = [func(x) for x in y if func(x)]

# ef0032: to_generator_in_list_comp
b = [x for x in open('test.txt')]


# ef034: it_send
def func4():
    y = 1
    for x in range(5):
        y = yield x * y


# ef035: throw_in_generator
def func5():
    try:
        yield 1
    except Exception:
        print('a')
    else:
        print(1)
