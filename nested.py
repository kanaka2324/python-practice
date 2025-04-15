for i in range(5):
    print("*",end=" ")



for i in range(1,6):
    for j in  range(1,6):
        print("*",end=" ")
    print()



for i in range(1,6):
    for j in  range(1,6):
        print(j,end=" ")
    print()



for i in range(1,6):
    for j in  range(1,6):
        print(i,end=" ")
    print()



for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()




for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()




    for i in range(1,6):
        for j in range(1,6):
            if(j<=i):
               print("*",end=" ")
            else:
                 print(j,end=" ")
        print()



for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


    for i in range(1,6):
        for j in range(1,6):
            if(j<=6-i):
                print(j,end=" ")
            else:
                print(" ",end=" ")
        print()



    for i in range(1,6):
        for j in range(1,6):
            if(j<=6-i):
                 print(i,end=" ")
            else:
                 print(" ",end=" ")
        print()



for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  



    for i in range(1,6):
        for j in range(1,10):
            if(j>=6-i and j<=4+i):
                print(i,end=" ")
            else:
                print("*",end=" ")
        print()     
