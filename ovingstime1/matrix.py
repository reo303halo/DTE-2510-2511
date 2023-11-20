
def sumLastIndex(nestedList):
    result = 0
 
    for row in nestedList:
        result += row[-1]

    return result


def firstAndLastList(nestedList):

    result = nestedList[0][0] + nestedList[-1][-1]

    return result



def main():

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = sumLastIndex(matrix)

    print("Result1 :", result1, "\n")


    result2 = firstAndLastList(matrix)

    print("Result2 :", result2)


if __name__ == "__main__":
    main()