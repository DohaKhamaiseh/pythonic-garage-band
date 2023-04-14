from abc import ABC, abstractmethod

""" This class is for building up a band that has a Guitarist, Drummer, and  Bassist as  members, I will explain each  method for this class """
class Band:
    instances = []
     
    """ this method initializes the class attributes, which are the name of the band and its members"""
    def __init__(self,name,members):
        self.name= name
        self.members= members
        Band.instances.append(self)
    
    """ this method is to call the paly_solo function(I will explain this function below) for each member and append the returned string from that function in a list """
    def play_solos(self):
       list = []
       for musician in self.members:
        #    print(f' {musician.name} please start playing' 
          list.append(musician.play_solo())
       return list
           
    """ this method will return a string that is intended for the user, a string  has the band name and its members """
    def __str__(self): 
        return f'Band name is : {self.name} and its members are {self.members}'
    
    """ this method will return a string that is intended for the developer a string has just the band name"""
    def __repr__(self): 
        return f'I am a representation of {self.name}'
    
    """this method will return a list containing all instances that are created from the Band class """
    @classmethod
    def to_list(cls):
        return cls.instances
"""this class is the father class for any kind of Musician and it just has the name of him/her attribute """
class Musician :
    """this method initializes the name attribute that is the musician name  """
    def __init__(self, name):
        self.name = name
        # self.instrument = instrument

"""this class is inherited from class for Musician class, it has some methods related to the Guitarist"""
class Guitarist(Musician):
    
    """this method initializes the name attribute that is the musician name by sending the name to the father class(Musician)  """
    def __init__(self, name):
         super().__init__(name)
    
    """ this method will return a string that is intended for the user, a string  has the musician name and his/her instrument which is guitar """
    def __str__(self): 
        #  "My name is Joan Jett and I play guitar"
         return f'My name is {self.name} and I play guitar'   
    
    """ this method will return a string that is intended for the developer a string has just the musician name """
    def __repr__(self): 
        # "Guitarist instance. Name = Joan Jett"
        return f'Guitarist instance. Name = {self.name}' 
    
    """this method will return a string has the musician instrument which is here a guitar"""
    def get_instrument(self):
       return f'guitar' 
   
    """this method will return an expression used in rock and heavy metal music to describe a particularly awe-inspiring guitar solo. """
    def play_solo(self):
        # "face melting guitar solo"
        return f'face melting guitar solo'

"""this class is inherited from class for Musician class, it has some methods related to the Drummer"""    
class Drummer(Musician):
    """this method initializes the name attribute that is the musician name by sending the name to the father class(Musician)  """
    def __init__(self, name):
         super().__init__(name)
    
    """ this method will return a string that is intended for the user, a string  has the musician name and his/her instrument which is drums """
    def __str__(self): 
        #  "My name is Sheila E. and I play drums"
         return f'My name is {self.name} and I play drums'   
    
    """ this method will return a string that is intended for the developer a string has just the musician name """
    def __repr__(self): 
        # "Drummer instance. Name = Sheila E."
        return f'Drummer instance. Name = {self.name}'
    
    """this method will return a string has the musician instrument which is here a drums"""
    def get_instrument(self):
       return f'drums' 
    
    """this method will return a words that create an image of a chaotic and noisy situation."""
    def play_solo(self):
        # "rattle boom crash"
        return f'rattle boom crash'

"""this class is inherited from class for Musician class, it has some methods related to the Bassist"""    
class Bassist(Musician):

    """this method initializes the name attribute that is the musician name by sending the name to the father class(Musician)  """
    def __init__(self, name):
         super().__init__(name)
    
    """ this method will return a string that is intended for the user, a string  has the musician name and his/her instrument which is bass """
    def __str__(self): 
        #  "My name is Meshell Ndegeocello and I play bass"
         return f'My name is {self.name} and I play bass'   
    
    """ this method will return a string that is intended for the developer a string has just the musician name """
    def __repr__(self): 
        # "Bassist instance. Name = Meshell Ndegeocello"
        return f'Bassist instance. Name = {self.name}' 
    
    """this method will return a string has the musician instrument which is here a bass"""
    def get_instrument(self):
       return f'bass' 
    
    """this method wiil return a sounds that create a sense of movement and momentum in the music."""
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


