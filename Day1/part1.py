list1 = []
list2 = []
sum = 0
with open("input.txt","r") as file:
    for line in file.readlines():
        nums = line.split()
        #print(nums)
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
list1.sort()
list2.sort()
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])
print(sum)