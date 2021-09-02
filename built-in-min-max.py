#built-in-min-max.py

#use own function for max
#create maximum() function for 3 values
def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

#use maximum() function to find maximum of three values
print('The maximum using a created function is', maximum(12, 27, 36))

#Use built in function for max
print('The max using a built in function is', max(12, 27, 36))

#Use built in function for min
print('The min using a built in function is', min(15, 9, 27, 14))

#create minimum() function for 4 values
def minimum(arg1, arg2, arg3, arg4):
    """Return the minimum of four values"""
    min_arg = arg1
    if arg2 < min_arg:
        min_arg = arg2
    if arg3 < min_arg:
        min_arg = arg3
    if arg4 < min_arg:
        min_arg = arg4
    return min_arg

#use minimum() function to find minimum of four values
print('The minimum using a created function is', minimum(15, 9, 27, 14))