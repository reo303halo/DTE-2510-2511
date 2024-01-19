
def findMax(lst):
    return findMaxHelper(lst, 0, lst[0])


def findMaxHelper(lst, index, currentMax):
    if index == len(lst): # Base case
        return currentMax
    else:
        if lst[index] > currentMax:
            currentMax = lst[index]
        return findMaxHelper(lst, index + 1, currentMax)


def main():
    lst = [1, 2, 3, 4, 5]
    print(f'Max of {lst} is {findMax(lst)}')

    lst = [5, 4, 3, 2, 1]
    print(f'Max of {lst} is {findMax(lst)}')

    lst = [3, 6, 1, 7, 4, 3]
    print(f'Max of {lst} is {findMax(lst)}')

    lst = [-7, -3, -2, -8]
    print(f'Max of {lst} is {findMax(lst)}')

if __name__ == "__main__":
    main()
