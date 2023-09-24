shangool=str(input())
ai={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
}
mangool=0
for habeangoor in shangool:
    mangool*=10
    chatgpt=ai[habeangoor]
    mangool+=chatgpt;
algoritm=0
for i in range(mangool):
    git=str(input())

    linux=0

    for commit in git:
        linux*=10
        conflict=ai[commit]
        linux+=conflict;
    algoritm^=linux;
ml=str(input())
if (algoritm==0)==(ml=="Naghi"):
    print("Yes :)")
else:
    print("No :(")