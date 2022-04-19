from wirelessNetwork import WirelessNetwork
class Application():
    def __init__(self):
        self._listOfSensors = []
        self._noOfNeighbours =0
        self._noSensors =0
        self._neighId = ""
        self._dist =0
        self._path =[]
    
    def createSensors(self,listOfSensors =[]):
        noOfSensors = input("Enter the number of sensors: ")
        self.setNoOfSensors(noOfSensors)
        for index in range(int(noOfSensors)):
            id = input("Enter the sensors id: ")
            self.setId(id)
            
            listOfSensors += [[id]]
            noOfNeighbours =input("Enter the number of neighbours: ")
            self.setNoOfNeighbours(noOfNeighbours)
            
            #This snippet creates number of neighbours with ids and distance from first Sensor id 
            for index in range(int(noOfNeighbours)):
                neighId = input(print("Enter the neighbour for Sensor ",id,": "))
                self.setNeighId(neighId)
                dist =input(print("Enter the distance to ",neighId,": "))
                listOfSensors += [[neighId,int(dist)]]
            oxlevel = input("Enter the Oxygen level in %: ")
            temp =input("Enter the temperature measurement: ")
            self.setTemprature(temp)
            print("_*__*__*__*__*__*__*__*__*__*_ ")        
            listOfSensors += [[oxlevel,temp]]
            self.setTemprature(temp)
            self.setListOfSensors(listOfSensors)
        print(listOfSensors)
            
    def setNoOfSensors(self,noOfSensors):
        self._noSensors = noOfSensors

    def getNoOfSensors(self):
        return self._noSensors    
    
    def setId(self,id):
        self._id =id

    def getId(self):
        return self._id    

    def setNoOfNeighbours(self,noOfNeighbours):
        self._noOfNeighbours = noOfNeighbours

    def getNoOfNeighbours(self):
        return self._noOfNeighbours  

    def setNeighId(self,neighId):
        self._neighId = neighId  

    def getNeighId(self):
        return self._neighId  

    def setOxLevel(self,oxlevel):
        self._oxygenlevel = oxlevel

    def getOxLevel(self):
        return self._oxygenlevel        
    
    def setTemprature(self,temp):
        self._temprature = temp

    def getTemprature(self):
        return self._temprature    

    def setListOfSensors(self,listOfSensors):
        self._listOfSensors = listOfSensors

    def getListOfSensors(self):
        return self._listOfSensors    
   
ob =Application()
ob.createSensors() 
