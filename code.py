# Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t).

# Input: [Int], Int
# Output: [Int]
# Test Case:
# [1,3,4,6], 5  
# [1,5]


# Create a dictionary
# Iterate through the array
	# Check if target - current value is in dictionary
		# return current value and x
	# Add current value to dictionary
# return no pair


def two_sum(arr, target):
	dict = {}
	for i in arr:
		if target - i in dict:
			return [target - i, i]
		dict[i] = True
	return None

# Good Test Cases

two_sum([1,3,4,6], 5)

# Bad Test Cases

two_sum([1,3,4,6], 10)
two_sum([1,3,4, "egg"], 10)


# Edge Cases

two_sum([1,3,-4,6], -3)












