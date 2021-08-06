A = int(input("Enter loop: "))
i = []
num = 0
for i in range(A):
    data = int(input("input num: "))
    i += [data]
while num <= A:
    if i[num] < 0:
        break
    print(i[num])
    num += 1


    
    
    
        
        