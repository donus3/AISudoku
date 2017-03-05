import numpy
import csv

class Table:

    def __init__(self, filepath):
        self.table = []
        self.createTable(filepath)

    def createTable(self, filepath):
        with open(filepath, newline='') as csvfile:
            suReader = csv.reader(csvfile)
            for row in suReader:
                self.table.append(list(map(int, row)))
    
    def add(self, i, j, number):
        self.table[i][j] = number
        return self.table

    def delete(self, i, j):
        self.table[i][j] = 0
        return self.table

    def genTransposeList(self):
        return numpy.transpose(self.table).tolist()

    def genThreeCrossThree(self):
        temp1 = numpy.array(self.table).reshape(9, 3, 3)
        temp2 = []
        s, e = 0, 3
        while s <= 6:
            for i in range(3):
                for j in range(s, e):
                    temp2.append(temp1[j][i])
                if i >= 2:
                    s += 3
                    e += 3
        return numpy.reshape(temp2,(9,9)).tolist()

    def checkThreeCrossThree(self):
        self.table = self.genThreeCrossThree() # transform to 3 x 3 pieces
        isNotAdd = self.checkToFill()
        self.table = self.genThreeCrossThree() # transform back to original
        if isNotAdd:
            return 1
        return 0

    def checkrow(self, row_num):
        return {1,2,3,4,5,6,7,8,9} - set(self.table[row_num])

    def checkcol(self, col_num):
        self.table = self.genTransposeList()
        temp = {1,2,3,4,5,6,7,8,9} - set(self.table[col_num])
        self.table = self.genTransposeList()
        return temp        
    
    def check3x3(self, group_num):
        temp = self.genThreeCrossThree()
        return {1,2,3,4,5,6,7,8,9} - set(temp[group_num])

    def checkall(self, row_num, col_num, group_num):
        return self.checkrow(row_num) & self.checkcol(col_num) & self.check3x3(group_num)

    def checkConstein(self):
        flagcheck = 1
        while flagcheck:
            flagcheck = 0
            irow = 0
            for row in self.table:
                icol = 0
                for col in row:
                    if self.table[irow][icol] == 0:
                        val_set = self.checkall(irow, icol, int(irow/3)*3+int(icol/3))
                        #print("row:", irow, " col:", icol, " posible value set:", val_set)
                        if len(val_set) < 2 and len(val_set) > 0:
                            val = val_set.pop()
                            self.add(irow, icol, val)
                            #print("place value:", val)
                            flagcheck = 1
                    icol += 1
                irow +=1

if __name__ == "__main__":
    t = Table('hard1.csv')
    t.checkConstein()
    for row in t.table:
        print(row)
