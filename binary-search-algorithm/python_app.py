def binary_search(lists, element):
    middle = 0
    start = 0
    end = len(lists)
    steps = 0

    while (start <= end):
        print("Step", steps, ":", str(lists[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == lists[middle]:
            return middle
        elif element < lists[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return - 1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9

binary_search(my_list, target)
