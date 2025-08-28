  # CMPS 6610 Problem Set 01
## Answers

**Name:**___Arturo Altamirano_____
**Name:**_________________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a    True, c = 2, n = 1, true for all n > 1
 
  - 1b    False, c = 2, n = 1, true for all n > 1
          The base 2 value in 2 ^ (2 ^ n) will always make this algorithm less efficient than simply 2 ^ n so it will instead dominante the other. 

  - 1c    c = 5, n = 1, true for all n > 0
          because logarithmic time is always dominated by polynomial time
          log is O(polynomial time)

  - 1d    True, n ^ 1.01 = Ω(log ^ 2 n)
          because logarithmic time is always dominated by polynomial time
          log is O(polynomial time)

  - 1e    c = 9, n = 81, true for all n >= 81

  - 1f    True, at n >= 81 for c = 2, sqrt(n) will always  
          be at least (log ^ 3 n) runtime and can be said to be of omega order.

  - 1g  

2. **SPARC to Python**

  - 2b 
       1) At the start of each invocation, if either input is equivalent to 0, return the counterpart input among the pair of (a, b) - evaluating them in the order of input a, then input b. 
       
       2) Else if neither input is 0, assign the lesser value to variable x, and the greater to variable y. 
       
       3) Pass (x,y) to a recursive invocation of Foo (step 1 - self), with variable a mapped to variable y, and variable b mapped to the result of variable y mod variable x. 

  - 2c O(n) for both work and span

3. **Parallelism and recursion**

  - 3b O(log n) for both work and span. As you need to recur   at most as much as the size of your input. 

  - 3d 

  - 3e
