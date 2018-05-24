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
        self.neighbors = []
 
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
    for i in range(len(list_of_cities)):
        print ("cities:",list_of_cities[i].ID)
    return boundNeighborsToACity(list_of_cities)

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
            print (list_of_cities[i].ID,"n[0]",list_of_cities[i].getNeighbors()[0])
 return list_of_cities
 
def nearestNeighbor (list_of_cities):
   path = []
   min_edge = 0
   total_cost = 0
   current_city = list_of_cities[0]
   path.append([current_city.ID,min_edge])
   next_city_id , min_edge = min(current_city.getNeighbors(),key=lambda x: x[1])
   next_city_index  = findCity(next_city_id,list_of_cities)
   next_city = list_of_cities[next_city_index]
   total_cost += min_edge 
   print(current_city.ID,"-->",next_city.ID)
   prev_city = current_city
   removeNeighbor(prev_city.ID,list_of_cities)
   current_city = next_city
   
   while (current_city.getNeighbors()):
       
       path.append([current_city.ID,min_edge])
       next_city_id , min_edge = min(current_city.getNeighbors(),key=lambda x: x[1])
       next_city_index  = findCity(next_city_id,list_of_cities)
       next_city = list_of_cities[next_city_index]
       print(current_city.ID,"-->",next_city.ID)
       prev_city = current_city
       removeNeighbor(prev_city.ID,list_of_cities)
       total_cost += min_edge
       current_city = next_city
       
   path.append([next_city.ID,min_edge])
   index = findCity(next_city.ID,list_of_cities)
   last_city = list_of_cities[index]
   last_edge = calculateDistance(list_of_cities[0].x_coordinate,last_city.x_coordinate,list_of_cities[0].y_coordinate,last_city.y_coordinate)
   total_cost += last_edge 
   return total_cost , path
               
def findCity (c,city_list):
    for i in range(len(city_list)):
        if city_list[i].ID == c:
            return i
    return -1
def findNeighbor(n, neighbor):
    for i in range(len(neighbor)):
        n_id , dist = neighbor[i]
        if n_id == n :
          return i
    return -1
def removeNeighbor(n,list_of_cities):
    for i in range(len(list_of_cities)):
        neighbor = list_of_cities[i].getNeighbors()
        j = findNeighbor(n,neighbor)
        del neighbor[j]
   
def listtoFile(output_file,cost,path):
 file = open(output_file,"w")
 file.write(str(cost))
 file.write("\n")
 file.writelines(["%s\n" % item[0] for item in path ])
 file.close()
    

cities = fileToList("test-input-3.txt")#fileToList(sys.argv[1])
total_cost,path = nearestNeighbor(cities)
print("Total cost :",total_cost)
listtoFile("output3.txt",total_cost,path)#(sys.argv[2],total_cost,path)

#fileToList(sys.argv[1]) 

    
   
