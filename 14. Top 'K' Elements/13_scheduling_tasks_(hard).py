from collections import Counter


def schedule_tasks(tasks, n):
    counter = Counter(tasks)
    max_freq = max(counter.values())
    max_freq_count = Counter(counter.values())[max_freq]
    return max(len(tasks), (n + 1) * (max_freq - 1) + max_freq_count)


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
