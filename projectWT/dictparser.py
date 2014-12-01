#!/usr/bin/env python
from pythonds.graphs import PriorityQueue, Vertex, Graph

def main():
     #file opening
     fo = open("words", "r")
     print ("Name of file: ", fo.name)
     print ("Closed or not: ", fo.closed)
     print ("Opening mode: ", fo.mode)
     print ("Softspace flag: ", fo.softspace)
     print
     #file parsing
     threeword = list()
     fourword = list()
     fiveword = list()
     
     for line in fo.readlines():
          x = line.strip()
          t = x.lower()
          y = t+'\n'
          if len(t) == 3 and t.isalnum() and y not in threeword:
               threeword.append(y)
          if len(t) == 4 and t.isalnum() and y not in fourword:
               fourword.append(y)
          if len(t) == 5 and t.isalnum() and y not in fiveword:
               fiveword.append(y)

     
     fo.close()
     
     f3 = open("words3", "wb")

     print ("Name of file: ", f3.name)
     print ("Closed or not: ", f3.closed)
     print ("Opening mode: ", f3.mode)
     print ("Softspace flag: ", f3.softspace)
     print

     for i in threeword:
          f3.write(i);
     f3.close()

     f4 = open("words4", "wb")

     
     print ("Name of file: ", f4.name)
     print ("Closed or not: ", f4.closed)
     print ("Opening mode: ", f4.mode)
     print ("Softspace flag: ", f4.softspace)
     print
          
     for i in fourword:
          f4.write(i);
     f4.close()

     f5 = open("words5", "wb")
     
     print ("Name of file: ", f5.name)
     print ("Closed or not: ", f5.closed)
     print ("Opening mode: ", f5.mode)
     print ("Softspace flag: ", f5.softspace)
     print
          
     for i in fiveword:
          f5.write(i);
     f5.close()

     
     
#     v = Vertex("String")
#     g = Graph()
#     g.addVertex(v)
#     s = str(v);
#     print(s),
     

     return 0


if __name__ == "__main__":
     main()
