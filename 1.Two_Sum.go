package main

func twoSum(nums []int, target int) []int {
	var seen map[int]int
	seen = make(map[int]int)

	for i, num := range nums {
		if val, ok := seen[target-num]; ok {
			return []int{val, i}
		}
		seen[num] = i
	}

	return []int{-1, -1}
}
