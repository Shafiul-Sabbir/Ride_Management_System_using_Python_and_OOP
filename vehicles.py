from abc import ABC, abstractmethod
class Vehicle(ABC):
    speed = {
        'car' : 30,
        'bike' : 50,
        'cng' : 15
    }
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.driver = driver
        self.status = 'available'
        self.speed = self.speed[vehicle_type]
        
    # @abstractmethod
    # def start(self):
    #     pass
    
    # @abstractmethod
    # def move(self):
    #     pass
    
    # @abstractmethod
    # def trip_finished(self):
    #     pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
        
        
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'start driving.')
        distance = abs(start - destination)
        import time
        for i in range(0, distance):
            time.sleep(.1)
            print(f'Driving {self.license_plate} current position {i} of distance {distance} \n')
            
        self.trip_finished()
        
        
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip.')
        
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
        
        
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'start driving.')
        distance = abs(start - destination)
        import time
        for i in range(0, distance):
            time.sleep(.1)
            print(f'Driving {self.license_plate} current position {i} of distance {distance} \n')
            
        self.trip_finished()
        
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip.')
        
        
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
        
        
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'start driving.')
        distance = abs(start - destination)
        import time
        for i in range(0, distance):
            time.sleep(.1)
            print(f'Driving {self.license_plate} current position {i} of distance {distance} \n')
            
        self.trip_finished()
        
        
    def trip_finished(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'completed trip.')
        
        