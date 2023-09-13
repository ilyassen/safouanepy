
class Champion:                   
 
    def __init__(self,name,championsexe,place,year,role,power):
        self.name = name
        self.gender = championsexe     
        self.place = place
        self.year = year
        self.role = role 
        self.power = power

    def get_gender(self):
        return self.gender

    def get_place(self):
        return self.place
    
    def get_year(self):
        return self.year
    
    def get_role(self):
        return self.role
    
    def get_power(self):
        return self.power
    def get_name(self):
        return self.name

    def display(self):
        print("Name: " + self.get_name())
        print("Gender : " + self.get_gender())
        print("place : " + self.get_place())
        print("year : " + self.get_year())
        print("role : " + self.get_role())
        print("power : " +self.get_power())

champion1 = Champion("Zilean","Male","Shhurima","2009","mid/support","VERY OP")
champion2 = Champion("Warwick","who knows","Zhaun","2009","Top/jungle","VERY tilti")


champion_list = []
champion_list.append(champion1)

champion_list.append(champion2)

print("CHKON A7SAN CHAMPION F L3ALAM")
print(" ----- CHAMPION LI WA3ER BEZAAAF------")
champion1.display()
print(" -----------------")

print("CHKON LI M9TOUL MARRA W MSALI")
print(" ----- YOU ASKED FOR IT------ ")
champion2.display()
print(" -----------------")