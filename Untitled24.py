#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#6.write a function to check whether string is a palindrome or not .
string = "mom"
reversed_string = string[::-1]
print(string == reversed_string)
print(reversed_string)


# In[7]:


def is_palindrome(text: str)-> bool:
    """
    check Whether a given string is a palindrome.

    Retrns:
          Returns True if String is a paindrome false otherwise.
    Raises:
          TypeError: If input is not a string.
          ValueError:If input string is empty.
    """

    if not isinstance(text,str):
        raise TypeError("Input must be a string")
    if text.strip() == "":
        raise ValueError("Input string must can not empty.")
    else:
        text =  text.strip().lower()
        reversed_string = ""
        for ch in text:
            reversed_string = ch + reversed_string
        return text == reversed_string
if __name__ == "__main__":
 try:
        user_input = input("Enter your string to check :")
        if is_palindrome(user_input):
            print(f"{user_input} is a palindrome")
        else:
            print(f"{user_input} is not a palindrome")
 except(TypeError,ValueError) as e:
        print("Error:",e)




# In[10]:


#7.count vowel in a string.
#logic building
text = "python"
vowels = "aeiou"
count = 0
for char in text.lower():
   if char in vowels:
       count = count + 1
print(count)


# In[3]:


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the given string.

    Parameters:
        text (str): The input string.

    Returns:
        int: Number of vowels in the string.

    Raises:
        TypeError: If the input is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count = count + 1

    return count


if __name__ == "__main__":
    try:
        user_input = input("Enter your string: ")
        result = count_vowels(user_input)
        print(f"Total vowels: {result}")

    except TypeError as e:
        print("Error:", e)

    except Exception as e:
        print("Error:", e)


# In[7]:


#8.find the second largest element in a list using for loop.
#logic building 
numbers_list = [1,3,90,45,28,90]

if numbers_list[0] > numbers_list[1]:
    largest = numbers_list[0]
    second = numbers_list[1]
else:
    largest = numbers_list[1]
    second = numbers_list[0]
for current_number in numbers_list[2:]:
    if current_number > largest:
        second = largest
        largest = current_number
    elif current_number != largest and current_number > second:
       second = current_number
print(second)



# In[3]:


from typing import List
def second_largest(nums: List[int])->int:
    """ Find the second largest number in a list without using sorting .
    parameters:
        nums (list[int]): A list of integers.
    Returns:
        int:The second largest unique value .
    Raises:
        TypeError:If input is not a list or elements are not integers.
        ValueError: If the list has fewer than 2 unique elements.
    """

    if not isinstance(nums,list):
        raise TypeError("Input must be a list of integers.")
    if any(not isinstance(current_number,int)for current_number in nums):
        raise TypeError("All elements of list should be integers.")
    if len (nums) < 2:
        raise ValueError("list should contain atleast two arguments.")
    if nums[0] > nums[1]:
       largest = nums[0]
       second = nums[1]
    else:
        largest = nums[1]
        second = nums[0]
    for current_number in nums[2:]:
        if current_number > largest:
            second = largest 
            largest = current_number 
        elif current_number != largest and current_number > second:
            second = current_number 
    return second
if __name__ == "__main__":
    numbers_list = [1,23,56,88,90,54]
    try:
        result = second_largest(numbers_list)
    except(TypeError,ValueError) as error:
        print(f"Error: {error}")
    except Exception as e:
        print(e)
    else:
        print("second largest", result)


# In[7]:


#9.sum of digits. do not convert number to string.
#logical building
number = 456
total = 0
while number > 0:
    total = total + number % 10
    number = number//10
print(total)




# In[16]:


def sum_of_digit(n: int) -> int:
    """
    Calculate the sum of digits of a non-negative integer.

    Parameters:
        n (int): The number whose digits will be summed.

    Returns:
        int: Sum of the digits.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """

    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a positive number.")

    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total
if __name__ == "__main__":
    try:
        num = int(input("Enter your number:"))
        result = sum_of_digit(num)
        print(f"sum of digits is {result}")
    except (TypeError,ValueError) as error:
        print("Error",error)



# In[13]:


sum_of_digit(345)


# In[23]:


#10.Remove Duplicate from a list .
List = [100,2,3,6,8,6]
result = []

for i in List:
    if i not in result:
        result.append(i)
result


# In[31]:


from typing import List,Any
def remove_duplicates(List:List[Any])->List[Any]:
    """
    Remove duplicates from a list while maintaining original order.

    Parameters:
         List(List[Any]):A list containing any type of elements.

    Returns:
         List[Any]:A new list with duplicates removed.

    Raises:
         TypeError : If input is not a list.
         ValueError: If the list is empty.
    """
    if not isinstance(List,list):
        raise TypeError("Input must be a list.")
    if len(List) == 0:
        raise ValueError("List must not be empty.")
    if len(List) == 1:
        print("List has already one element.No duplicate to remove")
        return List
    result = []
    for i in List:
        if i not in result:
            result.append(i)
    return result
if __name__ == "__main__":
    numbers_list = [100,45,56,67,89,30,45]
    try:
        result = remove_duplicates(numbers_list)
    except(TypeError,ValueError) as error:
        print("Error:",error)
    except Exception as error:
        print("Error :",error) 
    else:
        print("After removing duplicates :",result)




# In[ ]:




