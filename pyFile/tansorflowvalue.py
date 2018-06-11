
a = input()
with open(a+".txt",mode = "r", encoding="utf-8") as open_file:
    count = 0;
    while(True):
        a=open_file.readline()
        if not a :break;
if count < 400:
    value = 10
else if count > 400 && count <1000:
    value = 50
else if count >= 1000 && count <2000:
    value = 100
else if count >= 2000 && count <3000:
    value = 200
else if count >= 3000 && count <5000:
    value = 300
with open("true_text.txt",mode ="a",encoding = "utf-8") as open_file:
    open_file.write(a,count,value)
    
