b = int(input())
f = list(map(int, input().split()))

res = 0
for i in range(b):
    for j in range(i):
        if f[i] < f[j]:
            res += 1

print(res)