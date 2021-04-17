def is_palindrome(my_list):
  if len(my_list) <= 1 or not my_list:
    return True
  if my_list[0] != my_list[-1]:
    return False
  return is_palindrome(my_list[1:-1])

# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)