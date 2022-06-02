def convert_string(s):
    s_list = []
    s_b = 0

    for i in range(len(s)):
        elem = s[len(s) - i - 1]
        if elem != '#' and s_b == 0:
            s_list.append(elem)
        elif elem != '#' and s_b > 0:
            s_b -= 1
        else:
            s_b += 1

    return s_list


def backspace_compare(s, t):
    s_conv = convert_string(s)
    t_conv = convert_string(t)

    return s_conv[::-1] == t_conv[::-1]


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
