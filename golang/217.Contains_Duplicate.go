package main

func containsDuplicate(nums []int) bool {
	seen := map[int]bool{}

	for _, val := range nums {
		if _, ok := seen[val]; ok {
			return true
		}
		seen[val] = true
	}
	return false
}
