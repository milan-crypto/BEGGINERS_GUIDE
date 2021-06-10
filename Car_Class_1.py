class Car:

    def __init__(self, brand, model, engine_size, power, top_speed, torque, CO2_emissions, miles_per_tank, year, colour, interior, MOT_due, annual_road_tax):
        self.vehicle_kind = "Car"
        self.brand = brand
        self.model = model
        self.engine_size = engine_size
        self.power = power
        self.top_speed = top_speed
        self.torque = torque
        self.CO2_emissions = CO2_emissions
        self.miles_per_tank = miles_per_tank
        self.year = year
        self.colour = colour
        self.interior = interior
        self.MOT_due = MOT_due
        self.annual_road_tax = annual_road_tax
        self.reg()


    def reg(self):
        print("REG: M9LXN")



Alfa = Car("Alfa Romeo", "Brera", "3200cc", "275 BHP", "172mp/h", "400NM", "270g/km", "369 miles", "2007", "Silver", "Red Leather", "MOT Due: 17th June 2021", "£670" )

print(Alfa.brand)
print(Alfa.model)
print(Alfa.engine_size)
print(Alfa.power)
print(Alfa.top_speed)
print(Alfa.torque)
print(Alfa.CO2_emissions)
print(Alfa.miles_per_tank)
print(Alfa.year)
print(Alfa.colour)
print(Alfa.interior)
print(Alfa.MOT_due)
print(Alfa.annual_road_tax)


# Merc = Car("Mercedes Benz", "190D", "2500cc", "1990", "White", "Black Leather")
#
# print(Merc.brand)
# print(Merc.model)
# print(Merc.engine_size)
# print(Merc.year)
# print(Merc.colour)
# print(Merc.interior)


class Car:
    def __init__(self, year, make, speed):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def set_year_model(self, year):
        self.__year_model = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #methods
    def accelerate(self):
        self.__speed +=5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed

def main():

    year = input('Enter the car year: ')
    make = input('Enter the car make: ')
    speed = 0

    mycar = Car(year, make, speed)

    #Accelerate 5 times
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())

    #Brake 5 times
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())

#Call the main function
main()
