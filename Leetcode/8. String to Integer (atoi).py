class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        #First, convert the string to an array to make it easier to work with
        boolValues = []
        atLeastOneDigit = False
        for i in range(len(s)):
            if s[i].isdigit():
                boolValues.append(True)
            if not s[i].isdigit():
                boolValues.append(False)
        #print(boolValues)
        for i in range(len(boolValues)):
            if boolValues[i] == True:
                atLeastOneDigit = True
                break
        #print(atLeastOneDigit)
        if not atLeastOneDigit:
            return 0
        arr = []
        for i in range(len(s)):
            arr.append(s[i])
        
        #Next, remove the whitespace from the array
        def removeSpace(temp):
            while temp[0] == ' ':
                temp.pop(0)
            return temp
        arr = removeSpace(arr)

        #Now, check to see if the leading is a '-' and update negative operater based that
        isNegative = False
        if not (arr[0].isdigit()) and not (arr[1].isdigit()):
            return 0
        if arr[0] == '-':
            isNegative = True
            arr.pop(0)
        if arr[0] == '+':
            arr.pop(0)
        #print(arr)

        #Now, check to see that the first entry is a number
        firstIsDigit = False
        if arr[0].isdigit():
            firstIsDigit = True
        if not firstIsDigit:
            return 0
        #print(firstIsDigit)

        #Now, shorten the array to be only the first leading numbers
        newArr = []
        for i in range(len(arr)):
            if arr[i].isdigit():
                newArr.append(arr[i])
            if not arr[i].isdigit():
                break
        #print(newArr)

        #Taking care of a couple of special cases
        if len(newArr) == 1:
            if isNegative:
                return int(newArr[0]) * -1
            return int(newArr[0])
        zeroCount = 0
        for i in range(len(newArr)):
            if newArr[i] == '0':
                zeroCount += 1
        if zeroCount == len(newArr):
            return 0
        
        #Now, we have to remove the leading zeroes in the array
        while newArr[0] == '0':
            newArr.pop(0)
        #print(newArr)

        #Now, convert the array to integer & return it after checking negativity and range
        finalInt = int("".join(map(str, newArr)))
        if isNegative:
            finalInt = finalInt * -1
        #print(finalInt)
        lowerBound = -2 ** 31
        upperBound = (2 ** 31) - 1
        #print(lowerBound)
        #print(upperBound)
        if finalInt > upperBound:
            finalInt = upperBound
        if finalInt < lowerBound:
            finalInt = lowerBound
        return finalInt
