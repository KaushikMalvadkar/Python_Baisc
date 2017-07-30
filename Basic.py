def print_msg(msg,error="no error", *kwargs): #** kwargs accepts multiple agruments
    print("Log:"+error+"\t"+msg)
    print(kwargs)

#print_msg("Welcome","File not found")
#print_msg("Welcome")

print_msg("Welcome","File not found","1","2")

def print_msg1(msg,error="no error",*args, **kwargs): #** kwargs accepts multiple agruments
    print("Log:"+error+"\t"+msg)
    print(kwargs)
print_msg1("Welcome","File not found","1","2",key_1="123",key_2="1234")