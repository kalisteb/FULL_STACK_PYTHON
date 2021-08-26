# 7. Prueba tus clases creando una instancia de la Tienda y algunas instancias de la clase Producto, agrega esas instancias a la instancia de la tienda y luego prueba los métodos.

import store as store
import producto as producto

tienda1 = store.Store("tiendita")
prod1 = producto.Product("Agua mineral", 1000, "Bebidas", "0000000000001")
prod2 = producto.Product("Pan Marraqueta", 1400, "Panadería", "0000000000002")
prod3 = producto.Product("Tallarines", 700, "Pastas", "0000000000003")
prod4 = producto.Product("Pan Hot Dog", 1600, "Panadería", "0000000000004")

tienda1.add_product(prod1).add_product(prod2).add_product(prod3).add_product(prod4)

print("Productos")
prod1.print_info()
print("")
prod2.print_info()
print("")
prod3.print_info()
print("")
prod4.print_info()
print("")
tienda1.sell_product(3)
print("")


print("************************************")
tienda1.set_clearance("Bebidas",10).inflation(3)

prod1.print_info()
print("")

prod3.print_info()
print("")