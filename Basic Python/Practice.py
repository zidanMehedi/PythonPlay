class Test:
    myList = [] 
    def __init__(self, item1):
        self.myList.append(item1)

l = Test('ice-cream')
m = Test('biriyani')
n = Test('burger')
print (n.myList)
