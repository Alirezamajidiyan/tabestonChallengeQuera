n, k = map(int, input().split())
s = 0
for i in range(n):
    a = int(input())
    s += a
if s >= k:
    print('YES')
else:
    print('NO')