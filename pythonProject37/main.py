class Chair:
    def __init__(self, countlegs, material, color):
        self.countlegs = countlegs
        self.material = material
        self.color = color
        
    def corect_material(self, text):
        return self.material == text
        
    def __str__(self):
        return f"Chair({self.countlegs}), material({self.material}) , color({self.color})."
        
    def __repr__(self):
        return str(self.countlegs)

a = Chair(4, 'wood', 'Nutty')
print(a)
