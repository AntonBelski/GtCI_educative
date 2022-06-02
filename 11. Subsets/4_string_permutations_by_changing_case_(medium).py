def swapcase_backtrack(s, result, current, first=0):
    if first == len(s):
        result.append(''.join(current))
        return
    current.append(s[first])
    swapcase_backtrack(s, result, current, first + 1)
    current.pop()

    if s[first].isalpha():
        current.append(s[first].swapcase())
        swapcase_backtrack(s, result, current, first + 1)
        current.pop()


def find_letter_case_string_permutations(s):
    result = []
    current = []
    swapcase_backtrack(s, result, current)
    return result


def main():
    print("String permutations are: " + str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " + str(find_letter_case_string_permutations("ab7c")))


main()
