import os
def find_lowest(arr1, arr2):
    sorted_arr = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    distance = 0
    for i in range(len(sorted_arr)):
        distance += abs(sorted_arr[i] - sorted_arr2[i])


    return distance


def find_similarity(arr1, arr2):
    similarity = 0
    found = {}
    for x in arr1:
        if x not in found:
            count = 0
            for y in arr2:
                if (x == y):
                    count += 1
            found[x] = count
            print(x, count)
        similarity += found[x] * x

    return similarity


def main():
    f = open("day1/input.txt", "r")
    lines = f.readlines()
    arr1 = [None] * len(lines)
    arr2 = [None] * len(lines)
    for (i, line) in enumerate(lines):
        arr1[i] = int(line.split()[0])
        arr2[i] = int(line.split()[1])
    # print(find_lowest(arr1, arr2))
    print(find_similarity(arr1, arr2))


if __name__ == '__main__':
    main()