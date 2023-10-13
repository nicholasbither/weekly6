def factor(n):
    print("the factors of " +str(n) +" are: ")
    for i in range(1,n+1):
        if(n%i) == 0:
            print(i)
