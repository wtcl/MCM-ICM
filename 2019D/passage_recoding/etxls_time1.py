import math
import xlwt

total = 8000
floorweight = [1, 3, 8, 12, 6]
floors = []
sum = 0
d = 0.5
e = 0.1
nf = 4
v = 1
aimstairs = []
aimadd = []

for f in floorweight:
    sum += f
scost = 10/v
print(scost)
book = xlwt.Workbook()
sheet = book.add_sheet('Result')

class stair:
    def __init__(self, name, fl, aim, aimfloor, num):
        self.name = name
        self.fl = fl
        self.aim = aim
        self.aimfloor = aimfloor
        self.num= math.floor(num)

    def run(self, time):
        if time == self.cleartime() and self.aimfloor != -1:
            ss = floors[self.aimfloor].findstair(self.aim)
            aimstairs.append(ss)
            aimadd.append(self.num)
        self.num = math.floor(self.num - (time * nf * v) / (d + e))
        if self.num < 0:
            self.num = 0

    def cleartime(self):

        if (self.num * d + self.num * e) / nf >= 0:
            return (self.num * d + self.num * e) / (nf * v)
        else:
            return 0

class floor:
    def __init__(self, fl, sname, saim, saimfloor, sweight):
        self.name = fl
        self.num = total / sum * floorweight[fl]
        self.stairs = []
        n = 0
        for t in sweight:
            n = n + t
        for i in range(sname.__len__()):
            self.stairs.append(stair(sname[i], fl, saim[i], saimfloor[i],
                                     self.num * sweight[i] / n))

    def findstair(self, name):
        for s in self.stairs:
            if s.name == name:
                return s
        return None

    def min(self):
        result = None
        time = 1000000
        for s in self.stairs:
            if s.cleartime() > 0 and s.cleartime() < time:
                result = s
                time = s.cleartime()
        return result

    def run(self, time):
        for s in self.stairs:
            s.run(time)

if __name__ == '__main__':
    sn0 = ['E']
    sw0 = [1]
    sa0 = ['esc']
    saf0 = [-1]
    f = floor(0, sn0, sa0, saf0, sw0)
    floors.append(f)
    sn1 = ['A1', 'A2', 'A3']
    sw1 = [3, 4, 3]
    sa1 = ['E', 'E', 'E']
    saf1 = [0, 0, 0]
    f = floor(1, sn1, sa1, saf1, sw1)
    floors.append(f)
    sn2 = ['B1', 'B2', 'B', 'B3']
    sw2 = [2,2,2,2]
    sa2 = ['A1','A1','A1','A3']
    saf2 = [1,1,1,1]
    f = floor(2, sn2, sa2, saf2, sw2)
    floors.append(f)
    sn3 = ['E1','E2','E3','B']
    sw3 = [3,1,3,3]
    sa3 = ['B1','B','B2','B']
    saf3 = [2,2,2,2]
    f = floor(3, sn3, sa3, saf3, sw3)
    floors.append(f)
    sn4 = ['E1','B','B4']
    sw4 = [4,4,2]
    sa4 = ['E1','B','F']
    saf4 = [3,3,3]
    f = floor(4, sn4, sa4, saf4, sw4)
    floors.append(f)
    totaltime = 0
    col = 0
    while True:
        aimstairs.clear()
        aimadd.clear()
        time = 1000000
        s = None
        row = 0
        sheet.write(col, row, 'total')
        sheet.write(col + 1, row, totaltime)
        for i in range(5):
            stas = floors[i].stairs
            for sta in stas:
                row += 1
                str = sta.name + ' ' + sta.fl.__str__()
                num = sta.cleartime()
                if num < 0:
                    num = 0
                sheet.write(col, row, str)
                sheet.write(col + 1, row, num)
        for i in range(5):
            ss = floors[i].min()
            if ss is not None and 0 < ss.cleartime() < time:
                time = ss.cleartime()
                s = ss
        if s is None:
            break
        totaltime = totaltime + time + scost
        for i in range(5):
            floors[i].run(time)
        for i in range(aimstairs.__len__()):
            try:
                aimstairs[i].num = aimstairs[i].num + aimadd[i]
                print(aimstairs[i].name)
            except Exception as e:
                print(e)
        col += 2
    print(totaltime)
book.save('.//result_Five.xls')

