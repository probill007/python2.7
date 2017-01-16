parentheseis = raw_input("Dose akolouthia parenthesewn")
while not set('()').intersection(parentheseis):
    print "Invalid entry."
    parentheseis = raw_input("Dose akolouthia parenthesewn")
pattern = ')'
count1 =0
flag=True
start=0
while flag:
    a = parentheseis.find(pattern,start)
    if a==-1:          
        flag=False
    else:
        count1+=1        
        start=a+1
pattern = '('
count2 =0
flag=True
start=0
while flag:
    a = parentheseis.find(pattern,start)   
    if a==-1:          
        flag=False
    else:               
        count2+=1        
        start=a+1
if count1==count2:
    ok=2
else:
    print " i akolouthia einai lathos"
    ok=1
if ok==2:
    count3=0
    start=0
    if ok==2:
        while len(parentheseis)<>start:
                pattern= ")"
                a = parentheseis.find(pattern,start,start+1)          
                if a<>-1:
                    start+=1
                    count3-=1
                else:
                    count3+=1
                    start+=1
                if count3<0:
                    print "i akolouthia einai lathos"
                    break
    if count3>=0:
        print "i akolouthia einai swsth"
