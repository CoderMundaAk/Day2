class Animal:
    ''' That is my prent class its name is Animul
    '''
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Generic animal sound")
    def show_detail(self):
        print(f" Name:{self.name} Species:{self.species}")
class Dog(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
        super().show_detail()
    def make_sound(self):
        print("woof!")
    def fetch_ball(self):
        print("pick up the ball")
    # def show_detail(self):
    #     print(f" Name:{self.name} Species:{self.species}")

a=Animal("jackey","pitchata")
d=Dog("ff","hh")
a.show_detail()
d.show_detail()
a.make_sound()
d.make_sound()
d.fetch_ball()
print(Animal.__doc__)
        