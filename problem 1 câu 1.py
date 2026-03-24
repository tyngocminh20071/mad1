def next(s):
    if not s:
        return "a"
    chars = list(s)
    n = len(chars)
    alphabet = 'abcd'
    i=n-1
    while i >= 0 and chars[i] == 'd':
        chars[i] == 'a'
        i -= 1
        
    if i>=0:
        idx=alphabet.index(chars[i])
        chars[i]=alphabet[idx+1]
        return "".join(chars)
    else:
        return "a" * (n+1)

print("Kết quả sau khi chạy test là:")
test = ["aaa", "bccc", "ddd", "d", "aaaa", "abcd"]
for s in test:
    print(f"next('{s}') = '{next(s)}'")