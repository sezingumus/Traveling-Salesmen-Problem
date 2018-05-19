"""
Sezin Gümüş     150113841
Ufuk  Çetinkaya 150113824
"""
import math
import sys
class City(object):     
    def __init__(self , ID,x_coordinate,y_coordinate):
        self.ID = ID
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.visited = False
        self.neighbor = []
 
    def setIsVisit(self,visited):
        self.visited = visited         
    
    def addNeighbors(self,ID,distance):
        self.neighbor.append([ID,distance])
    def getNeighbors(self):
        return self.neighbor
    
def fileToList(input_file):
    file = open(input_file,"r")
    list_of_cities = []
    line = file.readline()
    while line:
        _id,x,y = line.split()
        list_of_cities.append(City(_id,int(x),int(y)))
        line = file.readline()
    file.close()
    return list_of_cities
    
def calculateDistance(x1,x2,y1,y2):
        x = (x1-x2) * (x1-x2)
        y = (y1-y2) * (y1-y2) 
        d = math.sqrt(x+y) 
        d = round(d)
        return d


def listToAdjacencyMatrix(city_list):
 length = len(city_list)    
 adjmatrix = [[0]*length for i in range(length)] 
 neighbor = []
 for i in range(0,length):
     for j in range(0,length):
        distance = calculateDistance(city_list[j].x_coordinate, city_list[i].x_coordinate , city_list[j].y_coordinate, city_list[i].y_coordinate)
        adjmatrix[i][j] = distance
        if distance != 0:
            city_list[i].addNeighbors(city_list[j].ID,distance)

 for i in range(len(city_list)):
     if city_list[i].ID == 'a':
         #print(city_list[i].x_coordinate,city_list[i].y_coordinate,city_list[i].visited)
         print(min(city_list[i].getNeighbors()))
         
 return adjmatrix

def findNearestNeighbor (city):
  pass
    

def listtoFile(output_file):
 file = open(output_file,"w")
 for i in range(5):
        file.write("exp \n")
 file.close()
    
cities = fileToList("test1.txt")
adj_matrix = listToAdjacencyMatrix(cities)


#adj = listtoAdjacencyMatrix("test1.txt")#listtoAdjacencyMatrix(sys.argv[1]) 

    
   
