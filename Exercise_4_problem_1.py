#!/usr/bin/env python
# coding: utf-8

# ## Problem 1 - Simple temperature calculator (*3 points*)
# 
# In the first problem your aim is to create a function that converts the input temperature from degrees Fahrenheit to degrees Celsius. The conversion formula from Fahrenheit to Celsius can be found below.
# 
#   T_{Celsius} = ( T_{Fahrenheit} - 32 ) / 1.8
# 
# Notice: Closely follow the instructions! 
# 
# Your score on this problem will be based on following criteria:
# 
# - Creating a function called `fahr_to_celsius`
# - Defining the function to have one input parameter called `temp_fahrenheit`
# - Creating a variable called `converted_temp` inside the function to which you should assign the conversion result (i.e., the input Fahrenheit temperature converted to Celsius)
# - Returning the converted value from the function back to the user
# - Answering some questions about functions at the end of this problem
# - Adding comments in your code and a docstring that explains how to use your `fahr_to_celsius` function (i.e., you should write the purpose of the function, parameters, and returned values)

# YOUR CODE HERE
def fahr_to_celsius(temp_fahrenheit):
    converted_temp = (temp_fahrenheit-32)/1.8
    return converted_temp
"""fahr_to_celsius is a function that takes Fahrenheit temperature temp_fahrenheit as an argument, substitutes converted_temp for the value converted to Celsius temperature, and returns converted_temp as the return value."""
# ### Problem 1 tests
# 
# Check that the function produces correct answers for:
# 1. What is 48° Fahrenheit in Celsius? 
# 2. What about 71° Fahrenheit in Celsius?
print("48 degrees Fahrenheit in Celsius is:", fahr_to_celsius(48))
print("71 degrees Fahrenheit in Celsius is:", fahr_to_celsius(71))
# ### Check your code
# 
# - Make sure you used the given variable names
# - Check that you have added necessary comments to your code
# - Check that your function has a docstring that describes what it does
# 
# ### Questions
# 
# We would like you to think about and answer the following questions based on the materials and ideas that you learned during the lecture:
# 
#   1. Is the concept of function clear to you? If not, what do you not understand?
#   2. What are some of the benefits of using functions?
#   
# Write your answers below:

# YOUR ANSWER HERE. Write your answers as comments
#1. yes
#2. Not only will it be easier to see by grouping each function, but debugging will also be more efficient.
#
#

# #### Done!
# 
# That's it! Now you are ready to continue with Problem 2.
