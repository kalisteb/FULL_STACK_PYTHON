# 1. Crea una clase de Tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en el momento de la creación, pero la lista de productos debe estar vacía.

class Store:
    def __init__(self,  name,  products=[]):
        self.name = name
        self.products = products

    
    # 5. Agrega el método add_product (self, new_product) a la clase store: toma un producto y lo agrega a la tienda
        
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    # 6. Agrega el método sell_product (self, id)a la clase Store : elimina el producto de la lista de productos de la tienda dada la identificación (suponga que id es el índice del producto en la lista) e imprima su información.
    
    def  sell_product(self,  id):
        print("Imprimiendo la información del producto")
        self.products[id].print_info()
        del self.products[id]
        print("El producto ha sido eliminado!")
        return self
    
    # 8 NINJA BONUS: Agrega el método inflation(self, percent_increase) a la clase Store: aumenta el precio de cada producto por el percent_increase dado (¡use el método que escribió en la clase Product!)
    def inflation(self, percent_increase):
        for product_ in self.products:
            product_.update_price(percent_increase, True)
        return self
    
    # 9. NINJA BONUS: Agregue el método set_clearance (self, category, percent_discount) a la clase Store: actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)
    
    def set_clearance(self, category, percent_discount):
        for producto in self.products:
            if producto.category == category:
                producto.update_price(percent_discount, False)
        return self