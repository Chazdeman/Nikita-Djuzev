def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    file=open(file,"r")
    stroka=file.read()#читает строку str
    stroka=file.readlines()#делает список list
    file.close()
    return stroka
stroka=loe_failist("TextFile.txt")
print(stroka)

def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_
spisok=loe_failist_listisse("TextFile.txt")
print(spisok)

def salvesta_failisse(file:str):
    file=open(file,"a")
    text=input("Sisesta tekst:")
    file.write(text+"\n")
    file.close()

for i in range(10):
    salvesta_failisse("Loetelu.txt")

def faili_sisu_umberkirjutamine(file:str):
    text=input("Sisesta uus tekst =>")
    with open(file, "w") as file:
        file.write(text+"\n")
faili_sisu_umberkirjutamine(input("Faili nimetus =>")+".txt")