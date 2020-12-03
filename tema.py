list=[7,8,9,2,3,1,4,10,5,6]
ascendent_list=list.copy()
ascendent_list.sort()
print(ascendent_list) #afisarea unei liste ordonate ascendent
ascendent_list.reverse()
print(ascendent_list) #afisarea unei liste ordonate descendent
print(ascendent_list[::2]) #afisarea nr pare
print(ascendent_list[1::2]) #afisarea nr impare
print(list[0:12:3]) #afisarea elementelor multipli ai lui 3 din lista initiala
print(ascendent_list[0:12:3]) #afisarea elementelor multipli ai lui 3 din lista ordonata descrescator