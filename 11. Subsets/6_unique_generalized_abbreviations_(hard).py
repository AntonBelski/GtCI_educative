def backtrack(word, result, current, start=0, prev=-1):
    for i in range(start, len(word)):
        left = i - prev - 1 if prev + 1 != i else ''
        right = len(word) - 1 - i if i != len(word) - 1 else ''
        current.append(str(left) + word[i])
        result.append(''.join(current) + str(right))
        backtrack(word, result, current, i + 1, i)
        current.pop()


def generate_generalized_abbreviation(word):
    result, current = [str(len(word))], []
    backtrack(word, result, current)
    return result


def main():
    print("Generalized abbreviation are: " + str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " + str(generate_generalized_abbreviation("code")))


main()
