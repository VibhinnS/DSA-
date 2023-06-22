nums = [2,0,2,1,1,0]

array = [0]*3
answer = []

for element in nums:
    array[element] +=1

for i in range(3):
    answer+=[i]*array[i]

print(answer)
