# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def def __init__(self, name, description, items=[]):
      self.name = name
      self.description = description
      
      self.n_to = None
      self.s_to = None
      self.e_to = None
      self.w_to = None
    
    def __str__(self):
      return self.name, self.descr
    
    
