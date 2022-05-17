def countCamelCase(S):
   
    # Stores the total count of
    # camelcase characters
    c = 1
 
    # Traverse the string S
    for i in range(1,len(str)-1):
       if(str[i].isupper()):
           c+=1
    return c
str=input()
print(countCamelCase(str))