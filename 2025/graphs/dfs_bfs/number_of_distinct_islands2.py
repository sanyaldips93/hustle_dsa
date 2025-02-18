from typing import List

class Solution:
    def countDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        unique = set()

        def dfs(r, c, rr, rc, shape):
            """DFS to extract island shape relative to (rr, rc)."""
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return
            visit.add((r, c))
            shape.append((r - rr, c - rc))  # Relative coordinates
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(r + dr, c + dc, rr, rc, shape)

        def normalize(shape):
            """Generate all 8 transformations and return the smallest one."""
            transformations = [[] for _ in range(8)]
            for x, y in shape:
                transformations[0].append((x, y))    # Original
                transformations[1].append((y, -x))   # 90° Rotation
                transformations[2].append((-x, -y))  # 180° Rotation
                transformations[3].append((-y, x))   # 270° Rotation
                transformations[4].append((x, -y))   # Horizontal Reflection
                transformations[5].append((-x, y))   # Vertical Reflection
                transformations[6].append((y, x))    # Reflection across y = x
                transformations[7].append((-y, -x))  # Reflection across y = -x

            # Normalize each transformation by translating to (0, 0)
            normalized = []
            for t in transformations:
                # Find the top-left corner of the shape
                min_x = min(x for x, y in t)
                min_y = min(y for x, y in t)
                # Translate the shape so that its top-left corner is at (0, 0)
                translated = sorted((x - min_x, y - min_y) for x, y in t)
                normalized.append(tuple(translated))

            # Return the smallest transformation
            return min(normalized)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    shape = []
                    dfs(r, c, r, c, shape)
                    normalized_shape = normalize(shape)
                    unique.add(normalized_shape)

        return len(unique)

# ✅ Test Case
print(Solution().countDistinctIslands2([[1,1,0,1], [1,0,1,1]]))  # Expected Output: 1