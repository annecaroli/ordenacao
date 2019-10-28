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
    def get_email(self):
        return self.email
        
    def set_gender(self, gender):
        self.gender = gender
    def get_gender(self):
        return self.gender
        
    def set_uid(self, uid):
        self.uid = uid
    def get_uid(self):
        return self.uid 
        
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
    def get_birthdate(self):
        return self.birthdate
        
    def set_height(self, height):
        self.height = height
    def get_height(self):
        return self.height
    
    def set_weight(self, weight):
        self.weight = weight
    def get_weight(self):
        return self.weight
