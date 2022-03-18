# in ra hợp số từ 0 đến <100
so_lan_lap=0
a=[]
for i in range(0,100):
    for z in range(1,i+1):
        if i%z == 0:
            so_lan_lap+=1
    if so_lan_lap >2:
        a.append(i)
    so_lan_lap = 0
print(a)


