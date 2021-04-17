def is_palindrome(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True


is_palindrome("abba")
# True
is_palindrome("abcba")
# True
is_palindrome("")
# True
is_palindrome("abcd")
# False