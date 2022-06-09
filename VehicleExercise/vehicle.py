
#Task:

#Please complete the following

# 1)Create a Vehicle class with max_speed and mileage instance attributes



# 2) Create a Vehicle class without any variables and methods

# 3) Create a child class Bus that will inherit all of the variables and methods of the 1st Vehicle class


# 4) Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.

# 5) Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

# 6) Define property that should have the same value for every class instance
# (Define a class attribute”colour” with a default value white)

#7) Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#Note: The bus seating capacity is 50. so the final fare amount should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.
class Vehicle:
    def __init__(self, name,max_speed, mileage, capacity):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity*100


class Bus(Vehicle):
    def fare(self):
        ammount = super().fare()
        new_ammount = ammount*1.1
        return new_ammount

bus = Bus("School Bus", 25, 22334455, 75)
print(bus.fare())

'''
    def seating_capacity(self):
        capacity = 50
        return capacity
    def fare_charge(self,seating_capacity):
        self.seating_capacity = seating_capacity
        seating_capacity = 50
        return seating_capacity*100


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, colour="white"):
        super().__init__( max_speed, mileage)
        self.colour = colour

  '''

'''
bus1 = Bus("70","123456")
print(bus1.__dict__)
print(bus1.seating_capacity())
print(bus1.fare_charge())'''