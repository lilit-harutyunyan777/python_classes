
# 1

import random


class Person:
    CL_NAME = "EXAM RESULTS"

    def __init__(self, name, surname, address):
        self.name = name
        self.surname = surname
        self.address = address

    def present_general(self):
        return f"Hello, I'm {self.name} {self.surname} and I live in {self.address}"


class Student(Person):
    def __init__(self, exam_result, name, surname, st_address):
        super().__init__(name, surname, st_address)
        self.result = exam_result

    def present(self):
        return f"{super().present_general()}, I {self.result} my exam."


student_1 = Student("passed", "Ann", "Smith", "Cherry Road, SOUTHAMPTON, SO53 5PD UK")
student_2 = Student("failed", "John", "Conway", "Des-ford Road, LEICESTER, LE194AT UK")
print(student_1.present())
print(student_2.present())

# 2


class Country:
    def __init__(self, cname, continent):
        self.country_name = cname
        self.continent = continent

    def present_c(self):
        return f"{self.country_name}, {self.continent}"


class Brand:
    def __init__(self, b_name, b_st_date):
        self.brand_name = b_name
        self.b_start_date = b_st_date

    def present_b(self):
        return f"{self.brand_name} Company, founded in {self.b_start_date}, produces three different products"


class Season:
    def __init__(self, s_name, average_temp):
        self.season_name = s_name
        self.average_temp = average_temp

    def present_s(self):
        return f"Usually in {self.season_name} average monthly temperatures is {self.average_temp}(°C)"


class Product(Country, Brand, Season):
    def __init__(self, pname, ptype, p_price, p_qnt, cname, continent, b_name, b_st_date, s_name, average_temp):
        super().__init__(cname, continent)
        super().__init__(b_name, b_st_date)
        super().__init__(s_name, average_temp)
        self.prod_name = pname
        self.prod_type = ptype
        self.prod_price = p_price
        self.prod_quant = p_qnt
        self.discount = None
        self.disc_price = None
        self.prod_quant2 = None

    def present_p1(self):
        return f"Meet {self.prod_type} {self.prod_name}, the best chocolate in the world"

    def present_p2(self):
        self.discount = int(input("Discount % \n"))
        self.disc_price = self.prod_price - self.prod_price * self.discount / 100
        return f"{self.present_p1()}. Best price for it is {self.prod_price}$ per unit, but for qnt more, than " \
               f"{self.prod_quant}, you will pay {self.disc_price}$"

    def present_p3(self):
        self.prod_quant2 = random.randint(self.prod_quant + 5, self.prod_quant + 10)
        return f"{self.present_p2()}, for qnt more, than {self.prod_quant2}, you will have additional discount"

    def present_p4(self):
        if self.prod_quant > 1:
            self.prod_quant = random.randint(1, self.prod_quant - 1)
        else:
            self.prod_quant = 1
        return f"The minimal qnt of order is {self.prod_quant}"


my_product = Product("Kit Kat", "Chocolate Wafer Bars", 7, 5, "Switzerland", "all over the world", "Nestle", 1905,
                     "winter", 3)
print(my_product.present_p3())
print(my_product.present_p4())

# 3


class Hotel:
    def __init__(self, h_name, h_place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):
        self.room_type = None
        self.hot_name = h_name
        self.hot_place = h_place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price
        self.booked_room = None
        self.discountT = None
        self.discountH = None
        self.discount_h = None
        self.a = None
        self.b = None

    def present_h(self):
        return f"{self.hot_name} is in {self.hot_place}"

    def booking(self):
        self.booked_room = int(input(f"room N\n"))
        if self.booked_room in self.rooms_mid.keys():
            return {self.rooms_mid[self.booked_room]}
        elif self.booked_room in self.rooms_lux.keys():
            return {self.rooms_lux[self.booked_room]}
        else:
            return "False Room N"

    def available_room_check(self):
        self.room_type = int(input("Mid room: 1 or Luxe room: 2 \n"))
        a = 0
        b = 0
        for i in self.rooms_mid:
            if self.rooms_mid[i] == "free":
              a += 1
        for j in self.rooms_lux:
            if self.rooms_lux[j] == "free":
              b += 1
            if self.room_type == 1:
                return f"{a} Mid rooms"
            elif self.room_type == 2:
                return f"{b} Luxe rooms"

    def discount_h(self):
        self.discount_h = random.randint(2, 10)
        return f"For room orders from Armenia you'll get {self.discount_h} % discount"


class Taxi:
    def __init__(self, taxi_name, car_types, price_for_tour):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = price_for_tour
        self.discount_t = None

    def discount_t(self):
        self.discount_t = random.randint(2, 10)
        return f"For taxi orders from Armenia you'll get {self.discount_t} % discount"

    def taxi_pres(self):
        return f"{self.taxi_pres} taxi service, car type:{self.car_types},price for tour {self.price_for_tour}"


class Tour(Hotel, Taxi):
    def __init__(self, name, price_lux, price_mid, h_name, h_place, rooms_mid, mid_room_price, rooms_lux,
                 lux_room_price, taxi_name , car_types, price_for_tour):
        super().__init__(taxi_name, car_types, price_for_tour, mid_room_price, rooms_lux, lux_room_price)
        super().__init__(h_name, h_place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
        self.tour_name = name
        self.price_lux = price_lux
        self.price_mid = price_mid
        self.price_lux = lux_room_price + price_for_tour
        self.price_mid = mid_room_price + price_for_tour

    def glob_present(self):
        return f"Hello we offer {self.hot_place} tour and we have two options of tour {self.price_lux}$ and " \
               f"{self.price_mid}$, we will stay at {self.hot_name} hotel, which offers two types of rooms: middle " \
               f"{self.mid_room_price}$ and lux {self.lux_room_price}$"


my_first_tour = Tour("Tour to Egypt", 1, 2, "JAZZ", "Egypt", {1: "free", 2: "busy", 3: "free", 4: "busy"}, 10,
                     {5: "free", 6: "busy", 7: "busy", 8: "busy"}, 15, "The Best", "Mercedes", 50)
print(my_first_tour.present_h())
print(my_first_tour.discount_t())
print(my_first_tour.glob_present())
print(my_first_tour.booking())
print(my_first_tour.available_room_check())
