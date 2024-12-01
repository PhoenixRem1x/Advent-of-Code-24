left = []
right = {}
sum = 0
with open("input.txt","r") as f:
    for line in f.readlines():
        nums = line.split()
        
        left.append(nums[0])
        if nums[1] not in right:
            right[nums[1]] = 1
        elif nums[1] in right:
            right[nums[1]] +=1
#print(left)
#print(right)
for i in left:
    if i in right:
        #print(i*right[i])
        sum += (int(i)*int(right[i]))
print(sum)