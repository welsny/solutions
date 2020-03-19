class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = {}
        res = i = 0
        for j, fruit in enumerate(tree):
            if fruit not in basket and len(basket) == 2:
                fruit2, i = min(basket.items(), key=lambda x: x[1])
                i += 1
                del basket[fruit2]

            basket[fruit] = j
            res = max(res, j-i+1)

        return res
