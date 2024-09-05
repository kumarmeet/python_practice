from typing import List


## remove duplicates

def remove_duplicates(data: List[int]):
    l2 = []

    for x in data:
        if x not in l2:
            l2.append(x)

    print(l2)


remove_duplicates([1, 2, 3, 6, 5, 8, 1, 2, 4, 9, 3])


## concat all int and form a single number

def concat_single(data: List[int]):
    res = ""

    for i in data:
        res += str(i)

    print(int(res))


concat_single([1, 2, 5, 6, 33])


## overlapping elements

def find_overlapping(arr1: List[int], arr2: List[int]):
    res = []

    for i in arr1:
        if i in arr2:
            res.append(i)

    print(res)


find_overlapping([10, 15, 6, 9, 12, 8, 4], [14, 6, 19, 4, 7, 10, 11])


## find occurrences of each element

def find_occurrences(data: List[int | str]):
    occurrences = []

    data.sort()

    i = 0

    while i < len(data):
        cnt = data.count(data[i])
        occurrences.append([data[i], cnt])
        i += cnt

    print(occurrences)


find_occurrences(["a", "t", "a", "r", "e", "t", "t"])


## convert string to morse code

def convert_string_morse_code(data: str):
    morse_code_list = [
        ".-",  # A
        "-...",  # B
        "-.-.",  # C
        "-..",  # D
        ".",  # E
        "..-.",  # F
        "--.",  # G
        "....",  # H
        "..",  # I
        ".---",  # J
        "-.-",  # K
        ".-..",  # L
        "--",  # M
        "-.",  # N
        "---",  # O
        ".--.",  # P
        "--.-",  # Q
        ".-.",  # R
        "...",  # S
        "-",  # T
        "..-",  # U
        "...-",  # V
        ".--",  # W
        "-..-",  # X
        "-.--",  # Y
        "--..",  # Z

        "-----",  # 0
        ".----",  # 1
        "..---",  # 2
        "...--",  # 3
        "....-",  # 4
        ".....",  # 5
        "-....",  # 6
        "--...",  # 7
        "---..",  # 8
        "----.",  # 9

        ".-.-.-",  # .
        "--..--",  # ,
        "..--..",  # ?
        ".----.",  # '
        "-.-.--",  # !
        "-..-.",  # /
        "-.--.",  # (
        "-.--.-",  # )
        ".-...",  # &
        "---...",  # :
        "-.-.-.",  # ;
        "-...-",  # =
        ".-.-.",  # +
        "-....-",  # -
        "..--.-",  # _
        ".-..-.",  # "
        "...-..-",  # $
        ".--.-."  # @
    ]

    morse_code = ""

    for i in data:
        morse_code += morse_code_list[ord(i) - 97] + " "

    print(morse_code)

convert_string_morse_code("abc")

## add two matrix

def print_matrix(data:List[List[int]]):
    for i in range(len(data)):
            print(data[i])

def add_two_matrix(data1:List[List[int]], data2:List[List[int]]):
    result = []

    print_matrix(data1)
    print_matrix(data2)

    for i in range(3):
        check = []
        for j in range(3):
            check.append(data1[i][j] + data2[i][j])
        result.append(check)

    print_matrix(result)

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]

add_two_matrix(matrix1, matrix2)
