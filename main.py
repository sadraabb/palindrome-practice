# تابع دریافت ورودی از کاربر
def get_user_input():
    while True:
        user_input = input("Please enter the word to check for palindrome:\n")
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter letters only.")
# تابع بررسی این که واژه یا جمله ای که کاربر وارد کرده پالین‌دروم  هست یا نه 
# تابع به صورت بولین تعریف شده 
def check_palindrome(word : str) -> bool:
    # متغیر معکوس سازی رشته به روش slicing
    reversed_word = word[::-1]
    return reversed_word == word

if __name__ == "__main__":
    word = get_user_input()
    if check_palindrome(word):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")