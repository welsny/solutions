class Solution:
    def trap(self, height: List[int]) -> int:
        stack, res = [], 0
        for j, h in enumerate(height):
            if stack and h >= stack[-1][1]:
                while stack and h > stack[-1][1]:
                    i, prev_height = stack.pop()
                if stack:
                    i, prev_height = stack[-1]

                for k in range(i+1, j):
                    new_h = min(prev_height, h)
                    res += new_h - height[k]
                    height[k] = new_h

            stack.append((j, h))
        return res