# Leetcode_problems
Leetcode problems that I have resolved (Check inside each file to see runtime).

  1. Two Sum: At first I used nested loops (2 'for') to iterate through each number at search for numbers which added equal to the target, but the complexity was O(n^2) so I used a dictionary to iterate through the list just one time and check for it's index by adding the already seen numbers which were not equal to the complement (target - number) to the dictionary and just returning the position where the condition was accomplished (O(n)).
  9. Palindrome Number: I separated each number into a list and then join (.join and map functions) them in a single variable, convert it into an int and then compare it to the original x value to check if it was equal or not.
