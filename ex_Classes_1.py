next_id = 1000

class Product:

    def __init__(self, name, description, price, quantity):
        if not isinstance(description, str):
            raise ValueError("Opis powinien być napisem")
        if not isinstance(price, float):
            raise ValueError("Cena to float")
        if price <= 0.01:
            raise ValueError("Podana cena musi być większa niż 0.01")
        if not isinstance(quantity, int):
            raise ValueError("W ilości musi być liczba")
        if quantity <= 0:
            raise ValueError("Ilość musi być większa od zera")

        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

        global next_id
        self._id = next_id
        next_id += 1

    #     print(str(self))
    #
    # def __str__(self):
    #     return "Produkt: {} \nOpis: {} \nCena w zł: {} \nIlość szt.: {} \nID: {}".format(
    #         self._name, self._description, self._price, self._quantity, self._id
    #     )

    def total_sum(self):
        return self._quantity * self._price

if __name__ == '__main__':
    produkt1 = Product("Marchewka", "Świeża marchew", 1.55, 4)
    print(produkt1.total_sum())
    produkt2 = Product("Cytryna", "Żółte cytryny", 5.95, 3)
    print(produkt2.total_sum())
    produkt3 = Product("Rabarbar", "Słodki rabarbar", 100.00, 1)
    print(produkt3.total_sum())