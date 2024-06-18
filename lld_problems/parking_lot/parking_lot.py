# identify objects
# - Vehicle
# - Parking spot
# - Ticket
# - Entrance
# - Exit
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.vehicle_id = None
        self.vehicle_type = None

class TwoWheeler(Vehicle):
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.vehicle_type = 'two-wheeler'

class FourWheeler(Vehicle):
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.vehicle_type = 'four-wheeler'

class ParkingSpot(ABC):  #abstract class to store parking spot info
    def __init__(self):
        self.parking_id = None
        self.isEmpty = True
        self.vehicle = None

    @abstractmethod
    def park(self,v: Vehicle):
        pass

    @abstractmethod
    def remove(self,v :Vehicle):
        pass


class TwoWheelerParkingSpot(ParkingSpot):
    def __init__(self):
        self.parking_id = None
        self.isEmpty = True
        self.vehicle = None

    def park(self, id, v: Vehicle):
        if self.isEmpty:
            self.vehicle = v
            self.isEmpty = False
            self.parking_id = id
            print(f"parking Succesful at {self.parking_id} for vehicle {self.vehicle.vehicle_id}")

    def remove(self, v: Vehicle):
        if not self.isEmpty:
            self.vehicle = None
            self.isEmpty = True
            self.parking_id = None

class FourWheelerParkingSpot(ParkingSpot):
    def __init__(self):
        self.parking_id = None
        self.isEmpty = True
        self.vehicle = None

    def park(self,id,v: Vehicle):
        if self.isEmpty:
            self.vehicle = v
            self.isEmpty = False
            self.parking_id = id
            print(f"parking Succesful at {self.parking_id} for vehicle {self.vehicle.vehicle_id}")

    def remove(self,v: Vehicle):
        if not self.isEmpty:
            self.vehicle = None
            self.isEmpty = True
            self.parking_id = None


class ParkingSpotManager(ABC): #abstract class to manage parking spots
    def __init__(self, parking_spots: list):
        self.parking_spots = parking_spots
    @abstractmethod
    def find_parking_spot(self, v:Vehicle):
        pass
    @abstractmethod
    def park_vehicle(self, v:Vehicle):
        pass
    @abstractmethod
    def remove_vehicle(self, v:Vehicle):
        pass

    @abstractmethod
    def clear_parking_spot(self, v: Vehicle):
        pass

class TwoWheelerParkingSpotManager(ParkingSpotManager): #abstract class to manage parking spots
    _two_wheeler_parking_spots = [None,None,None,None,None]
    def __init__(self):
        super().__init__(TwoWheelerParkingSpotManager._two_wheeler_parking_spots)


    def find_parking_spot(self, v: Vehicle):
        parked = False
        for index in range(len(self.parking_spots)):
            if self.parking_spots[index] is None:
                self.park_vehicle(index,v)
                parked = True
                self.parking_spots[index] = True
                return
        if not parked:
            print("No parking spots available in TwoWheeler ")

    def park_vehicle(self, id, v: Vehicle):
        TwoWheelerParkingSpot().park(id,v)

    def remove_vehicle(self, v: Vehicle):
        TwoWheelerParkingSpot().remove(id,v)
    def clear_parking_spot(self, v: Vehicle):
        self.remove(v)


class FourWheelerParkingSpotManager(ParkingSpotManager):  # abstract class to manage parking spots
    _four_wheeler_parking_spots = [None,None,None,None,None]
    def __init__(self):
        super().__init__(FourWheelerParkingSpotManager._four_wheeler_parking_spots)


    def find_parking_spot(self, v: Vehicle):
        parked = False
        for index in range(len(self.parking_spots)):
            if self.parking_spots[index] is None:
                self.park_vehicle(index,v)
                parked  = True
                self.parking_spots[index] = True
                return
        if not parked:
            print("No parking spots available in FourWheeler ")


    def park_vehicle(self, id,v: Vehicle):
        FourWheelerParkingSpot().park(id,v)

    def remove_vehicle(self, v: Vehicle):
        FourWheelerParkingSpot(v).remove(v)

    def clear_parking_spot(self, v: Vehicle):
        self.remove(v)

class ParkingSpotFactory:
    @staticmethod
    def get_psm( vehicle: Vehicle):
        if vehicle.vehicle_type == 'two-wheeler':
            return TwoWheelerParkingSpotManager()
        if vehicle.vehicle_type == 'four-wheeler':
            return FourWheelerParkingSpotManager()

class Ticket:
    def __init__(self):
        self.ticket_id = None
        self.entry_time = None

    def get_ticket(self): #get ticket


class Entrance():
    def __init__(self, vehicle: Vehicle):
        self.ticket_obj: Ticket = None
        self.vehicle_obj: Vehicle = vehicle
        self.park_obj: ParkingSpotFactory = ParkingSpotFactory.get_psm(self.vehicle_obj)

    def find_parking_spot(self):
        self.park_obj.find_parking_spot(self.vehicle_obj)

    def genrate_ticket(self):
        self.ticket_obj.get_ticket()

class Exit():
    def __init__(self, vehicle: Vehicle):
        self.vehicle_obj: Vehicle = vehicle
        self.park_obj: ParkingSpotFactory = ParkingSpotFactory.get_psm(self.vehicle_obj)

    def find_parking_spot(self):
        self.park_obj.clear_parking_spot(self.vehicle_obj)

    def cost_compute(self):
        if self.vehicle_obj.vehicle_type == 'two-wheeler':
            print("Cost to pe paid: ", 20)
        if self.vehicle_obj.vehicle_type == 'four-wheeler':
            print("Cost to pe paid: ", 40)

    def remove_vehicle(self):
        self.park_obj.remove(self.vehicle_obj)



if __name__ == "__main__":
    l = [TwoWheeler("KA05LL1128"),FourWheeler("UP78GL7080"),TwoWheeler("KA45AK1128"),FourWheeler("UP78UL7780"),TwoWheeler("KA45AK1128"),FourWheeler("UP78UL7780")]
    for v in l:
        Entrance(v).find_parking_spot()




