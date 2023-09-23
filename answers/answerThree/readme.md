### 🍉🍉 تابستون چلنج 🍉🍉

این سری از سوالات با زبان پایتون و سوال آخر با زبان سی پلاس پلاس حل شده است


**بی متن**

```Python
string=str(input())
print('b'+string)
```
<br>

**متن کوتاه**

```Python
print('YES')
```
<br>

**پشتیبانی**

```Python
b, f = map(int, input().split())
j = 0
for i in range(b):
    f = int(input())
    j += f
if j >= f:
    print('YES')
else:
    print('NO')
```
<br>

**متن سالم است**

```Python
b = int(input())
f = list(map(int, input().split()))

res = 0
for i in range(b):
    for j in range(i):
        if f[i] < f[j]:
            res += 1

print(res)
```
<br>

**جاج سالم است**

```c++
#include <iostream>

using namespace std;

int main() 
{
    int f, b;
    cin >> f >> b;
    cout << f * b << endl;
    return 0;
}
```
<br>