class Solution:    
    def minimumPlatform(self, arr, dep):
        # Sort both arrival and departure times
        arr.sort()
        dep.sort()

        n = len(dep)

        i = j = 0           # i -> index for arrivals, j -> index for departures
        ans = 1             # Stores the maximum platforms needed at any time
        count = 0           # Current count of platforms in use

        # Loop through all trains
        while i < n:
            if arr[i] <= dep[j]:
                # New train has arrived before the earliest train departs
                # So we need an extra platform
                count += 1
                i += 1
            else:
                # A train has departed before the next one arrives
                # So we can free a platform
                count -= 1
                j += 1

            # Update the maximum number of platforms needed
            ans = max(ans, count)

        return ans
