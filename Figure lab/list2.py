a=[1,2,2,3,3,4,4,5,5,6,6,7,7,8,9,10]
D=[11,20,33,44,49,50,55, 57, 66,68,70, 79, 88,90,98,100]
results=D[1]/a[1]
print(results)
for i in range(10):
    results=D[i]/a[i]
    print(results)
    #training and testing are part of the model
    f=open("marks.txt","w")
    f.write(str(results))
    f.close()
    f2=open("marks.txt","r")
    a=float(f2.read())
    print(a)
    f2.close()