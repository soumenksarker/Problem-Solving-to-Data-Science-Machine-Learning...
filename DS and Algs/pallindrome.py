def reverse(text):
    return text[::-1]

def is_pallindrome(text):
    return text == reverse(text)

something = input("Enter a text")

if is_pallindrome(something):
    print ("Yes, it is a pallindrome")
else:
    print ("No, it is not a pallindrome")
