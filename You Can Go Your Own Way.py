TotalIn=input()
TotalInC = 0
ANS=""
Turn=1
while int(TotalInC) < (int(TotalIn)):
    N=input()
    NC=1
    Path=input()
    Path=str(Path)
    Path=Path.replace("S", "W")
    Path=Path.replace("E", "S")
    Path=Path.replace("W", "E")
    TotalInC=TotalInC+1
    #print(Path)
    print ("Case #"+str(Turn)+": "+str(Path))
    Turn=Turn+1