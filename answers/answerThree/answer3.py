b, f = map(int, input().split())
j = 0
for i in range(b):
    a = int(input())
    j += a
if j >= f:
    print('YES')
else:
    print('NO')