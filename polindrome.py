def palindromeIndex(s):
    def check(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            if check(l + 1, r):
                return l
            if check(l, r - 1):
                return r
            return -1
        l += 1
        r -= 1

    return -1
print(palindromeIndex("ababab"))