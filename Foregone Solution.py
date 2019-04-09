InputBase=input()
TimesRAN=0
Turn=1
while int(TimesRAN) < int(InputBase) :
    Input=input()
    InputS=str(Input)
    MA=[]
    MAR=0
    DP=0
    for x in Input :
        MA.append(int(Input[MAR]))
        MAR=MAR+1
    #print(MA)
    Fours=MA.count(4)
    while Fours > 0 :
        T1=""
        itm=0
        for i in MA: 
            ZZZS=MA[itm]
            #print(ZZZS)
            T1=T1+str(ZZZS)
            itm=itm+1
        try:
            DP=MA.index(4)
        except ValueError:
            K=0
        #print(DP)
        MA.pop(DP)
        MA.insert(DP,3)
        Fours=MA.count(4)
        #print(ZZZ)
        itm2=0
        T2=""
        for i in MA:
            ZZZS=MA[itm2]
            #print(ZZZS)
            T2=T2+str(ZZZS)
            itm2=itm2+1
            #print(T2)
    T4=abs(int(Input)-int(T2))
    #print(T1)
    #print(T2)
    print ("Case #"+str(Turn)+": "+str(T4)+" "+str(T2))
    TimesRAN=TimesRAN+1
    Turn=Turn+1
