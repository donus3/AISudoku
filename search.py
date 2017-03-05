from table import Table
from tree import Tree

class Search:
    
    def __init__(self, filePath='easy'):
        self.table = Table(filePath+'.csv')
        self.tableGlobal = None
        #self.table.checkConstein()

    def getblanknodes(self):
        temp = []
        irow = 0
        for row in self.table.table:
            icol = 0
            for col in row:
                if self.table.table[irow][icol] == 0: #enter when blank
                    temp.append([irow, icol])
                icol += 1
            irow += 1
        return temp

    def traverse(self, blank_list, parent, table_tmp):
        if not len(blank_list):
            return table_tmp
        irow, icol, igroup = blank_list[0][0], blank_list[0][1], int(blank_list[0][0] / 3) * 3 + int(blank_list[0][1] / 3)
        val_set = self.table.checkall(irow, icol, igroup) #get set of posible value
        if not len(val_set):
            #print("Return!! irow: ", irow, " icol: ", icol)
            return None
        for val in val_set: #loop to add node
            parent.next.append(Tree(val))
        inode = 0
        for val in val_set:
            table_tmp.add(irow, icol, val)
            '''print("irow", irow, " icol:", icol, val_set, " add:",val)
            for row in table_tmp.table:
                print(row)
            print("------------") 
            i = input("continue")'''
            temp = self.traverse(blank_list[1:], parent.next[inode], table_tmp)
            if not temp:
                table_tmp.delete(irow, icol)
            else:
                return temp
            inode += 1

if __name__ == "__main__":
    filename = input("Enter suduku filepath: ")
    s = Search(filename)
    root = Tree()
    blank_list = s.getblanknodes()
    print("Pls wait a little. Be claim man.")
    result = s.traverse(blank_list, root, s.table).table
    for row in result:
        print(row)