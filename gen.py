import random
multi=40
def randomNumber(x,y,rooms,rooms2):
    num=rooms2[rooms.index([x,y])]
    if num == 2:
        ava=[1,2,3,4,5,0,2,2,2]
        return ava[random.randint(0,len(ava)-1)]
    elif num==1:
         ava=[3,2,0,2,2]
         return ava[random.randint(0,len(ava)-1)]
    elif num==3:
         ava=[3,2,0,2,2]
         return ava[random.randint(0,len(ava)-1)]
    elif num==4:
         ava=[2,5,0,2,2]
         return ava[random.randint(0,len(ava)-1)]
    elif num ==5:
         ava=[4,2,0,2,2]
         return ava[random.randint(0,len(ava)-1)]
    elif num == 0:
        ava=[1,2,3,4,5,0,2,2,2]
        return ava[random.randint(0,len(ava)-1)]
    else:
        return 5
def checkAvaible(width,height,x,y,rooms,rooms2):
    tests=[x-1, x+1]
    tests2=[y-1, y+1]
    for xs in tests:
        if xs<0 or xs>width:
            continue
        for i in rooms:
            if i!= [xs,y] and [xs,y] not in rooms:
                rooms.append([xs,y])
                rooms2.append(randomNumber(x,y,rooms,rooms2))
                break
                
    for ys in tests2:
        if ys<0 or ys>height:
            continue
        for i in rooms:
            if i!= [x,ys] and [x,ys] not in rooms:
                    rooms.append([x,ys])
                    rooms2.append(randomNumber(x,y,rooms,rooms2))
                    break
    return True
def cleanRooms(rooms,rooms2):
    for _ in range(len(rooms2)):
        try:
            w=rooms2.index(0)
            rooms2.remove(rooms2[w])
            rooms.remove(rooms[w])
        except:
            pass