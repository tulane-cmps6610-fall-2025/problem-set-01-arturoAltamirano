  # CMPS 6610 Problem Set 01
## Answers

**Name:** Arturo Altamirano


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a    True, c = 2, n = 1, true for all n > 1
 
  - 1b    False, c = 2, n = 1, true for all n > 1

          The base 2 value in 2 ^ (2 ^ n) will always make this algorithm less efficient than simply 2 ^ n so it will almost unanimously dominate the other. 

  - 1c    False, c = 5, n = 1, true for all n > 1

          Because logarithmic time is always dominated by polynomial time
          log is O(polynomial time)

  - 1d    True, n ^ 1.01 = Ω(log ^ 2 n)

          Because logarithmic time is always dominated by polynomial time
          log is O(polynomial time)

  - 1e    True, c = 9, n = 81, true for all n >= 81

  - 1f    False, at c = 2 for all n >= 81
  
          This sqrt will be dominated by this particular logarithmic operation. 

  - 1g    There exists no values where o(g(n)) ∩ ω(g(n)) since a given n
          cannot be both greater and lesser than c and hold the inequality of g(n) ≤ c ·f(n) or g(n) >= c ·f(n)
          
          Given the example problem of 10x ∈ o(x2), past the value n = 10, there is no c large enough to unequivically dominate the gap between the 2 functions, meaning that for significant n, there exists no c which inherently causes x^2 to NOT dominate 10x

          Even if given c = 1, n = 11 still yields dominance, and the inverse for ω(g(n)) with g(n) >= c ·f(n), even if given c = 1, n = 11 will still yeild inverse-dominance. There is no overlap.

2. **SPARC to Python**

  - 2b 
         1) At the start of each invocation, if either input is equivalent to 0, return the counterpart input among the pair of (a, b) - evaluating them in the order of input a, then input b. 
       
         2) Else if neither input is 0, assign the lesser value to variable x, and the greater to variable y. 
       
         3) Pass (x,y) to a recursive invocation of Foo (step 1 - self), with variable a mapped to variable y, and variable b mapped to the result of variable y mod variable x. 

         4) Ultimately the final output is the greatest value between the 2 inputs.

  - 2c O(log n) seems to be the upper bound for both work and span (see testingSolutions)
          O(log n) ^ 2 seems to be a safer answer. As n log n seems to be close to equivalent.

3. **Parallelism and recursion**

  - 3b O(n log n) as that is the nearest function it is dominated by.

  - 3d Ω(n) and O(n log n) meaning it dominates n runtime, and is dominated by n log n runtimes, it is somewhere in the middle of these.

  - 3e O(log n) for both work and span as these processes would now remove the additional overhead of having to do the entire span of work for every time step.
