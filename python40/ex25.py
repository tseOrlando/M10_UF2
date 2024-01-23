
class vehicle_t:

    def __init__(self, marca, model, any, matricula, gasoil):
        self.marca = marca
        self.model = model
        self.any = any
        self.matricula = matricula
        self.gasoil = gasoil

    def to_dict(self):
        return [{"vehicle":{"marca":self.marca, "model":self.model, "any":self.any, "matricula":self.matricula, "gasoil":self.gasoil}}]
    
    def show(self):
        print("vehicle data")
        print(self.marca)
        print(self.model)
        print(self.any)
        print(self.matricula)
        print(self.gasoil)

    def get_marca(self):
        return self.marca
    
    def get_model(self):
        return self.model
    
    def get_any(self):
        return self.any
    
    def get_matricula(self):
        return self.matricula
    
    def get_gasoil(self):
        return self.gasoil
    
    def set_marca(self, marca):
        self.marca = marca

    def set_model(self, model):
        self.model = model
        
    def set_any(self, any):
        self.any = any
        
    def set_matricula(self, matricula):
        self.matricula = matricula
        
    def set_gasoil(self, gasoil):
        self.gasoil = gasoil
