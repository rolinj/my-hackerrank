class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maxDiff= 0
        diff = 0

        for num in range(len(self.__elements)):
            for each_num in range(len(self.__elements[num:]) - 1):
                diff = self.__elements[num] - self.__elements[each_num+1]
                maxDiff = max(maxDiff, abs(diff))
      
        self.maximumDifference = maxDiff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)