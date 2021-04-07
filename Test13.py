class building:
    buildingName="Twin Tower"
    Floors=14
    def __init__(self,wingName,rooms):
        self.wing = wingName
        self.perFloorRooms = rooms
        self.TotalRooms = rooms * building.Floors

    def wingDetails(self):
        print("Wing - ",self.wing)
        print("Per floor rooms - ",self.perFloorRooms)
        print("Total rooms - ",self.TotalRooms)

    @classmethod
    def buildingDetails(cls):
        print("Name - ",cls.buildingName)
        print("Floors - ",cls.Floors)

    @staticmethod
    def Area(area):
        print("Area -",area)

building.buildingName="Twin Tower"
building.Floors=14
building.buildingDetails()
A=building("A",6)
A.wingDetails()
building.Area("Tirupati Nagar")