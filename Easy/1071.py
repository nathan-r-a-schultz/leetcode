# leetcode 1071: greatest common divisor of strings
# easy
# math, string
# completed jan 8, 2026

def gcdOfStrings(str1, str2):

    # selecting the shorter string to grab prefixes from
    workingStr = str2 if len(str2) < len(str1) else str1
    returnStr = ""

    for i in range(1, len(workingStr) + 1):

        # grab a prefix from the shorter string
        tempStr = workingStr[0:i]

        # verify the prefix can be used to construct both str1 and str2
        str1MultiplyFactor = len(str1) / len(tempStr)
        str2MultiplyFactor = len(str2) / len(tempStr)
    
        #if type(str1MultiplyFactor) == 'float' or type(str2MultiplyFactor) == 'float': # this if statement isn't needed when running locally but required for running on leetcode
        if str1MultiplyFactor.is_integer() == False or str2MultiplyFactor.is_integer() == False: 
            continue
        else:
            str1MultiplyFactor = int(str1MultiplyFactor)
            str2MultiplyFactor = int(str2MultiplyFactor)

        # construct new strings from the prefix and see if they match with str1 and str2
        if tempStr * str1MultiplyFactor == str1 and tempStr * str2MultiplyFactor == str2: returnStr = tempStr

    return returnStr

def optimizedSolution():

def main():
    str1 = "ABCABC"
    str2 = "ABC"

    print(gcdOfStrings(str1, str2))

main()