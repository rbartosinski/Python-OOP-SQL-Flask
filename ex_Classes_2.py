from ex_Classes_1 import Product

class ShoppingCart():

    def __init__(self):
        products = []
        self.products = products

    def add_product(self, added_product):
        self.products.append(added_product)
        print("Do koszyka dodano {}".format(added_product._name))
        return self.products

    def remove_product(self, product_id):
        for product in self.products:
            if product_id == product._id:
                self.products.remove(product)
                print("Usunięto: {}".format(product._name))
                return self.products
            else:
                pass

    def change_product_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product._id == product_id:
                product._quantity = new_quantity
                print ("Zmieniono ilość produktu {} na {}".format(product._name, product._quantity))
                return self.products
            else:
                pass

    def get_total_sum(self):
        total_sum = 0
        for product in self.products:
            if product._quantity >= 3:
                off = product._price * product._quantity * 0.2
                total_sum += product._price * product._quantity - off
                print("Naliczono rabat do {}\n               {} zł".format(
                    product._name, off
                ))
            else:
                total_sum += product._price * product._quantity
        return total_sum

    def print_receipt(self):
        for product in self.products:
            print ("\n{}  {}\n               x{}  {} zł".format(
                product._id, product._name, product._quantity, product._price
            ))

        print("Do zapłaty:\n               {} zł".format(self.get_total_sum()))

if __name__ == "__main__":
    produkt1 = Product("Marchewka", "Świeża marchew", 1.50, 1)
    produkt2 = Product("Cytryna", "Żółte cytryny", 5.90, 1)
    produkt3 = Product("Rabarbar", "Słodki rabarbar", 100.00, 1)

    Cart1 = ShoppingCart()

    Cart1.add_product(produkt1)
    Cart1.add_product(produkt1)
    Cart1.add_product(produkt3)

    Cart1.remove_product(1000)
    Cart1.remove_product(1005)

    Cart1.change_product_quantity(1000, 3)
    Cart1.print_receipt()

    Cart1.change_product_quantity(1000, 2)
    Cart1.print_receipt()
