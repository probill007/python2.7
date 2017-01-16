keimeno1 = raw_input("Dose keimeno")
keimeno2 = list(keimeno1)
pattern1 = '!'
start=0
pos1=0
pos2=0
while pos1<>len(keimeno1):
    a = keimeno1.find(pattern1,pos1,pos1+1)
    if a<>-1:
        c=keimeno2[pos2+1]
        delete=0
        keno=0
        if c.islower():
            delete=1
            print "ok1"
            del keimeno2[pos2]
            pos2-=1
        if pos2+2<len(keimeno2):
            print "ok"
            c=keimeno2[pos2+2]
            print c
            if c.islower()and delete==0:
                del keimeno2[pos2]
                pos2-=1
    pos1+=1
    pos2+=1
print ''.join(keimeno2) 
        
            


