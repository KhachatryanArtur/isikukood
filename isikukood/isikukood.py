
arvud=[]
isikukoodid=[]

while True:
    ik=input("Anna isikukood: ") #str
    if ik=="1": break
    if len(ik)!=11:
        print("Liiga palju v�i liiga v�he s�mboleid. Sisesta veel kord:")
        arvud.append(ik)
    else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene s�mbol ei ole �ige!")
            arvud.append(ik)
        else:
            print("Esimene s�mbol on �ige")
            y=ik_list[1]+ik_list[2] #aasta
            m=ik_list[3]+ik_list[4] #kuu
            d=ik_list[5]+ik_list[6] #p�ev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("S�nnip�ev ei saa luua")
                arvud.append(ik)
            else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy="19"
                else:
                    yy="20"
                spaev=d+"."+m+"."+yy+y #ei ole 18..,19..,20..
                print(f"S�nnip�ev on {spaev}")
                print(f"Viimane number: {ik_list[-1]}")
                kontrollnr=0
                
                hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
                if 1<=hhh<=10:
                    haigla="kuresaare Haigla"
                elif 11<=hhh<=19:
                    haigla="Tartu �likooli Naistekliinik, Tartumaa, Tartu"
                elif 21<=hhh<=220:
                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna s�nnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                else:
                    haigla=" ---"

                if int(ik_list[0])%2==0:
                    sugu="naine"
                else:
                    sugu="mees"
                print(f"See in {sugu}, s�nnip�ev{spaev}. Ta on s�ndinud {haigla}")
                isikukoodid.append(ik)
print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)