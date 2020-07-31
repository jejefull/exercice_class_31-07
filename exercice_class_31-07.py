#exercice 1

numb = int(input("input numb : "))
print(numb)
while True:
    numb=int(numb/2)
    print(numb)
    if numb==0:
        break



#exercice 2

count=0
total=0
avr=0
while True:
    numb = int(input("input numb : "))
    count=count+1
    total=total+numb
    avr=int(total/count)
    print(total)
    print(avr)
    if numb==1:
        print("good by")
        break

#exercice 3
str_list=[]
x=''
while True:
    x= input("Input word: ")
    str=x.upper()
    str_list.append(str)
    if str_list.count(str) == 3:
        print("same word")
        break
    else:
        continue

#exercice 4

list_numb1=[3,5,30,0,1]
list_numb2=[1000,4,29,-5,4]
res_list1=0
res_list2=0
count=-1

for x in list_numb1:
    count=count+1
    if count>len(list_numb2):
        break
    if x>list_numb2[count]:
        res_list1=res_list1+1
    elif list_numb2[count]>x:
        res_list2=res_list2+1
if res_list1>res_list2:
    print("the first list is win")
else:
    print("the second list is win")

'''
