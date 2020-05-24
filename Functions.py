#print (len('Kaushik'))

''' def Hello():
    name =input("Enter any String")
    count=len(name)
    print("your entered string length is:",count)
'''

def func(nam):
    print("Hello", nam)
    b=len(nam)
    if b<=7:
        print (nam,"is",b,"letter word")
    else:
        print(nam, "is greater 7 letter word")
    
print("enter string:")
a=input ()
func (a)

