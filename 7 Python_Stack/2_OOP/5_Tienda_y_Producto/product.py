# 2. Crea una clase de Producto que tenga 3 atributos: un nombre, un precio y una categoría. Todo esto debe proporcionarse en el momento de la creación.
        
class Product:
    def __init__(self, description, price, category, code):
        self.description = description
        self.price = price
        self.category = category
        self.code = code
        
    # 3. Agrega el método print_info (self) a la clase producto: imprime el nombre del producto, su categoría y su precio.
    
    def print_info(self):
        print("Código ", self.code)
        print("Nombre: ", self.description)
        print("Categoría: ", self.category)
        print("Precio: $", self.price)
        
        return self
        
    # 4. Agrega el método update_price(self, percent_change, is_increased) : actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
    
    def update_price(self, percent_change, is_increased):
        if is_increased==True :
            self.price += self.price*percent_change/100
        else:
            self.price -= self.price*percent_change/100
        return self
    