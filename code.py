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




# Given a list of n strings with mixed casing, return a new list of all strings that start with a capitalized letter.

# Input: [Strings]
# Output: [Strings]
# Test Cases:
# Input: ["apples", "Bananas", "eggs", "Pina"]
# Output: ["Bananas", "Pina"]


# Create an array to store list of strings that start with capitalize letters
# Iterate through given array of strings
	# Check if current element starts with a capitalized letter
		# Add current element to array
# return created array


def capitalized_list(arr)
	cap_list = []
	for word in arr:
		if word[0].isupper():
			cap_list.append(word)
	return cap_list


# Good Test Cases

capitalized_list(["apples", "Bananas", "lemons", "Torta"])


# Bad Test Cases

capitalized_list(["apples", "Bananas", 9, "Torta"])
capitalized_list(["apples", "Bananas", False, "Torta"])

#Edge Cases

capitalized_list(["apples", "Bananas", "      ", "Torta"])
























