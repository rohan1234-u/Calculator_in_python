def X(a,b,c):
    if(c=="+"):
        return a+b
    elif(c=="*"):
        return a*b
    elif(c=="-"):
        return a-b
    elif(c=="/"):
        return a/b

def isFloatnum(str_char):
    try:
        float(str_char)
        return True
    except ValueError:
        return False



def F(list_of_):
    operator_stack = []
    nnumber_stack = []
    n = 0
    d = {}
    d["+"] = []
    d["*"] = []
    d["-"] = []
    d["/"] = []
    total_length = len(list_of_)
    while(n< total_length):
        if(list_of_[n]=="("):
            K = []
            n = n+1
            while(list_of_[n]!=")"):
                K.append(list_of_[n])
                n = n+1
            nnumber_stack.append(F(K))
        elif(isFloatnum(list_of_[n])):
            nnumber_stack.append((list_of_[n]))
        else:
            operator_stack.append(list_of_[n])
            d[list_of_[n]].append(len(operator_stack)-1)
        n = n+1
    #print(d)
    #print(operator_stack)
    #print(nnumber_stack)
    '''
    for indices in d["/"]:
        nnumber_stack[indices]  = nnumber_stack[indices]/nnumber_stack[indices+1]
        nnumber_stack[indices+1] = nnumber_stack[indices]
    for indices in d["*"]:
        nnumber_stack[indices]  = nnumber_stack[indices]*nnumber_stack[indices+1]
        nnumber_stack[indices+1] = nnumber_stack[indices]
    for indices in d["+"]:
        nnumber_stack[indices]  = nnumber_stack[indices]+nnumber_stack[indices+1]
        nnumber_stack[indices+1] = nnumber_stack[indices]
    for indices in d["-"]:
        nnumber_stack[indices]  = nnumber_stack[indices]-nnumber_stack[indices+1]
        nnumber_stack[indices+1] = nnumber_stack[indices]
    print(nnumber_stack)
    return nnumber_stack[0]
    '''
    for indice,ope in enumerate(operator_stack):
        if(ope=="/"):
            nnumber_stack[indice] = nnumber_stack[indice]/nnumber_stack[indice+1]
            nnumber_stack.pop(indice+1)
            operator_stack.pop(indice)
    for indice,ope in enumerate(operator_stack):
        if(ope=="*"):
            nnumber_stack[indice] = nnumber_stack[indice]*nnumber_stack[indice+1]
            nnumber_stack.pop(indice+1)
            operator_stack.pop(indice)
    for indice,ope in enumerate(operator_stack):
        if(ope=="+"):
            nnumber_stack[indice] = nnumber_stack[indice]+nnumber_stack[indice+1]
            nnumber_stack.pop(indice+1)
            operator_stack.pop(indice)

    for indice,ope in enumerate(operator_stack):
        if(ope=="-"):
            nnumber_stack[indice] = nnumber_stack[indice]-nnumber_stack[indice+1]
            nnumber_stack.pop(indice+1)
            operator_stack.pop(indice)
    
    return nnumber_stack[0]
    
            
    




given_ = input()
L = given_.split(" ")
Stack_coll = []
n = len(L)
if(n==1):
    if(L[0].isnumeric()):
        print(L[0])
    else:
        raise Exception("Invalid input")

if(n==3):
    if(L[0].isnumeric() and L[2].isnumeric()):
        print(float(L[0]),L[2],float(L[1]))

postfix_stack = []

Actual_thing = []
#print(L)
for x in L:
    if(isFloatnum(x)):
        Actual_thing.append(float(x))
    else:
        if(x[0]=="("):
            Actual_thing.append("(")
            if(x[len(x)-1]==")"):
                Actual_thing.append(float(x[1:len(x)-1]))
                Actual_thing.append(")")
            else:
                Actual_thing.append(float(x[1:]))
        else:
            if(x[len(x)-1]==")"):
                Actual_thing.append(float(x[0:len(x)-1]))
                Actual_thing.append(")")
            else:
                Actual_thing.append(x)
#print(Actual_thing)
print(F(Actual_thing))



    




    
