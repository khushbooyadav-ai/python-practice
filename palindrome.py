def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]

text=input("Enter a word: ")
if is_palindrome(text):
    print("palindrome")

else:
    print("Not a palindrome")