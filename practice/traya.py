class Solution():
    def threeSum(self, arr):
        # Sort this
        arr.sort()
        res = []
        # Pick one number in a loop
        for i in range(len(arr)-2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            first = arr[i]
            # use the other part of the array for two pointers
            target = 0 - first
            start = i+1
            end = len(arr) - 1
            while start < end:
                second = arr[start]
                third = arr[end]
                sum = second + third
                if sum == target:
                    res.append([first, second, third])
                    start += 1
                    # while arr[start] == arr[start-1] and start < end:
                    #     start += 1
                elif sum > target:
                    end -= 1
                else:
                    start += 1
        
        return res
    
print(Solution().threeSum([-2, -1, -1, -1, 0, 1]))



class Solution:
    def productOfArray(self, nums):
        n = len(nums)
        forwardP = [1] * n
        backwardP = [1] * n
        res = []
        
        prev = forwardP[0]
        for i in range(1, n):
            forwardP[i] = prev * nums[i-1]
            prev = forwardP[i]
        
        prev = backwardP[n-1]
        for i in range(n-2, -1, -1):
            backwardP[i] = prev * nums[i+1]
            prev = backwardP[i]
        
        for i in range(n):
            res.append(backwardP[i] * forwardP[i])
        
        return res

print(Solution().productOfArray([1,2,3,4]))