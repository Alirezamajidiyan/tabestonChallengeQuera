tabestoon=str(input())
hack={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
quera=0

for challeng in tabestoon:
    quera*=10
    emoji=hack[challeng]
    quera+=int(emoji)


if quera>3 and 7>quera:
    print("Yes :)")
else:
    print("No :(")