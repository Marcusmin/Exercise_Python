
def fn1(a):
    z = 1
    def fn2(fn):
        def wrapper(args, keys):
            args += z
            keys += z
            return fn(args, keys)
        return wrapper
    return fn2

@fn1('a')
def test(a, b):
    return a, b
print(test(1,2))


def longestCommonPrefix(strs):
    len_str = len(strs[0])
    len_list = len(strs)
    same = ''
    for i in range(len_list-1):
        for j in range(len_str-1):
            if strs[i][j] == strs[i+1][j+1]:
                same += strs[i][j] 






