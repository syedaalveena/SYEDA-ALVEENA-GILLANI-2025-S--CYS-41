import matplotlib.pyplot as mp
a=["Khizra","Shafia", "Alveena"]
b=[3.0,3.7,2.8]
mp.plot(a,b,marker='o',linestyle='--',)
mp.savefig("new graph.png")
mp.show()
mp.title("new graph")
mp.xlabel("x-axis")
mp.ylabel("y-axis")
