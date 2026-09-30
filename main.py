#from driver import Driver
from driver import *
def main():
    d1 = Driver("Amulya",5,123,False)
    d2 = Driver("Amulya",5,123,False)

    d3 = Driver("Shiva",driverId=345,is_Online=True)
print(d3.driveId)
print(d3.is_Online)
