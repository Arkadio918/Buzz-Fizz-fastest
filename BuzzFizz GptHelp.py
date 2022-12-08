import time
from functools import lru_cache
import operator

# read the last number from the user
print("insert the last number:")
Limit=input()
Limit=int(Limit)+1


# implementation using an if/else statement
def Classic():
    for i in range(1, Limit):

        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
            
# implementation using a ternary operator
def Alternative1():  # Not mine
    for i in range(1, Limit):
        print("fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or i)
        
# implementation using a list and indexing
def Alternative2():  # Not mine
    for i in range(1, Limit):
        print([i, "buzz", "fizz", "fizzbuzz"][2 * (i % 3 == 0) + (i % 5 == 0)])

def Inline1():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    # outside string declaration
    for i in range(1, Limit):
        print(a if (i % 5 == 0) else b if (i % 3 == 0) else c if (i % 15 == 0) else str(i))
        
def Inline2():
    for i in range(1, Limit):
        a = "bazz"
        b = "fizz"
        c = "fizzbuzz"
        # inside string declaration
        print(a if (i % 5 == 0) else b if (i % 3 == 0) else c if (i % 15 == 0) else str(i))

def Inline3():
    for i in range(1, Limit):
        # no string declaration
        print("bazz" if (i % 5 == 0) else "fizz" if (i % 3 == 0) else "fizzbuzz" if (i % 15 == 0) else str(i))


def RandomTest():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if i % 3 == 0 or i % 5 == 0:
            if i % 5 == 0 and i % 3 == 0:
                print(c)
                continue
            elif i % 3 == 0:
                print(a)
            elif i % 5 == 0:
                print(b)
        else:
            print(i)
#gpt update
def RandomTest2():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if any(i % x == 0 for x in (3, 5)):
            if i % 5 == 0 and i % 3 == 0:
                print(c)
            elif i % 3 == 0:
                print(a)
            elif i % 5 == 0:
                print(b)
        else:
            print(i)
         
def RandomTest3():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if any(i % x == 0 for x in (3, 5)):
            print(c if i % 15 == 0 else a if i % 3 == 0 else b if i % 5 == 0 else i)
        else:
            print(i)
def RandomTest4():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if i % 3 == 0 or i % 5 == 0:
            print(c if i % 15 == 0 else a if i % 3 == 0 else b if i % 5 == 0 else i)
        else:
            print(i)
@lru_cache()
def RandomTest5():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if i % 3 == 0 or i % 5 == 0:
            print(c if i % 15 == 0 else a if i % 3 == 0 else b if i % 5 == 0 else i)
        else:
            print(i)    
def RandomTest6():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if (i & 3 == 0) or (i & 5 == 0):
            print(c if (i & 15 == 0) else a if (i & 3 == 0) else b if (i & 5 == 0) else i) 
        else:
            print(i)

def RandomTest6NoPrint():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    for i in range(1, Limit):
        if (i & 3 == 0) or (i & 5 == 0):
            c if (i & 15 == 0) else a if (i & 3 == 0) else b if (i & 5 == 0) else i
        else:
            pass
           # print(i)
def RandomTest7():
    # create a lookup table that stores the "fizzbuzz" values for numbers from 1 to the maximum number in the input
    lookup = ["bazz" if (i & 5 == 0) else "fizz" if (i & 3 == 0) else "fizzbuzz" if (i & 15 == 0) else str(i) for i in range(1, Limit)]

    # for each number in the input
    for i in range(1, Limit):
        # print the "fizzbuzz" value from the lookup table
        print(lookup[i-1])
        
@lru_cache()
def RandomTest8():
    # create a lookup table that stores the "fizzbuzz" values for numbers from 1 to the maximum number in the input
    lookup = ["bazz" if (i & 5 == 0) else "fizz" if (i & 3 == 0) else "fizzbuzz" if (i & 15 == 0) else str(i) for i in range(1, Limit)]

    # for each number in the input
    for i in range(1, Limit):
        # print the "fizzbuzz" value from the lookup table
        print(lookup[i-1])
        
def FasterBuzzFizz():
  # create a dictionary that maps numbers to their "fizzbuzz" values
  fizzbuzz = {
    3: "fizz",
    5: "buzz",
  }

  # for each number from 1 to the last number
  for i in range(1, Limit+1):
    # initialize the "fizzbuzz" value for the number to an empty string
    value = ""
    # if the number is divisible by 3, append "fizz" to the value
    if i % 3 == 0:
      value += "fizz"
    # if the number is divisible by 5, append "buzz" to the value
    if i % 5 == 0:
      value += "buzz"
    # if the value is still an empty string, set it to the number itself
    if value == "":
      value = i
    # print the "fizzbuzz" value
    print(value)
 
# implementation using a dictionary
def Dictionary():
  # create a dictionary that maps numbers to their "fizzbuzz" values
  fizzbuzz = {
    3: "fizz",
    5: "buzz",
    15: "fizzbuzz"
  }

  # for each number from 1 to the Limit number
  for i in range(1, Limit+1):
    # check if the number is divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
      # if the number is divisible by 15, print "fizzbuzz"
      if i % 15 == 0:
        print(fizzbuzz[15])
      # if the number is divisible by 5, print "buzz"
      elif i % 5 == 0:
        print(fizzbuzz[5])
      # if the number is divisible by 3, print "fizz"
      elif i % 3 == 0:
        print(fizzbuzz[3])
    # if the number is not divisible by 3 or 5, print the number itself
    else:
      print(i)

# create a list of all the implementations aka definitions
implementations = [Classic, Alternative1, Alternative2, Inline1, Inline2, Inline3, RandomTest,RandomTest2,RandomTest3,RandomTest4,RandomTest5,RandomTest6,RandomTest6NoPrint,RandomTest7,RandomTest8,FasterBuzzFizz,Dictionary]
#implementations = [RandomTest6,RandomTest6NoPrint]

# initialize the total time and number of implementations
total_time = 0
num_implementations = len(implementations)

# initialize a dictionary to store the elapsed times for each implementation
elapsed_times = {}

# for each implementation in the list
for implementation in implementations:
  # start the timer
  start_time = time.time()

  # run the implementation
  implementation()

  # stop the timer and calculate the elapsed time
  end_time = time.time()
  elapsed_time = end_time - start_time

  # add the elapsed time to the total time
  total_time = total_time + elapsed_time

  # store the elapsed time for this implementation in the dictionary
  elapsed_times[implementation.__name__] = elapsed_time

# calculate the average time
average_time = total_time / num_implementations

# find the slowest and fastest implementations
slowest = max(elapsed_times.items(), key=operator.itemgetter(1))[0]
fastest = min(elapsed_times.items(), key=operator.itemgetter(1))[0]

# print the total and average times
print("\n= | Total Time : ", round(total_time, 5))
print("= | Average  : ", round(average_time, 5))

# for each implementation in the list
for implementation in implementations:
  # get the elapsed time for this implementation
  elapsed_time = elapsed_times[implementation.__name__]

  # check if the elapsed time is greater than, equal to, or less than the average elapsed time
  if elapsed_time == average_time:
    print("= | {:{}} : {}".format(implementation.__name__, 8, round(elapsed_time, 5)))
  elif elapsed_time > average_time:
    print("↑ | {:{}} : {}".format(implementation.__name__, 8, round(elapsed_time, 5)))
  elif elapsed_time < average_time:
    print("↓ | {:{}} : {}".format(implementation.__name__, 8, round(elapsed_time, 5)))

# print the fastest
if fastest in elapsed_times:
  print("↓ | The fastest is: {:{}}\n↓ | Whit: {}".format(fastest, 8, round(elapsed_times[fastest], 5)))

# print the slowest
if slowest in elapsed_times:
  print("↑ | The slowest is: {:{}}\n↑ | Whit: {}".format(slowest, 8, round(elapsed_times[slowest], 5)))