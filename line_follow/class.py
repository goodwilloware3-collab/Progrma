class vehicle:
    def __init__(self,model,make):
        self.model=model
        self.make=make
    def moves(self):
        print("Moving along")
    def make_model(self):
        print(f"I'm a {self.make} {self.model}")
my_car=vehicle("TEsla","Mode 3")
print(my_car.model)
print(my_car.make)

my_car.moves()
class Airplane(vehicle):
    def __init__(self,model,make,faa_id):
        super().__init__(self, model,make)
        self.faa_id=faa_id
    def moves(self):
        print("Flying along")
class TRuck(vehicle):
    def moves(self):
        print("rumbling along")
class golf_cart(vehicle):
    def moves(self):
        pass
cessna=Airplane("cessna","Skyhawk")
cessna.moves()
cessna.make_model()

mack=TRuck("Mack","Anthem")
mack.moves()
mack.make_model()

golf= golf_cart("Club Car","Onward")
golf.moves()
golf.make_model()



for i in (my_car,cessna,mack,golf):
    i.moves()
    i.make_model()