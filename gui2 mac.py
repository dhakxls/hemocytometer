from tkinter import *

app = Tk()
app.title('Hemocytometer Calculation')
app.iconbitmap(r'/Users/martinvo/OneDrive - Xavier University/Dr. Escorcia Research/Lab Program Codes/Hemocytometer/hemocytometer.ico')

def outputLabel():
    cellsInStock = Calculations.totalCellsInStock()
    amountUse = Calculations.amountToUse()
    dilutionUse = Calculations.checkDilutionToUse()
    myLabel = Label(app, text=cellsInStock + "\n" + amountUse + "\n" + dilutionUse)
    myLabel.pack()

labelText=StringVar()
labelText.set("Enter Cell Count")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.pack()

directory=IntVar(None)
cellNum3=Entry(app,textvariable=directory,width=50)
cellNum3.pack()

labelText=StringVar()
labelText.set("Serial Dilution used? Expand the factor number (10^2 = 100)")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.pack()

directory=IntVar(None)
dilutionFactor3=Entry(app,textvariable=directory,width=50)
dilutionFactor3.pack()

myButton = Button(app, text="Calculate", height=1, command=outputLabel)
myButton.pack()

#Calculations
class Calculations:

    # cellNum = cellNum3.get()
    # dilutionFactor = dilutionFactor3.get()
    # cellNum2 = int(cellNum)
    # dilutionFactor2 = int(dilutionFactor)


    def totalCellsInStock():

        cellNum = cellNum3.get()
        dilutionFactor = dilutionFactor3.get()
        cellNum2 = int(cellNum)
        dilutionFactor2 = int(dilutionFactor)
        
        totalCells = cellNum2 * dilutionFactor2 * 10
        totalCells2 = int(totalCells)
        return ('Total cells per uL in stock is: ' + (format(totalCells2, "5.2e")))


    def amountToUse():

        cellNum = cellNum3.get()
        dilutionFactor = dilutionFactor3.get()
        cellNum2 = int(cellNum)
        dilutionFactor2 = int(dilutionFactor)

        cells = float(500 / cellNum2)
        yes = float(100 - cells)
        return ('The amount of uL to use for the cells is: ' + format(round(cells, 1)) + '\nThe amount of uL to use for YES is: ' + format(round(yes, 1)))
    
    def checkDilutionToUse():

        cellNum = cellNum3.get()
        dilutionFactor = dilutionFactor3.get()
        cellNum2 = int(cellNum)
        dilutionFactor2 = int(dilutionFactor)

        totalCells = cellNum2 * dilutionFactor2 * 10
        totalCellsInStock2 = int(totalCells)
        

        if (9999999 > totalCellsInStock2 > 1000000):
            return ("Use 10^5 serial dilution")
        elif (999999 > totalCellsInStock2 > 100000):
            return ("Use 10^4 serial dilution")
        elif (99999 > totalCellsInStock2 > 10000):
            return ("Use 10^3 serial dilution")
        elif (9999 > totalCellsInStock2 > 1000):
            return ("Use 10^2 serial dilution")
        elif (999 > totalCellsInStock2 > 100):
            return ("Use 10^1 serial dilution")
        elif (99 > totalCellsInStock2 > 10):
            return ("Use stock solution")

app.mainloop()

