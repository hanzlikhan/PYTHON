nums = [1,4,9,16,25,36,49,64,81,100]
targ = 36
i = 0
while i < len(nums):
    if(targ == nums[i]):
        print("target found")
        break
    else:
        print("target not found")
    i+=1