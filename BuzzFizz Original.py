#for every number divisible by 3 print fizz
#for every number divisible by 5 print buzz
#for every number divisible by 3 and 5 print fizzbuzz

import time
from functools import lru_cache
import operator

#Limit = 100
print("insert the last number:")
Limit=input()
Limit=int(Limit)+1
@lru_cache(maxsize=None)
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


@lru_cache(maxsize=None)
def Alternative1():  # Not mine
    for i in range(1, Limit):
        print("fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or i)


@lru_cache(maxsize=None)
def Alternative2():  # Not mine
    for i in range(1, Limit):
        print([i, "buzz", "fizz", "fizzbuzz"][2 * (i % 3 == 0) + (i % 5 == 0)])


@lru_cache(maxsize=None)
def Inline1():
    a = "bazz"
    b = "fizz"
    c = "fizzbuzz"
    # outside string declaration
    for i in range(1, Limit):
        print(a if (i % 5 == 0) else b if (i % 3 == 0) else c if (i % 15 == 0) else str(i))


@lru_cache(maxsize=None)
def Inline2():
    for i in range(1, Limit):
        a = "bazz"
        b = "fizz"
        c = "fizzbuzz"
        # inside string declaration
        print(a if (i % 5 == 0) else b if (i % 3 == 0) else c if (i % 15 == 0) else str(i))


@lru_cache(maxsize=None)
def Inline3():
    for i in range(1, Limit):
        # no string declaration
        print("bazz" if (i % 5 == 0) else "fizz" if (i % 3 == 0) else "fizzbuzz" if (i % 15 == 0) else str(i))


@lru_cache(maxsize=None)
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


##run the tests
Flag0 = time.time()  # start
Classic()
Flag1 = time.time()  # stop cla
Alternative1()
Flag2 = time.time()  # stop alt
Alternative2()
Flag3 = time.time()  # stop alt2
Inline1()
Flag4 = time.time()  # stop in1
Inline2()
Flag5 = time.time()  # stop in2
Inline3()
Flag6 = time.time()  # stop in3
RandomTest()
Flag7 = time.time()  # stop RT
#
Flag_time1 = Flag1 - Flag0
Flag_time2 = Flag2 - Flag1
Flag_time3 = Flag3 - Flag2
Flag_time4 = Flag4 - Flag3
Flag_time5 = Flag5 - Flag4
Flag_time6 = Flag6 - Flag5
Flag_time7 = Flag7 - Flag6
# create a dict whit flag names end flag times
flag_list = {"Flag1": Flag_time1, "Flag2": Flag_time2, "Flag3": Flag_time3, "Flag4": Flag_time4, "Flag5": Flag_time5,
             "Flag6": Flag_time6, "Flag7": Flag_time7}

# total time
Flag7_0 = (Flag7 - Flag0)
# calc the average
average = Flag7_0 / 7

# print the total end average times
print("\n= |    Total Time : ", round(Flag7_0, 5))
print("= |       average : ", round(average, 5))

# check if more then average
if Flag_time1 == average:
    print("= |       Classic : ", round(Flag_time1, 5))
if Flag_time1 > average:
    print("↑ |       Classic : ", round(Flag_time1, 5))
if Flag_time1 < average:
    print("↓ |       Classic : ", round(Flag_time1, 5))
# check if more then average
if Flag_time2 == average:
    print("= |  Alternative1 : ", round(Flag_time2, 5))
if Flag_time2 > average:
    print("↑ |  Alternative1 : ", round(Flag_time2, 5))
if Flag_time2 < average:
    print("↓ |  Alternative1 : ", round(Flag_time2, 5))
# check if more then average
if Flag_time3 == average:
    print("= |  Alternative2 : ", round(Flag_time3, 5))
if Flag_time3 > average:
    print("↑ |  Alternative2 : ", round(Flag_time3, 5))
if Flag_time3 < average:
    print("↓ |  Alternative2 : ", round(Flag_time3, 5))
# check if more then average
if Flag_time4 == average:
    print("= |       Inline1 : ", round(Flag_time4, 5))
if Flag_time4 > average:
    print("↑ |       Inline1 : ", round(Flag_time4, 5))
if Flag_time4 < average:
    print("↓ |       Inline1 : ", round(Flag_time4, 5))
# check if more then average
if Flag_time5 == average:
    print("= |       Inline2 : ", round(Flag_time5, 5))
if Flag_time5 > average:
    print("↑ |       Inline2 : ", round(Flag_time5, 5))
if Flag_time5 < average:
    print("↓ |       Inline2 : ", round(Flag_time5, 5))
# check if more then average
if Flag_time6 == average:
    print("= |       Inline3 : ", round(Flag_time6, 5))
if Flag_time6 > average:
    print("↑ |       Inline3 : ", round(Flag_time6, 5))
if Flag_time6 < average:
    print("↓ |       Inline3 : ", round(Flag_time6, 5))
# check if more then average
if Flag_time7 == average:
    print("= |    RandomTest : ", round(Flag_time7, 5))
if Flag_time7 > average:
    print("↑ |    RandomTest : ", round(Flag_time7, 5))
if Flag_time7 < average:
    print("↓ |    RandomTest : ", round(Flag_time7, 5))

# check the slowest
temp_x = max(flag_list.items(), key=operator.itemgetter(1))[0]
temp_xx = str(temp_x)
# check the fastest
temp_y = min(flag_list.items(), key=operator.itemgetter(1))[0]
temp_yy = str(temp_y)
# print the slowest
if temp_xx == "Flag1":
    print("↑ | The slowest is: ", "Classic     \n↑ | Whit:", round(flag_list["Flag1"], 5))
elif temp_xx == "Flag2":
    print("↑ | The slowest is: ", "Alternative1\n↑ | Whit:", round(flag_list["Flag2"], 5))
elif temp_xx == "Flag3":
    print("↑ | The slowest is: ", "Alternative2\n↑ | Whit:", round(flag_list["Flag3"], 5))
elif temp_xx == "Flag4":
    print("↑ | The slowest is: ", "Inline1     \n↑ | Whit:", round(flag_list["Flag4"], 5))
elif temp_xx == "Flag5":
    print("↑ | The slowest is: ", "Inline2     \n↑ | Whit:", round(flag_list["Flag5"], 5))
elif temp_xx == "Flag6":
    print("↑ | The slowest is: ", "Inline3     \n↑ | Whit:", round(flag_list["Flag6"], 5))
elif temp_xx == "Flag7":
    print("↑ | The slowest is: ", "RandomTest  \n↑ | Whit:", round(flag_list["Flag7"], 5))
else:
    pass
# print the fastest
if temp_yy == "Flag1":
    print("↓ | The fastest is: ", "Classic    \n↓ | Whit:", round(flag_list["Flag1"], 5))
elif temp_yy == "Flag2":
    print("↓ | The fastest is: ", "Alternative1\n↓ | Whit:", round(flag_list["Flag2"], 5))
elif temp_yy == "Flag3":
    print("↓ | The fastest is: ", "Alternative2\n↓ | Whit:", round(flag_list["Flag3"], 5))
elif temp_yy == "Flag4":
    print("↓ | The fastest is: ", "Inline1     \n↓ | Whit:", round(flag_list["Flag4"], 5))
elif temp_yy == "Flag5":
    print("↓ | The fastest is: ", "Inline2     \n↓ | Whit:", round(flag_list["Flag5"], 5))
elif temp_yy == "Flag6":
    print("↓ | The fastest is: ", "Inline3     \n↓ | Whit:", round(flag_list["Flag6"], 5))
elif temp_yy == "Flag7":
    print("↓ | The fastest is: ", "RandomTest  \n↓ | Whit:", round(flag_list["Flag7"], 5))
else:
    pass
