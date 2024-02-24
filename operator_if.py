#1
nimi=input("Mis on sinu nimi?") #upper()-"JUKU",lower()-"juku",capitalize()-"Juku"
if nimi.upper()=="JUKU":
	print("Lahme kinno")
	vanus=int(input("Kui vana sa oled? "))
	if vanus<0 or vanus>100:
		vastus="Viga vanusega"
	elif vanus<6:
		vastus="tasuta pilet"
	elif vanus<14:
		vastus="lastepilet"
	elif vanus<65:
		vastus="taispilet"
	elif vanus<100:
		vastus="sooduspilet"
	print("On vaja Jukule osta",vastus)
else:
	print("Joonistame")


#2
n1=input("Esimene nimi: ")
n2=input("Teine nimi: ")
if (n1.upper()=="ANNA" and n2.upper()=="BEN") or (n1.upper()=="BEN" and n2.upper()=="ANNA"):
    print(n1,"ja", n2, "tana te istusite kokku")


#3
a=float(input("Ruumi pikkus: "))
b=float(input("Ruumi laius: "))
S=a*b
v=input("Kas soovote teha remoont? ")
if v.upper()=="JAH":
    h=float(input("Kui palju maksab ruut meeter? "))
    r=S*h
    print("Remoonti hind on", round(r,2))
    

#4
h=float(input("Milline on hind? "))
if (h>700):
    s=h-(h*0.3)
    print(round(s,2),"euro")


#5
t=float(input("Missugune on temperatuur? "))
if (t>18):
    print("Temperatuur on rohrem, kui 18 C")


#6
t=float(input("Mis on sinu pikkus? "))
if t<150:
    print("Sa oled lühike")
elif t<160:
    print("Sa oled keskmist kasvu")
else:
    print("Sa oled pikk")


#7
t=float(input("Mis on sinu pikkus? "))
p=input("Kas sa oled naine voi mees? ")
if p=="mees":
    if t<160:
        print("Sa oled lühike")
    elif t<170:
        print("Sa oled keskmist kasvu")
    else:
        print("Sa oled pikk")
elif p=="naine":
    if t<150:
        print("Sa oled lühike")
    elif t<160:
        print("Sa oled keskmist kasvu")
    else:
        print("Sa oled pikk")


#8
from datetime import *
from random import *
arve_nr=date.today() #datetime.now()
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

tooded=["Piim","Leib","Suhkur","Voi"] #len(tooded)=4
hinnad=[randint(50,150)/100,randint(50,150)/100,randint(100,150)/100,randint(100,550)/100]
for i in range(len(tooded)): #tooded[0]="Piim, tooded[1]="Leib", tooded[2]="Suhkur", tooded[3]="Voi"
    toode=tooded[i]
    hind=hinnad[i]
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta? ").lower()
    if v=="jah":
        mitu=int(input("Mitu? "))
        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
        summa+=mitu*hind
    print()
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)


#9
a=float(input("Первая сторона квадрата: "))
b=float(input("Вторая сторона квадрата: "))
if a==b:
    print("Это квадрат!")
    S=a*b
    print("Площадь:",S)


#10
arv1=float(input("Первое число: "))
arv2=float(input("Второе число: "))
d=input("Выберите действие (+,-,*,/): ")
error=False
if d=="+":
    r=arv1+arv2
elif d=="-":
    r=arv1-arv2
elif d=="*":
    r=arv1*arv2
elif d=="/":
    r=arv1/arv2
else:
    error=True
    
if error:
    print("Неправильное действие",d)
else:
    print(arv1,d,arv2,"=",r)


#11
from datetime import *
a=int(input("Год рождения: "))
t=date.today()
j=t.year-a
print ("Возраст:",j)
m=j/10
k=round(m)
d=k*10
if d==j:
    print("с юбилеем")


#12
h=float(input("Цена: "))
if h<=10:
    r=h-h*0.1
    print("Скидка в 10%, цена :",round(r,2))
elif h>10:
    r=h-h*0.2
    print("Скидка в 20%, цена :",round(r,2))


#13
p=input("Пол(м/ж):")
t=p.upper()
if t=="М":
    a=int(input("Взраст: "))
    if 16<=a and a<=18:
        print("Подходит")
    else:
        print("Не подходит")
else:
    print("Не подходит")


#14
from random import *
K=randint(5,150)
M=randint(10,30)
s=0
p=0
print("всего",K, "человек")
print("в один автобус помещается",M, "человек")
while(K>0):
    K-=1
    s+=1
    if(s==M):
        p+=1
        s=0
print(p, "полных автобусов")
print("в последнем автобусе будет",s, "человек")
