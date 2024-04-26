from keras.models import load_model
import csv, math
import numpy as np
model = load_model('./ball_model.h5')
if __name__=="__main__":
    t1=input("Enter Team1 ")
    t2=input("Enter Team2")
    with open("playing12.csv","r") as f:
        s=f.readlines()
        c=[]
        for i in s:
            c.append(i.split(','))

    p1=[]
    p2=[]
    for i in c:
        if i[1]==t1:
            p1=i[2:]
        elif i[1]==t2:
            p2=i[2:]

    score1=0
    rem=120
    for i in p1:
        with open("last10.csv","r") as f:
            ch=[]
            for p in f.readlines():
                ch.append(p.split(','))
            
            for p in ch:
                if i==p[1]:
                    avg=list(map(float, p[-10:]))
                    avg = sum(avg)/10
                    balls=list(map(int, p[13:23]))
                    preds = math.ceil(model.predict(np.array([balls]))[0][0])
                    mult  = int(preds)

                    if( mult>rem ):
                        mult=rem

                    runs = math.ceil(mult*avg)
                    score1+=runs
                    rem-=mult

                    if( rem==0 ):
                        break

    score2=0
    rem=120
    for i in p2:
        with open("last10.csv","r") as f:
            ch=[]
            for p in f.readlines():
                ch.append(p.split(','))
            
            for p in ch:
                if i==p[1]:
                    avg=list(map(float, p[-10:]))
                    avg = sum(avg)/10
                    balls=list(map(int, p[13:23]))
                    preds = math.ceil(model.predict(np.array([balls]))[0][0])
                    mult  = int(preds)

                    if( mult>rem ):
                        mult=rem

                    runs = math.ceil(mult*avg)
                    score2+=runs
                    rem-=mult

                    if( rem==0 ):
                        break
    print("t1:",score1)
    print("t2: ",score2)
    if score1>score2:
        print("Winner: ",t1)
    elif score1<score2:
        print("Winner: ",t2)
    else:
        print("Lets go for a super over")




