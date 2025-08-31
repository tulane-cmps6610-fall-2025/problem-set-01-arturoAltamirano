"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        #print("a = 0")
        return int(b)
    
    elif b == 0: 
        #print("b = 0")
        return int(a)
    
    else:
        #let (x,y) = (min(a,b), max(a,b))
        (x,y) = (min(a,b), max(a,b))

        #print(x,y)

        #recursive call, need to use return
        return foo(y, y % x)
    
#returned_value = foo(1, 2)
def test_foo():
    assert foo(1,2)
    
def longest_run(mylist, key):
    counters = []
    counter = 0
    #iterate by index to access individual elements
    for x in range(len(mylist)):

        #increment a counter and lazily append every match increment to the list
        if mylist[x] == key:
            counter += 1
            counters.append(counter)

        #streaks been broken so reset to 0 
        else:
            counter = 0

    #just return the highest count we reached
    return max(counters)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    print(longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3)

test_longest_run()

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
#my testing solution is different, but this one i think is closer to what the desired outcome is
#see the notebook if you want to see the version i worked on more/modified
def longest_run_recursive(mylist, key):

    if len(mylist) == 0:
        #print(f"base case 0: {Result(0, 0, 0, True), call_counter}")
        return Result(0, 0, 0, True)

    elif len(mylist) == 1:
        if mylist[0] == key:
            #print(f"base case 1: {Result(1, 1, 1, True), call_counter}")
            return Result(1, 1, 1, True)
        else:
            #print(f"base case 1: {Result(0, 0, 0, False), call_counter}")
            return Result(0, 0, 0, False)

    mid = len(mylist) // 2
    left = mylist[:mid]
    right = mylist[mid:]

    #print(f"left {left}")
    #print(f"right {right}")

    left_result = longest_run_recursive(left, key)
    right_result = longest_run_recursive(right, key)

    #if left side is a full house, add it to the current right left size to get the full run
    #left = [12,12,12] and right may start with 12 
    if left_result.is_entire_range:
        left_size = left_result.left_size + right_result.left_size
    
    #otherwise left is interupted at the end of the run [12,12,3] - so set the current record 
    else:
        left_size = left_result.left_size

    #same as left but inverted for the right size with left overlap 
    if right_result.is_entire_range:
        right_size = right_result.right_size + left_result.right_size
    
    else:
        right_size = right_result.right_size
 
    cross_run = 0
    #trying to capture values over the middle, if the right and left size indicate that the two partitions merge together
    if left_result.right_size > 0 and right_result.left_size > 0:
        cross_run = left_result.right_size + right_result.left_size

    #capture the longest of the results across the partitons 
    longest_size = max(left_result.longest_size, right_result.longest_size, cross_run)
    
    #if the paritions all indicate entire range, we're looking at a full house
    is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    #should we store longest left and longest right? unsure how to handle the values here
    return Result(left_size, right_size, longest_size, is_entire_range)

    #left_size_final = int(max(left_size_track))
    #right_size_final = int(max(right_size_track))

    #print(left_size_final, right_size_final)
    #print(longest_size)

    #return Result(left_size, right_size_final, longest_size, is_entire_range), call_counter


## Feel free to add your own tests here.
def test_longest_run_recursive():
    print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))

test_longest_run_recursive()