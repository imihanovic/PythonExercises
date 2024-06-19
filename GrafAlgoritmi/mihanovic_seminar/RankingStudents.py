# -*- coding: utf-8 -*-
import itertools
possible = []
class RankingStudents:
    def __init__(self, n, f, a, b):
        self.n = n
        self.f = f
        self.a = a
        self.b = b
        
    def checkElements(self, lst):
        for i in range(len(lst)):
            if(lst[i]<0 or lst[i]>(self.n-1)):
                return True
        return False    

    def checkConstraints(self):
        if(self.n<1 or self.n>1000):
            return False
        if(len(self.f) != self.n):
            return False
        if graph.checkElements(self.f) or graph.checkElements(self.a) or graph.checkElements(self.b):
            return False
        if(len(self.a) < 0 or len(self.a) > 1000):
            return False
        if(len(self.b)!=len(self.a)):
            return False
        return True
    
    def checkPermutation(self, p):
        global possible
        
        for i in range(len(p)):
            indeks = p.index(i)
            if(self.f[i] < indeks):
                return False

        for i in range(len(self.a)):
            if(p.index(self.a[i])>p.index(self.b[i])):
                return False
            
        possible.append(p)
        return True
                
    def getPermutations(self):
        return list(itertools.permutations([*range(self.n)] ))
    
    def rankingPossible(n, f, a, b):
        global graph
        graph = RankingStudents(n, f, a, b)
        if not graph.checkConstraints():
            return "Constraints are not valid!"
        permutations = list(set(graph.getPermutations()))
        print(permutations)
        for p in permutations:
            graph.checkPermutation(list(p))
        if(len(possible)>0):
            print("Valid orders: ", end = "")
            for i in range(len(possible)):
                for j in (possible[i]):
                    print(j,end="")
                if(i!=len(possible)-1):
                    print(",",end="")
            print()
            return "Possible"
        return "Impossible"
    
def main():
    # n = 4
    # f = [1, 1, 1, 3]
    # a = [1]
    # b = [3]

    # n = 6
    # f = [5, 5, 5, 1, 5, 4]
    # a = [0, 2, 4]
    # b = [1, 3, 5]
    
    n = 3
    f = [0, 1, 2]
    a = [0, 1]
    b = [2, 2]
    
    # n = 3
    # f = [2, 2, 2]
    # a = [0, 1, 2]
    # b = [1, 2, 0]
    
    pos = RankingStudents.rankingPossible(n,f,a,b)
    print(pos)
    
if __name__ == '__main__':
    main()




