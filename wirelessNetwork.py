class WirelessNetwork:
    ADHOC_MODE = "ON"
    BRAND_NAME = "Cisco"

    def __init__(self):
        self._id = ""
        self._oxygenLevel = 0
        self._temprature =0.0
       

    @staticmethod
    def greetingMessage():
        print("******************************************************************************")
        print("Welcome to the company's IoT-Based Health System")
    
    @classmethod
    def brand(cls):
        print("These are sensors of ",cls.BRAND_NAME,", and their Ad Hoc Mode is ",cls.ADHOC_MODE)
        print("****************************************************************************** ")   

    


