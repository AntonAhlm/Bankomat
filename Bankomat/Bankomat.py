
ruta=" "*50
print(ruta,"+","-"*16,"+")
print(ruta,"|  Te21C           |")
print(ruta,"|  Anton Ahlm      |")
print(ruta,"+","-"*16,"+\n\n") 

 

pengar=int(input("Hur mycket pengar? ")) 

apa=1

fh=int(pengar/500)

th=int((pengar-fh*500)/200)

eh=int((pengar-fh*500-th*200)/100) 



#print(fh,th,eh)

#Lapp eller Lappar
if fh==1:
    lapp5="femhundralapp"
else:
    lapp5="femhundralappar"
if th==1:
    lapp2="tvahundralapp"
else:
    lapp2="tvahundralappar"
if eh==1:
    lapp1="hundrasedel"
else:
    lapp1="etthundralappar"

#Utskrift

if fh==0:

    if th==0:
        if eh==0: 
            apa+1
        else: 
            print("Det blir",eh,lapp1) 

    else: 
        print("Det blir",th,lapp2)

        if eh==0: 
            apa+1
        else: 
            print("Det blir",eh,lapp1)

else: 
    print("Det blir",fh,lapp5)
    if th==0:
        if eh==0: 
            apa+1
        else: 
            print("Det blir",eh,lapp1)

    else: 
        print("Det blir",th,lapp2)
        if eh==0: 
            apa+1
             
        else: 
            print("Det blir",eh,lapp1)







