
cellNum = input("Enter number of cells: ")
dilutionFactor = input("Enter dilution factor (ex. 10^2 = 100): ")
cellNum2 = int(cellNum)
dilutionFactor2 = int(dilutionFactor)


def totalCellsInStock():
    totalCells = cellNum2 * dilutionFactor2 * 10
    totalCells2 = int(totalCells)
    return (format(totalCells2, "5.2e"))

# second function for the checkDilutionFunction
def totalCellsInStock2():
    totalCells = cellNum2 * dilutionFactor2 * 10
    totalCells2 = int(totalCells)
    return totalCells2

def amountToUse():
    cells = float(500 / cellNum2)
    yes = float(100 - cells)
    return ('The amount of uL to use for the cells is: ', round(cells, 1), 'The amount of uL to use for YES is: ', round(yes, 1))
    
def checkDilutionToUse():
    if (9999999 > totalCellsInStock2() > 1000000):
        return ("Use 10^5 serial dilution")
    elif (999999 > totalCellsInStock2() > 100000):
        return ("Use 10^4 serial dilution")
    elif (99999 > totalCellsInStock2() > 10000):
        return ("Use 10^3 serial dilution")
    elif (9999 > totalCellsInStock2() > 1000):
        return ("Use 10^2 serial dilution")
    elif (999 > totalCellsInStock2() > 100):
        return ("Use 10^1 serial dilution")
    elif (99 > totalCellsInStock2() > 10):
        return ("Use stock solution")


# print(cellNum)
# print(format(dilutionFactor2, "5.2e"))
print("The number of cells in the stock solution is: ", totalCellsInStock())
print(amountToUse())
print(checkDilutionToUse())



    