class Estrutura():
    
    def __init__(self):
        self.email = ""
        self.gender = ""
        self.uid = ""
        self.birthdate = ""
        self.height = ""
        self.weight = ""
        
    def __str__(self):
        return "Registro: " + str(self.email) + ' ' + str(self.gender) + ' ' + str(self.uid) + ' ' + str(self.birthdate) + ' ' + str(self.height) + ' ' + str(self.weight)
    
    def __getitem__(self, key):
        return self.uid
        
    def set_email(self, email):
        self.email = email
        
    def set_gender(self, gender):
        self.gender = gender
        
    def set_uid(self, uid):
        self.uid = uid
        
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
        
    def set_height(self, height):
        self.height = height
    
    def set_weight(self, weight):
        self.weight = weight
        
    def get_uid(self):
        return self.uid