text ="My name is Kaushik"
print(text.split(" "))

Agr="100-92882-2019-1"
print(Agr)
spli=Agr.split("-")
print("Splited Agr no.:",spli)
ls=list(spli)
print("converting Agr into list:",ls)
#print(ls[4])

alpha=''.join(ls)
print(alpha)

lis=["Kaushik","Shirish","Rohini","Digambar","Govind","Malvadkar"]
txt=",".join(lis)
print(txt.capitalize())
print(txt.title())
