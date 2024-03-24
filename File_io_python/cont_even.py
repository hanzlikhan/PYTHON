count = 0
with open("newFile.txt","r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2 == 0):
            count +=1
print(count)
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #     else:
    #         num+=data[i]

