class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big_slot = big
        self.medium_slot = medium
        self.small_slot = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            self.big_slot -= 1
            ans = True if self.big_slot>=0 else False
            return ans
        elif carType == 2:
            self.medium_slot -= 1
            ans = True if self.medium_slot>=0 else False
            return ans
        else:
            self.small_slot -= 1
            ans = True if self.small_slot>=0 else False
            return ans

if __name__ == "__main__":
    obj = ParkingSystem(2,1,2) # big, medium, small
    param_1 = obj.addCar(2) # medium
    print(param_1)