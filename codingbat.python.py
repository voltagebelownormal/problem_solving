# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative

def pos_neg(a, b, negative):
   if negative:
       return a < 0 and b < 0

   return a < 0 and b < 0 or a > 0 and b < 0


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if str[0:3] != "not":
        str = "not" + str

    return str


# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    return str[:n] + str[n + 1:]


# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) >= 2:
        return str[-1] + str[1:-1] + str[0]

    return str


# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

def front3(str):
    front = ""

    if len(str) < 3:
        front = str
    else:
        front = str[0:3]

    return front * 3


# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    return str * n


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
    front = ""

    if len(str) < 3:
        front = str
    else:
        front = str[:3]

    return front * n


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"

def string_bits(str):
    result = ""

    for i in range(0, len(str), 2):
        result += str[i]

    return result


# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ""

    for i in range(len(str) + 1):
        result += str[:i]

    return result


# Given a string, return the count of the number of times that a substring length 2 appears
# in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    pattern = str[-2:]
    count = 0

    for i in range(len(str)-2):
        if str[i:i+2] == pattern:
           count += 1

    return count


# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0

    for i in nums:
        if i == 9:
            count += 1

    return count


# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

def array_front9(nums):

    count = 0
    array_ln = 4

    if len(nums) < 4:
        array_ln = len(nums)

    for i in range(array_ln):
        if nums[i] == 9:
            return True

    return False


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    if len(nums) < 3:
        return False

    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True

    return False


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    length = min(len(a), len(b))
    count = 0

    for i in range(length):
        if a[i:i+2] == b[i:i+2]:
            count += 1

    return count


# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
    return a + b + b + a


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  return "<" + tag + ">" + word + "<" + "/" + tag + ">"


# Given an "out" string length 4, such as "<<>>", and a word,
# return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    return out[0:2] + word + out[2:]


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
# The string length will be at least 2.

def extra_end(str):
    return str[-2:] * 3


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
    if len(str) > 2:
        str = str[0:2]

    return str


# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    return str[0:len(str) / 2]


# Given a string, return a version without the first and last char, so "Hello" yields "ell".
# The string length will be at least 2.

def without_end(str):
    return str[1:-1]


# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.

def left2(str):
  return str[2:] + str[:2]


# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    return sum(nums)


# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


# Given an array of ints length 3, figure out which is larger,
# the first or last element in the array, and set all the other elements to be that value.
# Return the changed array.

def max_end3(nums):
    if nums[0] > nums[2]:
        nums[2] = nums[1] = nums[0]
    else:
        nums[0] = nums[1] = nums[2]

    return nums


# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
    if len(nums) < 2:
        return sum(nums)

    return nums[0] + nums[1]


# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

def in1to10(n, outside_mode):
  if outside_mode:
      return n <= 1 or n >= 10

  return n in range(1, 11)


# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
   # Check if we have enough 1 inch bricks to fill out the reminder:
   if goal % 5 > small:
     return False

   small -= goal % 5
   small /= 5
   return small + big >= goal / 5


# Given a string, return a string where for every char in original, there are two chars

def double_char(str):
    result = ""

    for ch in str:
        result += ch * 2

    return result


# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
    return str.count("hi")













