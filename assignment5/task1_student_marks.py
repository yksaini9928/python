dict1 ={"Alice":85,"saini":95,"yksaini":68,"sunil":75,"rahul":85}


name=input("Enter the student's name:")

if name in dict1:
    print(name,"'s marks:", dict1[name])
else:
    print("not found in the records ")    
