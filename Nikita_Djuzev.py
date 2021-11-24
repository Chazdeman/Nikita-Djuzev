from module1 import *
users=["Nikita"]
passwords=["12345"]

while True:
	print("Näita kõike-0 Reg-1,Avt-2,Välja-3")
	v=int(input())
	if v==0:
		koik_kasutajad(users,passwords)
	if v==1:
		print("Registreerimine")
		users,passwords=register(users,passwords)
	elif v==2:
		print("Avtoriseerimine")
		autoris(users,passwords)
	elif v==3:
		print("Välja")
		break
	else:
		print("On vaja valida 0 / 1 / 2 / 3")# kõik on olemas

