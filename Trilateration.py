def Trilat(routers):
    #routers is a dictionary with n sensors. The keys are the positions
    #of the sensors (latitude and longitude in "45.102N,12.34E" format), 
    #the values are the intensities
    def Coords(routers):
        n=len(routers)
        lat=[]
        long=[]
        for i in range(n):
            dummy=list(routers.keys())[i]
            dummy=dummy.split(',')
            if 'N' in dummy[0]:
                dummy[0]=dummy[0].translate({ord('N'): None})
                dummy[0]=float(dummy[0])
            else:
                dummy[0]=dummy[0].translate({ord('S'): None})
                dummy[0]=-float(dummy[0])
            if 'E' in dummy[1]:
                dummy[1]=dummy[1].translate({ord('E'): None})
                dummy[1]=float(dummy[1])
            else:
                dummy[1]=dummy[1].translate({ord('W'): None})
                dummy[1]=-float(dummy[1])
            lat.append(dummy[0])
            long.append(dummy[1])
            
        return lat,long
    
    lat,long=Coords(routers)
    s=list(routers.values())
    corr_int=[]
    for i in range(len(s)): corr_int.append((s[i]+100))
    a=0
    b=0
    somma=sum(corr_int)
    s_n = [x / somma for x in corr_int]
    for i in range(len(routers)):
        a=a+s_n[i]*lat[i]
        b=b+s_n[i]*long[i]
    return a,b 
        