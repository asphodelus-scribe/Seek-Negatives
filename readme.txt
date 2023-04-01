Initialization:
First, take user input for an integer i, with the condition that that the program will exit when -i is reached
Next, accept input for two integers, b and f, where b is the number of integers to count backwards from i, and f the number of integers to count forward from i
By this process form the interval of integers [i-b,i+b] as a set 
Then, accept input for an integer x, which will be the index in set s to start iteration of the main process

Main Runtime Loop:
Decrement n by c
Replace the element of index x in set s with n
if the end of the set is reached, loop back to index 0 in set s
otherwise increment x by one
