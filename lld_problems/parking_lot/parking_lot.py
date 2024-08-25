# identify objects
# - Vehicle
# - Parking spot
# - Ticket
# - Entrance
# - Exit
from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

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

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self):
        pass

class TwoWheelerParkingStrategy(ABC):

    def find_parking_spot(self,parking_spots):
        spot_list = []
        for spot in parking_spots:
            if spot.isEmpty:
                spot_list.append(spot)
        return spot_list


class FourWheelerParkingStrategy(ABC):

    def find_parking_spot(self, parking_spots):
        spot_list = []
        for spot in parking_spots:
            if spot.isEmpty:
                spot_list.append(spot)
        return spot_list



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
    def __init__(self,id):
        self.parking_id = id
        self.isEmpty = True
        self.vehicle = None

    def park(self, v: Vehicle):
        if self.isEmpty:
            self.vehicle = v
            self.isEmpty = False
            print(f"parking Succesful at {self.parking_id} for vehicle {self.vehicle.vehicle_id}")

    def remove(self, v: Vehicle):
        if not self.isEmpty:
            self.vehicle = None
            self.isEmpty = True
            print(f"vehicle at {self.parking_id} is freed ,last  vehicle {self.vehicle.vehicle_id}  ")

class FourWheelerParkingSpot(ParkingSpot):
    def __init__(self):
        self.parking_id = None
        self.isEmpty = True
        self.vehicle = None

    def park(self,v: Vehicle):
        if self.isEmpty:
            self.vehicle = v
            self.isEmpty = False
            print(f"parking Succesful at {self.parking_id} for vehicle {self.vehicle.vehicle_id}")

    def remove(self,v: Vehicle):
        if not self.isEmpty:
            self.vehicle = None
            self.isEmpty = True
            print(f"vehicle at {self.parking_id} is freed ,last  vehicle {self.vehicle.vehicle_id}  ")


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
    _two_wheeler_parking_spots: List[TwoWheelerParkingSpot]  = []
    def __init__(self,parking_spots: List[TwoWheelerParkingSpot]):
        super().__init__(parking_spots)


    def find_parking_spot(self):
        ps = TwoWheelerParkingStrategy()
        parking_spot_list = ps.find_parking_spot(self.parking_spots)
        if len(parking_spot_list) == 0:
            print("No parking spot found")
        else:
            return parking_spot_list[0]


    def park_vehicle(self,  v: Vehicle,parking_spot_obj: ParkingSpot):
        # parking_spot_obj = self.find_parking_spot()
        parking_spot_obj.park(v)

    def remove_vehicle(self,parking_spot_obj:ParkingSpot):
        parking_spot_obj.remove()
    def clear_parking_spot(self, v: Vehicle):
        for spot in self.parking_spots:
            if spot.vehicle == v:
                self.remove_vehicle(spot)
                break


class FourWheelerParkingSpotManager(ParkingSpotManager):  # abstract class to manage parking spots
    _four_wheeler_parking_spots : List[FourWheelerParkingSpot]  = []
    def __init__(self,parking_spots: List[FourWheelerParkingSpot]):
        super().__init__(parking_spots)


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
        FourWheelerParkingSpot().remove(v)

    def clear_parking_spot(self, v: Vehicle):
        self.remove_vehicle(v)

class ParkingSpotFactory:
    @staticmethod
    def get_psm( vehicle: Vehicle,parking_spot):
        if vehicle.vehicle_type == 'two-wheeler':
            return TwoWheelerParkingSpotManager(parking_spot)
        if vehicle.vehicle_type == 'four-wheeler':
            return FourWheelerParkingSpotManager()

class Ticket:
    def __init__(self,id,vehicle,parking_spot):
        self.ticket_id = id
        self.entry_time = datetime.now()
        self.vehicle: Vehicle = vehicle
        self.parking_spot:ParkingSpot = parking_spot


    def get_ticket(self): #get ticket
        print(f"Ticket genrated for {self.parking_spot.parking_id}, {self.vehicle.vehicle_id} at {self.entry_time}")


class Entrance():
    def __init__(self, vehicle: Vehicle,parking_spot):
        self.ticket_obj: Ticket = None
        self.vehicle_obj: Vehicle = vehicle
        self.park_obj: ParkingSpotFactory = ParkingSpotFactory.get_psm(self.vehicle_obj,parking_spot)

    def find_parking_spot(self):

        self.parking_spot = self.park_obj.find_parking_spot()
        self.park_obj.park_vehicle(self.vehicle_obj,self.parking_spot)


    def genrate_ticket(self):
        self.ticket_obj = Ticket(1,self.vehicle_obj,self.parking_spot)
        self.ticket_obj.get_ticket()

class Exit():
    def __init__(self, ticket: Ticket):
        self.ticket: Ticket = None
        self.park_obj: ParkingSpotFactory = ParkingSpotFactory.get_psm(self.vehicle_obj)

    # def find_parking_spot(self):


    def cost_compute(self):
        if self.vehicle_obj.vehicle_type == 'two-wheeler':
            print("Cost to pe paid: ", 20)
        if self.vehicle_obj.vehicle_type == 'four-wheeler':
            print("Cost to pe paid: ", 40)

    def remove_vehicle(self):
        self.park_obj.clear_parking_spot(self.vehicle_obj)



if __name__ == "__main__":
    # l = [TwoWheeler("KA05LL1128"),FourWheeler("UP78GL7080"),TwoWheeler("KA45AK1128"),FourWheeler("UP78UL7780"),TwoWheeler("KA45AK1128"),FourWheeler("UP78UL7780")]
    # for v in l:
    #     Entrance(v).find_parking_spot()
    # for v in l:
    #     Exit(v).remove_vehicle()
    #     Exit(v).cost_compute()

    v  = TwoWheeler("KA05LL1128")
    v2 = TwoWheeler("KA05LL1129")
    v3 = TwoWheeler("KA05LL1127")
    l = [TwoWheelerParkingSpot(1),TwoWheelerParkingSpot(2)]
    ob = Entrance(v,l)
    ob.find_parking_spot()
    ob.genrate_ticket()
    ob2 = Entrance(v2,l)
    ob2.find_parking_spot()
    ob2.genrate_ticket()
    # Entrance(v3, l).find_parking_spot()
    # Entrance(v, l).find_parking_spot()









