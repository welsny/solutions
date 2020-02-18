class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        """
        Naive -- scan entire matrix. This passes Lintcode, but is slower because it
        will always search the entire matrix.

        O(N*M) runtime
        O(1) space
        """
        min_x = max_x = x
        min_y = max_y = y

        for x, row in enumerate(image):
            for y, pixel in enumerate(row):
                if pixel == "1":
                    min_x = min(min_x, x)
                    max_x = max(max_x, x)
                    min_y = min(min_y, y)
                    max_y = max(max_y, y)

        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def minArea(self, image, x, y):
        """
        Here we do a DFS which uses more memory. However, we don't check the entire
        matrix -- the complexity is linear with respect to the number of black pixels
        that we have.

        O(k) runtime, where k is the number of black pixels
        O(k) space, since we use a stack for DFS
        """
        n, m = len(image), len(image[0])

        def adj(x, y):
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < n and 0 <= j < m:
                    yield i, j

        min_x = max_x = x
        min_y = max_y = y

        stack = [(x, y)]
        while stack:
            x, y = stack.pop()

            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)

            image[x][y] = "0"

            for i, j in adj(x, y):
                if image[i][j] == "1":
                    stack.append((i, j))

        return (max_x - min_x + 1) * (max_y - min_y + 1)
