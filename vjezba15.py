#To do Aplikacija

lista_zadataka = []

print("Dobrodosli u To do aplikaciju. Za izlaz odaberite x")

while True:

    zadatak = input("Unesi novi zadatak")

    if zadatak.lower() != "x" :
        lista_zadataka.append(zadatak)    
    else:
        break

    print("lista_zadataka")
    for x in lista_zadataka:
        print(x) 