#for letter in 'Python':     # First Example
#   print( 'Current Letter :', letter)


print("Who are u?")
#a=input()
#print("Hello!",a)

# Bollean
b= 3
c=5
print(1, b==3)
print(2, c==5)
print(3, b==3 and c==5)
print(4, b==5 and c==3)
print(5, not b==5 and c==5)
print(6, b==5 or c==5)
print(7, b==5 and c==3)
print(8, not (b==5 and c==5))
print(9, not b==5 and c==3)

print("Enter Time in Hrs")
Time=float(input())
print ("Enter distance in Km")
Distance=float(input())
print("you speed was:", (Distance/Time),"Km/Hr")
