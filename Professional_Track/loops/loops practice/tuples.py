nums=(1,4,9,16,25,36,49,64,81,100)
i=1
x=36
while i<=len(nums)-1:
    if(nums[i]==x):
        print("found at index:",i)
        break
    else:
        print("finding...")
    i+=1