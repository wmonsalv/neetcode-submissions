class Solution:
    def hammingWeight(self, n: int) -> int:
        newNum = format(n, "b")
        counter = 0
        for e in newNum:
            print(e)
            if e == "1":
                counter += 1
        return counter