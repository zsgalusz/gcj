# https://code.google.com/codejam/contest/544101/dashboard#s=p1
import sys

def calculateDeletes(memo, i, D):
    for j in range(256):
        deletecost = memo[i][j] + D
        if memo[i + 1][j] > deletecost:
            memo[i + 1][j] = deletecost

def calculateChanges(memo, i, M, a):
    for j in range(256):
        for k in range(256):
            if abs(j - k) <= M:
                changecost = memo[i][j] + abs(a[i] - k)
                if memo[i + 1][k] > changecost:
                    memo[i + 1][k] = changecost  

def calculateInserts(memo, i, I, M):
    if M != 0:
        for j in range(256):
            for k in range(256):
                insertcount = (abs(j - k) + M - 1) // M
                insertcost = memo[i + 1][k] + I * insertcount
                if memo[i + 1][j] > insertcost:
                    memo[i + 1][j] = insertcost

def calculatecost(D, I, M, N, a):
    memo = [[]] * (N+1)

    for x in range(N+1):
        if x == 0:
            memo[x] = [0] * 256
        else:
            memo[x] = [sys.maxint] * 256

    for i in range(N):
        calculateDeletes(memo, i, D)
        calculateChanges(memo, i, M, a)
        calculateInserts(memo, i, I, M)
    
    res = min(memo[N])
    return res

def main(infileName, outfileName):
    with open(infileName) as infile:
        with open(outfileName, "w") as outfile:
            T = int(infile.readline())
            for case in range(T):
                outfile.write("Case #" + str(case+1) + ": ")

                line = infile.readline().split()
                D, I, M, N = int(line[0]), int(line[1]), int(line[2]), int(line[3])

                line = infile.readline().split()
                a = [int(x) for x in line]

                outfile.write(str(calculatecost(D, I, M, N, a)) + '\n')



if __name__ == "__main__":
    infileName = "Z:\\gcj\\2010-1A\\B\\B-large-practice.in"
    outfileName = "Z:\\gcj\\2010-1A\\B\\B-large-practice.out"
    main(infileName, outfileName)