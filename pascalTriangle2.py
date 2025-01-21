def getRow(rowIndex: int) -> list[int]:
    data = []
    for i in range(1, rowIndex + 2):
        if i == 1:
            data.append([1])
        elif i == 2:
            data.append([1, 1])
        else:
            info = [1]
            for i in range(len(data[-1]) - 1):
                info.append(sum(data[-1][i: i+2]))
            info.append(1)
            data.append(info)
    return data[rowIndex]



if __name__ == '__main__':
    row_index=3
    result = getRow(row_index)
    print(result)