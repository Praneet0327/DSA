nums = [1,3,7,5,3]
target = 6
for i in range(0, len(nums)-1):
            a = target-nums[i]
            if a in nums[i+1:]:
                t = []
                t.append(i)
                if i==nums.index(a):
                    ind = nums[i+1:].index(a)
                    t.append(ind+i+1)
                else:
                    t.append(nums.index(a))
                print(t)
            else:
                continue