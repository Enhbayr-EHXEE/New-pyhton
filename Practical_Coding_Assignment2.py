# Task 1
def powerN(base, n):
    if n <= 0:  # Base case: checking if n is less than or equal to 0 to handle edge cases
        return 1
    if n == 1:  # Base case: any number to the power of 1 is the number itself
        return base
    else:
        return base * powerN(base, n - 1)
# Task 2
def count_str(long_str, short_str):
    if len(short_str) == 0 or len(long_str) < len(short_str):  # Base case: checking if short_str is empty or long_str is too short
        return 0
    if long_str[:len(short_str)] == short_str:  # Check if the start of long_str matches short_str
        return 1 + count_str(long_str[len(short_str):], short_str)
    else:
        return count_str(long_str[1:], short_str)
#Task3
def countBound(x, y):
    if x > y:  # Base case: if x is greater than y, stop recursion
        return 1
    if x == y:  # Base case: if x equals y, return x (or y)
        return x
    else:
        return x * countBound(x + 1, y)
#Task4 (works using task 2)
def count_char(string1, string2):
    if not string1 or not string2:  # Base case: if either string is empty, stop recursion
        return 0
    else:
        return count_str(string1,string2[0]) + count_char(string1,string2[1:])
#Task5 
def count_even_list(lst):
    if not lst:  # Base case: if the list is empty, stop recursion
        return 0
    if lst[0] % 2 == 0:  # Check if the first element is even
        return 1 + count_even_list(lst[1:])
    else:
        return count_even_list(lst[1:])
    
def main(): #main function
    print(count_even_list([1,3,5,7,9]))

if __name__ == "__main__":
    main()