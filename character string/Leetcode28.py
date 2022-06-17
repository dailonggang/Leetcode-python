def strStr(haystack, needle):
    a = len(needle)
    b = len(haystack)
    if a == 0:
        return 0
    next = getnext(a, needle)
    p = 0
    for k in range(b):
        while p >= 1 and needle[p] != haystack[k]:  # p>=0?保证next数组不越界
            p = next[p-1]
        if needle[p] == haystack[k]:
            p += 1
        if p == a:
            return k - a + 1
    return -1


def getnext(a, needle):
    """
    初始化
    前后缀不相同
    前后缀相同
    next
    """
    # 初始化
    next = ['' for i in range(a)]  # ['', '', '', '', '', '']
    j = 0  # 生成next为原数组
    next[0] = 0  # 开始设为0
    for i in range(1, len(needle)):  # 从1开始遍历needle
        # 前后缀不相同，j回退
        while j > 0 and needle[j] != needle[i]:  # j > 0保证不会越界，也就是回退的极限，
            j = next[j-1]
        # 前后缀相同
        if needle[j] == needle[i]:
            j += 1  # 因为在for循环中，所以i++
        #  更新next数组的值
        next[i] = j
    return next


haystack ="aabaabaaf"
needle ="af"
l = strStr(haystack, needle)
print(l)

