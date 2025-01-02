# DO NOT MODIFY THE PLANT CLASS
class Plant:
    def __init__(self, starting_energy):
        self.energy = starting_energy

    def absorb_sunlight(self, sunlight_energy):
        self.energy += sunlight_energy

    def __str__(self):
        return f"I am a {type(self).__name__} and I have {self.energy} energy!" 


##########################################
#       Add your new classes here!       #
# (Make sure not to accidentally indent) #
##########################################

class Potato(Plant):
    def __init__(self, starting_energy):
        super().__init__(starting_energy)
        self.tubers = []

    def __str__(self):
        return f"I am a Potato and I have {self.energy} energy!"

    def sprout_tuber(self):
        if self.energy >= 30:
            new_tuber = Tuber()
            self.tubers.append(new_tuber)
            self.energy -= 30
            
    def absorb_sunlight(self, sunlight_energy):
        if self.tubers:
            self.energy += sunlight_energy // 2

            energy_per_tuber = sunlight_energy // 2 // len(self.tubers)
            for tuber in self.tubers:
                tuber.energy += energy_per_tuber
        else:
            self.energy += sunlight_energy



class Tuber():
    def __init__(self, energy=30):
        self.energy = energy

    

########## WAVE 1 ##########
# Checking the behavior for creating an instance of Potato
assert issubclass(Potato, Plant), "Potato must be a subclass of Plant"
my_potato = Potato(70)
assert my_potato.energy == 70
assert my_potato.tubers == []
assert str(my_potato) == "I am a Potato and I have 70 energy!"
print("Wave 1 passed!")


########## WAVE 2 ##########
# Checking the behavior for sprouting one tuber
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 1
first_tuber = my_potato.tubers[0]
assert isinstance(first_tuber, Tuber), "A Potato's tubers must be instances of class Tuber"
assert first_tuber.energy == 30
assert my_potato.energy == 40

# Checking the behavior for sprouting a second tuber
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 2
assert my_potato.tubers[0].energy == 30
assert my_potato.tubers[1].energy == 30
assert my_potato.energy == 10

# Checking the behavior for attempting to sprout a tuber when the potato
# does not have enough energy
my_potato.sprout_tuber()
assert len(my_potato.tubers) == 2
assert my_potato.tubers[0].energy == 30
assert my_potato.tubers[1].energy == 30
assert my_potato.energy == 10
print("Wave 2 passed!")


########## WAVE 3 ##########
# Checking the behavior for absorbing sunlight for a 
# potato with multiple tubers
my_potato.absorb_sunlight(100)
assert my_potato.energy == 60
assert my_potato.tubers[0].energy == 55
assert my_potato.tubers[1].energy == 55

# Checking the behavior for absorbing sunlight for a 
# potato with one tuber
new_potato = Potato(30)
new_potato.absorb_sunlight(40)
assert new_potato.energy == 70
print("Wave 3 passed!")

print("All tests passed!")
print("If time remains, discuss alternate design decisions you could have made, or other ways you may think to add more functionality to your code.")
