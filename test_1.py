# Test 1 - Samuel Vannarith Om Mercado

# Structured English:
"""
Even though there is mulltiple ways to solve question 1, one of the most easiest ways to do it is by creating
a function for each of the two possibles salaries. That is two functions labeled as option1 and option2.
option 1 is going to directly multiply the amount of money per day by the days worked. That is $100x10 = $1,000.
The option2 is going to use exponential. That would be 2^9. we set 2 because the amount doubles, and we set 9 instead
of 10 because we discount the first day with $1. After we get both of the final amounts, we use another function to
compare which value es higher and display a message stating which one is more convenient.
"""



# Pseudocode:
"""
option1
	return 100*days

option2
	return 2^(days - 1)

calculations
	if salary1 > salary2 then
		print option1 is better

	if salary1 = salary2 then
		print both options are the same

	else then
		print option2 is better

main
	set days to 10
	set salary1 to the option1 function
	set salary2 to the option2 function
	print the value of salary1
	print the value of salary2
	call the calculations function

call for the main function
"""