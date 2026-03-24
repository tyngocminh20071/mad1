def previous(s):
    if not s:
        return None
    if s == "a" * len(s):
        if len(s) == 1:
            return None
        return "d" * (len(s) - 1)
    
    chars = list(s)
    n = len(chars)
    alphabet = "abcd"
    
    i = n - 1
    while i >= 0 and chars[i] == 'a':
        chars[i] = 'd'
        i -= 1
    
    if i >= 0:
        idx = alphabet.index(chars[i])
        chars[i] = alphabet[idx - 1]
        return "".join(chars)
    return None
def previous_palindrome(s):
    if not s:
        return None
    
    n = len(s)
    chars = list(s)
    alphabet = "abcd"
    
    def is_palindrome(t):
        return t == t[::-1]

    current = previous(s)
    while current is not None:
        if is_palindrome(current):
            return current
        current = previous(current)
    
    return None

print("Kết quả sau khi chạy test là:")
test = ["aab", "aba", "bbb", "caaa", "aaaa", "abc", "ddd"]
for s in test:
    prev = previous_palindrome(s)
    print(f"previous_palindrome('{s}') = '{prev}'")