import random

class Taksopark:
    def __init__(self, title):
        self.title = title
        self.balance = 0
        self.cars = []
        self.safarlar = []

class Car:
    def __init__(self, raqami, driver_name, reyting):
        self.raqami = raqami
        self.driver_name = driver_name
        self.reyting = reyting
        self.balance = 0

class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.cards = []

class Card:
    def __init__(self, number, muddat, password, owner, balance):
        self.number = number
        self.muddat = muddat
        self.password = password
        self.owner = owner
        self.balance = balance

class Safar:
    def __init__(self, client_phone, car_number, qayerdan, qayerga, distance):
        self.client_phone = client_phone
        self.car_number = car_number
        self.qayerdan = qayerdan
        self.qayerga = qayerga
        self.distance = distance

if __name__ == "__main__":
    my_taksopark = Taksopark("Arzon Taksopark")

    my_taksopark.cars = [
        Car(1111, "Driver1", "Economy"),
        Car(2222, "Driver2", "Comfort"),
        Car(3333, "Driver3", "Business"),
        Car(4444, "Driver4", "Economy"),
        Car(5555, "Driver5", "Comfort"),
        Car(6666, "Driver6", "Business"),
        Car(7777, "Driver7", "Economy"),
        Car(8888, "Driver8", "Comfort"),
        Car(9999, "Driver9", "Business"),
        Car(1010, "Driver10", "Economy"),
        Car(1011, "Driver11", "Comfort"),
        Car(1212, "Driver12", "Business"),
        Car(1313, "Driver13", "Economy"),
        Car(1414, "Driver14", "Comfort"),
        Car(1515, "Driver15", "Business")
    ]

    clients = [
        Client("+998901111010"),
        Client("+998902222020"),
        Client("+998903333030"),
        Client("+998904444040"),
        Client("+998905555050")
    ]

    cards = [
        Card("860012341", "12/25", "1111", "Ayub", 100000),
        Card("860012342", "12/25", "2222", "Ayub", 150000),
        Card("860012343", "12/25", "3333", "Sherzod", 120000),
        Card("860012344", "12/25", "4444", "Sherzod", 140000),
        Card("860012345", "12/25", "5555", "Yusuf", 130000),
        Card("860012346", "12/25", "6666", "Yusuf", 160000),
        Card("860012347", "12/25", "7777", "Ali", 110000),
        Card("860012348", "12/25", "8888", "Ali", 170000),
        Card("860012349", "12/25", "9999", "Azizxon", 180000),
        Card("860012350", "12/25", "1010", "Azizxon", 190000)
    ]

    # Har bir klientga ikkita karta qo'shamiz
    for i, client in enumerate(clients):
        client.cards.append(cards[i*2])
        client.cards.append(cards[i*2 + 1])

    client_phone = input("Telefon raqamingizni kiriting: ")
    client = next((c for c in clients if c.phone_number == client_phone), None)

    if client:
        qayerdan = input("Qayerdan: ")
        qayerga = input("Qayerga: ")
        distance = random.randint(1, 20)  # Masofa random orqali aniqlanadi

        # Moshina biriktiriladi
        car = random.choice(my_taksopark.cars)
        print(f"Sizga biriktirilgan moshina: {car.raqami}, haydovchi: {car.driver_name}")

        narx = distance * 10000  # 1 km = 10,000 so'm
        print(f"Umumiy masofa: {distance} km. To'lov: {narx} so'm.")

        selected_card = client.cards[0]  # Default birinchi karta tanlanadi

        if selected_card.balance >= narx:
            selected_card.balance -= narx
            park_share = narx * 0.2
            car_share = narx * 0.8

            my_taksopark.balance += park_share
            car.balance += car_share

            print(f"To'lov amalga oshirildi! Taksopark ulushi: {park_share} so'm, Moshina ulushi: {car_share} so'm.")

            # Safarni saqlaymiz
            safar = Safar(client_phone, car.raqami, qayerdan, qayerga, distance)
            my_taksopark.safarlar.append(safar)
        else:
            print("Karta balansida mablag' yetarli emas!")
    else:
        print("Bunday raqam bilan ro'yxatdan o'tgan klient topilmadi!")
