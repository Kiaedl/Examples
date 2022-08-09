s = [input() for _ in range(int(input()))]
a = 'anton'
for i in range(len(s)):
    flag = 0
    for j in range(len(s[i])):
        if s[i][j] in a[flag]:
            flag += 1    
        if flag == 5:
            print(i+1, end=' ')
            break