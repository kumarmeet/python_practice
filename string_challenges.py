## sort string

_str = "uiojklasdfih"

sorted_string = "".join(sorted(_str))

print(sorted_string)

## display data
def display_data():
    item = input("Input item name")
    price = float(input("Input item price"))

    dots = "." * (25 - len(item) + len(str(price)))

    print(item + dots + str(price))


## if password and confirm password are same

def check_confirm_password():
    password:str = input("Input password ->")
    confirm_password:str = input("Input confirm password -> ")

    if password.strip() == confirm_password.strip():
        print("Confirm password is same")
    else:
        print("Confirm password is not same")

## display credit card

def display_credit_card():
    credit_card = input("Input credit card number :: ")

    if not credit_card.isnumeric() or len(credit_card) != 16:
        print("Credit card number must be 16 digit")
        return

    first_twelve_digit = credit_card[len(credit_card) - 4::]

    hide_prefix = ("*" * 4 + " ") * 3 + first_twelve_digit

    print(hide_prefix)


## user id and domain find

def find_userid_domain():
    email = input("Input email address -> ")

    if not email.find("@") or not email.find("."):
        print("Please input valid email address")
        return

    userid = email.split("@")[0]
    domain = email.split("@")[1]

    print(f"User id is {userid} and email domain is {domain}")

## check is string is palindrome or not

def is_palindrome():
    data = input("Input string -> ")
    actual_string = data
    rev_str = data[::-1]

    if actual_string == rev_str:
        print("String is palindrome")
    else:
        print("String is not palindrome")

## convert given string into palindrome

def convert_into_palindrome():
    data = input("Input string -> ")
    reverse_string = data[::-1]

    convert_palindrome = data + reverse_string
    print(convert_palindrome)

## find day month and year
def find_day_month_year():
    ddmmyy = input("Input dd/mm/yyyy -> ")
    day, month, year = ddmmyy.split("/")
    print(f"day {day} month {month} year {year}")

## check anagram of two string
def check_anagram():
    str1 = input("Input 1st string -> ")
    str2 = input("Input 2nd string -> ")

    if sorted(str1) == sorted(str2):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")


## rearrange the string chars first upper and then lower

def rearrange_cases():
    data = input("Input string")

    lower = ""
    upper = ""

    for v in data:
        if v.lower():
            lower += v
        else:
            upper += v

    result = lower + upper

    print(result)

## remove any type of symbols from string

def remove_punctuations():
    data = input("Input string -> ")
    str1 = "!@#$%^&*()_+<>?:~*?/.<>,"
    res = ""

    for v in data:
        if v not in str1:
            res += v
    print(res)

remove_punctuations()