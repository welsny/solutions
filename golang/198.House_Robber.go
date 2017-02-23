package main

func rob(nums []int) int {

	if len(nums) == 0 {
		return 0
	}

	maxs := map[int]int{}

	for i, value := range nums {

		var p1_max, p2_max int

		if val, ok := maxs[i-1]; ok {
			p1_max = val
		} else {
			p1_max = 0
		}

		if val, ok := maxs[i-2]; ok {
			p2_max = val
		} else {
			p2_max = 0
		}

		maxs[i] = max(value+p2_max, p1_max)
		fmt.Println(i, maxs)
	}

	return maxs[len(nums)-1]
}

func max(n, m int) int {
	if m > n {
		return m
	}
	return n
}
