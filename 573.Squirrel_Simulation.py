class Solution:
    """
    @param height: the height
    @param width: the width
    @param tree: the position of tree
    @param squirrel: the position of squirrel
    @param nuts: the position of nuts
    @return: the minimal distance
    """
    def minDistance(self, height, width, tree, squirrel, nuts):
        if not nuts:
            return 0

        tx, ty = tree
        sx, sy = squirrel
        dists = [abs(tx-nx) + abs(ty-ny) for nx, ny in nuts]

        max_delta = float('-inf')
        for i, d in enumerate(dists):
            nx, ny = nuts[i]
            d2 = abs(sx-nx) + abs(sy-ny)
            if d-d2 > max_delta:
                max_delta = d-d2

        return 2*sum(dists) - max_delta
