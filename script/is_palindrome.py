from palindrome import first
from palindrome import last
from palindrome import middle

def is_palindrome(word):
    if len(word) <= 1   :
        return True
    if first(word) != last(word):
        return False

    return is_palindrome(middle(word))

print(is_palindrome("redivider"))
