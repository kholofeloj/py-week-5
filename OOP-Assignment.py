class smartPhone:
    
    simSlots = 2

    def __init__(self, brand, model, color,):
        self.brand = brand
        self.model = model
        self.color = color

    def ring(self):
        print(f"My {self.color} {self.brand} {self.model} is ringing")


phone1 = smartPhone("Apple", "iPhone 16 Pro Max", "black")
phone2 = smartPhone("Samsung", "Galaxy S25 Ultra", "white")

phone1.ring()