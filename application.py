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
        #The loop checks if noOfSensors is int or not
        while(noOfSensors.isnumeric() == False):
            print("This is an invalid entry for the number of sensors!")
            noOfSensors =input("Re - enter the number of sensors: ")  
        for index in range(int(noOfSensors)):
            id = input("Enter the sensors id: ")
            self.setId(id)
            while(id.isnumeric() == True):
                print("This is an invalid entry for sensor Id! ")
                print("_*__*__*__*__*__*__*__*__*__*_ ")
                id = input(print("Enter the Sensor Id: "))
                self.setId(id)
                
            #This is when id =A!
            while(('!' in id) == True):    
                print("This is an invalid entry for sensor Id! ")
                print("_*__*__*__*__*__*__*__*__*__*_ ")         
                id = input(print("Enter the Sensor Id: "))
            listOfSensors += [[id]]
            noOfNeighbours =input("Enter the number of neighbours: ")
            self.setNoOfNeighbours(noOfNeighbours)
            while(noOfNeighbours.isnumeric() == False):
                try:
                    nNeigh = None
                    nNeigh =int(noOfNeighbours)
                    
                except Exception:
                    print("This is an invalid entry for the number of neighbours! ")  
                    noOfNeighbours =input("Enter the number of Neighbours: ")  
                    self.setNoOfNeighbours(noOfNeighbours)
            
            #This snippet creates number of neighbours with ids and distance from first Sensor id 
            if(noOfNeighbours !=0):
                for index in range(int(noOfNeighbours)):
                    neighId = input(print("Enter the neighbour for Sensor ",id,": "))
                    self.setNeighId(neighId)
                    while(neighId.isnumeric() ==True):
                        print("This is an invalid entry for the neighbour’s name and/or distance! ")
                        neighId = input(print("Enter the neighbour Id for Sensor ",id,": "))
                        self.setNeighId(neighId)
                    while(('!' in neighId) == True):    
                        print("This is an invalid entry for the neighbour’s name and/or distance! ")
                        neighId = input(print("Enter the neighbour for Sensor ",id,": "))      
                        self.setNeighId(neighId)
                    dist =input(print("Enter the distance to ",neighId,": "))
                    while(dist.isnumeric() ==False):
                        print("This is an invalid entry for the neighbour’s name and/or distance! ")
                        dist = input("Enter the distance to ",neighId,": ")
                    listOfSensors += [[neighId,int(dist)]]
            oxlevel = input("Enter the Oxygen level in %: ")
            while(oxlevel.isnumeric() ==False):
                print("This is an invalid entry for the oxygen level! ")
                oxlevel = input("Enter the Oxygen level in %: ")
                self.setOxLevel(oxlevel)
            temp =input("Enter the temperature measurement: ")
            self.setTemprature(temp)
            res = False
            while(res == False):
                try:
                    float(temp)
                    res =True
                except :
                    print("This is an invalid entry for the temperature! ")
                    temp =input("Enter the temperature measurement: ")
                    self.setTemprature(temp)
                    res =False
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
