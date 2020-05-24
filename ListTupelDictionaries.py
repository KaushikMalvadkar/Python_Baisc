num=[1,2,3,4,5]
mamals=["Unicorn","Pheonix","Dragon","Vampire","Minotaur","Balrog"]
print("*-LIST-*")
print (num[1])
print (num[-4])
print (num[1:3])
print (mamals[1:3])
print(num+mamals)

# Append
num.append(278)
num.insert(6,62)
print(num)
mamals=mamals+["Grifin"]
print(mamals)

#Remove from index no.
del num[5]
mamals.remove("Grifin")
mamals.pop(4)
print(num)
print(mamals)

#covert sting into list
name=input("Enter any name: \n")
ls =list(name)
print(ls+num)
print("Length of list is:",len(ls+num))

#Tuples cannot add or remove items
week=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
print("*-TUPLES-*")
print(week)
ncp=[("Shweta",2002),("Apoorva",2004),("Dolly",2007),("Komal",2012),("Dimple", 2013),("Suhasna",2014),("Riya",2015)]
print(ncp)
print (ncp[0][1])
print ("Max",max(ncp))

#Dictionaries
phonebook={"Emma":1234, "Donald":42525, "Daniel":9833, "Max":7892}
print(phonebook)
print(phonebook["Max"])
phonebook["Max"]="020 240 022"
del phonebook["Max"]
print(phonebook)

name=input("Enter name: \n")
no= int (input("Enter mobile no.: \n"))
phonebook[name]=no
print(phonebook)
