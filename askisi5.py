print " Oi arithmoi Harshard mexri to 1000 einai"
for i in range (0,2):
        for j in range (0,10):
                for k in range (0,10):
                        for l in range (0,10):
                                num=i*1000+j*100+k*10+l+0.0
                                sum=i+j+k+l
                                if sum<>0:
                                        condition=num%sum
                                        if condition==0:
                                                print num
                                        if num==1000:
                                                break
                        if num==1000:
                                break
                if num==1000:
                        break	
        if num==1000:
                break
print "arithmoi pou to ginomeno ton psifion tous diairei ton idio ton arithmo"
for a in range (0,1):
        for b in range (0,10):
                for c in range (0,10):
                        for d in range (0,10):
                                num=a*1000+b*100+c*10+d+0.0
                                if a<>0:
                                        prod=a*b*c*d
                                elif a==0 and b<>0:
                                        prod=b*c*d
                                elif a==0 and b==0 and c<>0:
                                        prod=c*d
                                else:
                                        prod=d
                                if prod<>0:
                                        condition=num%prod
                                        if condition==0:
                                                print num
                                        if num==1000:
                                                break
                        if num==1000:
                                break
                if num==1000:
                        break	
        if num==1000:
                break

