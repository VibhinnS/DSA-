def is_palindrome(s):
    return s == s[::-1]

def precompute_palindromes(s, n):
    palin = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            if is_palindrome(s[j:j + i]):
                palin[i] = True
                break
    return palin

def f_value(s, l, r, palin):
    n = len(s)
    result = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            if not palin[j - i + 1]:
                result += j - i + 1
                break
    return result

s = "aaab"
n = len(s)
palin = precompute_palindromes(s, n)
queries = [(1, 4), (1, 3), (3, 4),(2,4)]
for l, r in queries:
    print("Query:", l, r)
    print("f_value:", f_value(s, l - 1, r - 1, palin))
