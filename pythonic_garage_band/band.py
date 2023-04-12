from abc import ABC, abstractmethod

class Band:
    instances = []

    def __init__(self,name,members):
        self.name= name
        self.members= members
        Band.instances.append(self)

    def play_solos(self):
       list = []
       for musician in self.members:
        #    print(f' {musician.name} please start playing' 
          list.append(musician.play_solo())
       return list
           
    
    def __str__(self): 
        return f'Band name is : {self.name} and its members are {self.members}'
    
    def __repr__(self): 
        return f'I am a representation of {self.name}'
    
    @classmethod
    def to_list(cls):
        return cls.instances

class Musician :
    def __init__(self, name):
        self.name = name
        # self.instrument = instrument


class Guitarist(Musician):
    
    def __init__(self, name):
         super().__init__(name)

    def __str__(self): 
        #  "My name is Joan Jett and I play guitar"
         return f'My name is {self.name} and I play guitar'   
    
    def __repr__(self): 
        # "Guitarist instance. Name = Joan Jett"
        return f'Guitarist instance. Name = {self.name}' 
    
    def get_instrument(self):
       return f'guitar' 
   
   
    def play_solo(self):
        # "face melting guitar solo"
        return f'face melting guitar solo'
    
class Drummer(Musician):
    def __init__(self, name):
         super().__init__(name)

    def __str__(self): 
        #  "My name is Sheila E. and I play drums"
         return f'My name is {self.name} and I play drums'   
    
    def __repr__(self): 
        # "Drummer instance. Name = Sheila E."
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
       return f'drums' 
    
    def play_solo(self):
        # "rattle boom crash"
        return f'rattle boom crash'

class Bassist(Musician):
    def __init__(self, name):
         super().__init__(name)

    def __str__(self): 
        #  "My name is Meshell Ndegeocello and I play bass"
         return f'My name is {self.name} and I play bass'   
    
    def __repr__(self): 
        # "Bassist instance. Name = Meshell Ndegeocello"
        return f'Bassist instance. Name = {self.name}' 
    
    def get_instrument(self):
       return f'bass' 
    
    def play_solo(self):
        # "bom bom buh bom"
        return f'bom bom buh bom'

if __name__ == "__main__":
    # Guitarist = Musician("Jo","Guitar")
    # Bassist = Musician ("Albirt", "Bass")
    # Drummer = Musician ("Shon","Drum")

    # print(Guitarist.play_solo())
    # print(Bassist.play_solo())
    # print(Drummer.play_solo())

    # Garage_band.play_solos()

    # members = [
    #     Guitarist("Kurt Cobain"),
    #     Bassist("Krist Novoselic"),
    #     Drummer("Dave Grohl"),
    # ]

    # one_band = Band("Nirvana",members)
    # print(one_band.play_solos())

    print(Band.to_list())


