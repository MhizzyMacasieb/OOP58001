# Week 11 Quiz
# For instance that the following distance unit conversion formula:
    # centimeter = meter * 100
    # kilometer = meter / 1000
    # inches = meter *39.37
# Create a class DistanceConversion with attribute distance
# Create different methods to convert meter to centimeter, meter to kilometer, and meter to inch
# Use mangling for encapsulation
# The program will accept user input and by showing the three consecutive outputs (meter to centimeter, meter to kilometer, and meter to inch)

class DistanceConversion:
    def __init__(self, meter):
        self.meter = meter


    def Centimeter(self):
        return self.meter * 100


    def Kilometer(self):
        return self.meter / 1000


    def Inches(self):
        return self.meter * 39.37


m=int(input("Enter the Meters: "))
obj=DistanceConversion(m)
print("Meters to Centimeters: ", obj.Centimeter(), )
print("Meters to Kilometers: ", obj.Kilometer(), )
print("Meters to Inches: ", obj.Inches(), )