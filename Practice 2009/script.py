# https://code.google.com/codejam/contest/32003/dashboard

def ConvertToDecimal(number, language):
    raw = 0
    base = len(language)

    for digit in number:
        raw *= base
        raw += language.index(digit)

    return raw

def ConvertFromDecimal(number, language):
    text = ""
    n = number
    base = len(language)

    while n >= base:
        text = language[n % base] + text
        n = n // base
    else:
        text = language[n] + text

    return text

def runTest(infileName, outfileName):
    with open(infileName) as infile:
        with open(outfileName, "w") as outfile:
            N = int(infile.readline())
            for case in range(N):
                words = infile.readline().split()
                result = ConvertFromDecimal(ConvertToDecimal(words[0], words[1]), words[2])
                outfile.write("Case #" + str(case+1) + ": " + result + "\n")

if __name__ == "__main__":
    infileName = "D:\Temp\gcj\A-large-practice.in"
    outfileName = "D:\Temp\gcj\A-large-practice.out"
    runTest(infileName, outfileName)
