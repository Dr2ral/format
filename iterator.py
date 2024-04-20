class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            res = self.start
            self.start += 2
            return res
        raise StopIteration

res = EvenNumbers(10, 25)
print(res)
for i in res:
    print(i)

#class EvenNumbers:
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end
#        self.i = 0
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.start < self.end:
#           for i in range(self.start, self.end, 2):
#              print(i)
#        if self.start == self.end:
#           return
#        raise StopIteration
#
#res = EvenNumbers(10, 25)
#print(res)
#for i in res:
#    print(i)
