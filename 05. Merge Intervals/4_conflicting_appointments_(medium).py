def can_attend_all_appointments(intervals):
    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
