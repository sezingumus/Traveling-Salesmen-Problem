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
        self.neighbors = []
 
    def setIsVisit(self,visited):
        self.visited = visited         
    
    def addNeighbors(self,ID,distance):
        self.neighbors.append([ID,distance])
    def getNeighbors(self):
        return self.neighbors
    
def fileToList(input_file):
    file = open(input_file,"r")
    list_of_cities = []
    line = file.readline()
    while line:
        _id,x,y = line.split()
        list_of_cities.append(City(_id,int(x),int(y)))
        line = file.readline()
    file.close()
    boundNeighborsToACity(list_of_cities)
    #return list_of_cities
    
def calculateDistance(x1,x2,y1,y2):
        x = (x1-x2) * (x1-x2)
        y = (y1-y2) * (y1-y2) 
        d = math.sqrt(x+y) 
        d = round(d)
        return d

def boundNeighborsToACity(list_of_cities):
 length = len(list_of_cities)     
 for i in range(0,length):
     for j in range(0,length):
        distance = calculateDistance(list_of_cities[j].x_coordinate, list_of_cities[i].x_coordinate ,list_of_cities[j].y_coordinate, list_of_cities[i].y_coordinate)
        if distance != 0:
            list_of_cities[i].addNeighbors(list_of_cities[j].ID,distance)


def nearestNeighbor (list_of_cities):
   for i in range(len(list_of_cities)):
     if city_list[i].ID == 'a':
         print(min(list_of_cities[i].getNeighbors(), key=lambda x: x[1]))         

    

def listtoFile(output_file):
 file = open(output_file,"w")
 for i in range(5):
        file.write("exp \n")
 file.close()
    

fileToList("test1.txt")
#boundNeighborsToACity(cities)



#fileToList(sys.argv[1]) 

    
   
