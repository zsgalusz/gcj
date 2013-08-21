# https://code.google.com/codejam/contest/544101/dashboard

class table:
    def __init__(self, N, K):
        self.size = N
        self.rcond = 'R' * K
        self.bcond = 'B' * K
        self.rwin = False
        self.bwin = False
        self.content = [["."] * N for x in range(N)]

    def addLine(self, line, i):
        j = 0

        for c in reversed(line):
            if c == 'B' or c == 'R':
                self.content[j][i] = c
                j += 1

    def checkWin(self, line):
        if self.rcond in line:
            self.rwin = True
        if self.bcond in line:                       
            self.bwin = True

    def finish(self):       
        for i in range(self.size):            
            # check columns
            self.checkWin(''.join(self.content[i]))

            # check rows
            row = ''.join([v for x in self.content for ix,v in enumerate(x) if ix == i])
            self.checkWin(row)

            # check diagonals
            self.checkWin(self.walkUpRight(0,i))
            self.checkWin(self.walkDownRight(0,i))

            if i > 0:
                self.checkWin(self.walkUpRight(i, self.size-1))
                self.checkWin(self.walkDownRight(i, 0))

    def win2text(self):
        if not self.rwin and not self.bwin:
            return "Neither"
        elif self.rwin and self.bwin:
            return "Both"
        elif self.rwin:
            return "Red"
        else:
            return "Blue"

    def walkUpRight(self, startx, starty):
        x, y = startx, starty
        text = ""

        while(x < self.size and y >= 0):
            text += self.content[x][y]
            x += 1
            y -= 1

        return text

    def walkDownRight(self, startx, starty):
        x, y = startx, starty
        text = ""

        while(x < self.size and y < self.size):
            text += self.content[x][y]
            x += 1
            y += 1
            
        return text

def main(infileName, outfileName):
    with open(infileName) as infile:
        with open(outfileName, "w") as outfile:
            T = int(infile.readline())
            for case in range(T):
                outfile.write("Case #" + str(case+1) + ": ")

                l = infile.readline().split()
                N, K = int(l[0]), int(l[1])
                t = table(N,K)

                for i in range(N):
                    l = infile.readline()
                    t.addLine(l, i)

                t.finish()
                outfile.write(t.win2text() + '\n')



if __name__ == "__main__":
    infileName = "D:\\Temp\\gcj\\2010-1A\\A\\A-large-practice.in"
    outfileName = "D:\\Temp\\gcj\\2010-1A\\A\\A-large-practice.out"
    main(infileName, outfileName)