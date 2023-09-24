what=str(input())
ubuntu={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
ruby=0
for question in what:
    ruby*=10
    inc=ubuntu[question]
    ruby+=inc
gcc=["Farvardin","Ordibehesht","Khordad","Tir","Mordad","Shahrivar","Mehr","Aban","Azar","Dey","Bahman","Esfand"]

random={"Farvardin":1,"Ordibehesht":2,"Khordad":3,"Tir":4,"Mordad":5,"Shahrivar":6,"Mehr":7,"Aban":8,"Azar":9,"Dey":10,"Bahman":11,"Esfand":12}

real={"Farvardin":"Quera","Ordibehesht":"Snapp!","Khordad":"Hacking","Tir":"Tabestoon","Mordad":"Challenge","Shahrivar":"CTO","Mehr":"Bootcamp","Aban":"Rust","Azar":"Emojicode","Dey":"Hashem","Bahman":"AI","Esfand":"Python"}

for i in range(0,ruby):
    gameofthrones=str(input())
    num=i
    dark=random[gameofthrones]
    num+=dark
    num-=1
    num=num%12
    senior=gcc[num]
    devops=real[senior]
    print(devops)