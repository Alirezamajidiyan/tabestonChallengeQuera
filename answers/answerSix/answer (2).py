ali=str(input())
tabestoon={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
snapp=0
for name in ali:
    snapp*=10
    question=tabestoon[name]
    snapp+=question
for i in range(0,snapp):
    python=str(input())
    rust=0
    for cpp in python:
        rust*=10
        go=tabestoon[cpp]
        rust+=go
    if rust<=50:
        print("Mitoonam Komak Konam.")
    else:
        print("Motaesfam Barat!")
