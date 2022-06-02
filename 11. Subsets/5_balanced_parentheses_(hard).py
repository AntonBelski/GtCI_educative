def recursive_parentheses(result, parentheses, cur, n, balance=0, ind=0):
    if ind == n * 2 or balance < 0 or balance > n:
        if balance == 0:
            result.append(''.join(cur))
        return

    for p in parentheses:
        new_balance = balance + parentheses[p]
        cur.append(p)
        recursive_parentheses(result, parentheses, cur, n, new_balance, ind + 1)
        cur.pop()


def generate_valid_parentheses(n):
    result, cur = [], []
    parentheses = {'(': 1, ')': -1}
    recursive_parentheses(result, parentheses, cur, n)
    return result


def main():
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " + str(generate_valid_parentheses(3)))


main()
