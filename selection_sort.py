def selection_sort(elements):
    pos = 0

    for i in range(len(elements)):
        min_ele = 8089776
        for j in range(i, len(elements)):
            if elements[j] < min:
                min_ele = elements[j]
                pos = j

        elements[i], elements[pos] = elements[pos], elements[i]

    return elements


if __name__ == '__main__':
    print(selection_sort([1, 2, 3, 2, 1, 5, 6]))
