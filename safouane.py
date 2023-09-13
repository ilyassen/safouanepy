
class Dog:                   
 
    def __init__(self,dogBreed,dogEyeColor):
    
        self.breed = dogBreed       
        self.eyeColor = dogEyeColor

    def get_breed(self):
        return self.breed

    def get_eyeColor(self):
        return self.eyeColor
    
    def display(self):
        print("Breed : " + self.get_breed())
        print("Eye Color : " +self.get_eyeColor())

dog1 = Dog("Nasus","Black")
dog2 = Dog("ChienLoup","Blue")

Dogs_list = []
Dogs_list.append(dog1)

Dogs_list.append(dog2)

for item in Dogs_list:
    print(" ----- Item ------")
    item.display()
    print(" -----------------")