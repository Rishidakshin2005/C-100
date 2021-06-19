class Car:
    def __init__(self, company,color):
        self.company= company
        self.color = color
     
    def startcar(self):
         print("car started")

    def stopcar(self):
        print("car stoped")

car1=Car("Maruti Suzuki Swift", "red")
car2=Car("Honda City", "grey")
print(car2.color)
car1.startcar()