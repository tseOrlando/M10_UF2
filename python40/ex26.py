
class user_t:

    def __init__(self, name, surname, email, dni, mf):
        self.name = name
        self.surname = surname
        self.email = email
        self.dni = dni
        self.mf = mf

    def to_dict(self):
        return [{"user":{"name":self.name, "surname":self.surname, "email":self.email, "dni":self.dni, "mf":self.mf}}]
    
    def show(self):
        print("vehicle data")
        print(self.name)
        print(self.surname)
        print(self.email)
        print(self.dni)
        print(self.mf)

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_any(self):
        return self.any
    
    def get_dni(self):
        return self.dni
    
    def get_mf(self):
        return self.mf
    
    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname
        
    def set_any(self, any):
        self.any = any
        
    def set_dni(self, dni):
        self.dni = dni
        
    def set_mf(self, mf):
        self.mf = mf
