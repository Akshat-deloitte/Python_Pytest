from itertools import combinations


class StringClass:

    def __init__(self):
        self.str = "12314532"
        self.str2 = "45211834"


    def getLength(self):
        length = len(self.str)
        print(length)


    def StrToList(self , str1):
        final_list = list(str1)
        print(final_list)


class PairsPossible(StringClass):
    def listOfPairs(self):
        res = list(combinations(self.str2, 2))
        print(res)



class SearchCommonElements(StringClass):
    arr = []

    def commonEle(self):
        dict = {}
        for char in self.str:
            if char in dict:
                continue
            else:
                dict[char] = 1
        for char in self.str2:
            if char in dict:
                self.arr.append(char)

        for key, val in dict.items():
            print(key + " ")






class EqualSumPairs(SearchCommonElements):

    def printList(self):
        print("third")
        print(self.arr)








obj = StringClass()
obj.getLength()
obj.StrToList()


obj1 = PairsPossible()
obj1.listOfPairs()

obj2 = SearchCommonElements()
obj2.commonEle()


obj3 = EqualSumPairs()
obj3.printList()