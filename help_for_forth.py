
def make_string_array(currentLine, fromStr, toStr):
    j = 0
    keyWords = []
    while j < len(currentLine) - 1:
        k = currentLine.find(fromStr)
        keyWords.append(currentLine[k + 8:currentLine.find(toStr, k) - 1])
        j += currentLine.find(toStr)
        currentLine = currentLine[j + 1:]
    return keyWords

def comparison_in_arrayes(new_array, array):
    iflag = False
    for k in range(len(array)):
        for j in range(len(new_array)):
            if array[k] == new_array[j]:
                iflag = True
    return iflag
