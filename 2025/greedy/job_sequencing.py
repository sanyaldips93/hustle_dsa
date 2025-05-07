# Greedy
class Solution:
    def jobSequencing(self, deadline, profit):
        maxdeadline = 0
        for i in range(len(profit)):
            maxdeadline = max(maxdeadline, deadline[i])
        hash = {i+1:-1 for i in range(maxdeadline)}
        
        arr = [[deadline[i], profit[i]] for i in range(len(profit))]
        arr.sort(key=lambda x:x[1], reverse=True)
        
        cnt, totalprofit = 0, 0
        for i in range(len(arr)):
            for j in range(arr[i][0], -1, -1):
                if j > 0 and hash[j] == -1:
                    cnt += 1
                    totalprofit += arr[i][1]
                    hash[j] = 1
                    break
        return [cnt, totalprofit]

print(Solution().jobSequencing([4,1,1,1], [20,10,40,30]))

# Disjoint Set
class Solution2 :
    def jobSequencing(self, deadline, profit):
        # Function to find the latest available day <= d
        def find(parent, d):
            # If the day is its own parent, it's free
            if parent[d] == d:
                return d
            # Otherwise, go to the parent (next free slot)
            parent[d] = find(parent, parent[d])  # Path compression
            return parent[d]

        # Function to merge day d with day d-1 (marking d as used)
        def union(parent, u, v):
            parent[u] = v

        n = len(profit)
        max_deadline = max(deadline)

        # Initialize DSU parent array where each day points to itself
        parent = [i for i in range(max_deadline + 1)]

        # Pair up jobs with their deadlines and profits
        jobs = list(zip(deadline, profit))

        # Sort jobs by profit in descending order
        jobs.sort(key=lambda x: x[1], reverse=True)

        count = 0         # Number of jobs done
        total_profit = 0  # Total profit made

        # Try to schedule each job
        for d, p in jobs:
            # Find the latest available slot for this job
            available_slot = find(parent, d)

            # If we found a free slot (> 0), schedule the job
            if available_slot > 0:
                # Mark this slot as used by merging it with slot-1
                union(parent, available_slot, available_slot - 1)
                count += 1
                total_profit += p

        return [count, total_profit]
