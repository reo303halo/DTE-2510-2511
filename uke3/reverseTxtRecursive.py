
def reverseLines(inputFile, outputFile):
    with open(inputFile, "r") as inFile, open(outputFile, "w") as outFile:
        reverseLinesHelper(inFile, outFile, inFile.readline())


def reverseLinesHelper(inFile, outFile, line):
    nextLine = inFile.readline()
    if nextLine: # Base case
        reverseLinesHelper(inFile, outFile, nextLine)

    outFile.write(line) # Write the line after the recursive call


def main():
    reverseLines("input.txt", "output.txt")
    print("Lines reversed successfully!")


if __name__ == "__main__":
    main()
