s = [int(input()) for i in range((int(input()))+1)]
n = "НЕТ"
for j in range(len(s)-1):
    if n != "НЕТ":
        break
    for k in range(j+1, len(s)-1):
        if s[j] * s[k] == s[-1]:
            n = "ДА"
            break
print(n)