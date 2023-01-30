class Car:
    """Основной класс-родитель"""
    COUNTRIES = ['RU', 'EU', 'JP', 'US']
    ENG_TYPES = ['Diesel', 'Petrol', 'Electrical']

    def __init__(self, region: str, brand: str, eng_type: str):
        self._region = region
        self._brand = brand
        self._eng_type = eng_type

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region not in Car.COUNTRIES:
            raise ValueError("Check car region!")
        self._region = region

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def eng_type(self):
        return self._eng_type

    @eng_type.setter
    def eng_type(self, eng_type):
        if eng_type not in Car.ENG_TYPES:
            raise ValueError("Wrong engine type!")
        self._eng_type = eng_type

    def __str__(self):
        return f"Car region is {self.region}, brand is {self.brand} and engine type is {self.eng_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(region={self.region!r}, brand={self.brand!r}, engine type{self.eng_type!r})"


class Passenger_Car(Car):
    """Класс конструктор для обьектов "легковой автомобиль"."""
    BODY_TYPES = ['wagon', 'coupe', 'sedan']
    SEATS = (2, 4, 5, 7)

    def __init__(self, region: str, brand: str, eng_type: str, body_type: str, seats_num: int):
        super().__init__(region, brand, eng_type)
        self.set_body_type(body_type)
        self.set_seats_num(seats_num)

    def set_body_type(self, body_type):
        if body_type not in Passenger_Car.BODY_TYPES:
            raise ValueError("Check body type for the car")
        self.body_type = body_type

    def set_seats_num(self, seats_num):
        if seats_num not in range(2, 8):
            raise ValueError("Wrong seats num!")
        self.seats_num = seats_num

    @classmethod
    def new_body_type(cls, new_type):
        if new_type not in cls.BODY_TYPES:
            cls.BODY_TYPES.append(new_type)

    @staticmethod
    def speed_converter(value):
        return f"{value} mph = {value * 1.60934} kph"

    def __str__(self):
        return f"Passenger car from {self.region}, brand is {self.brand} and engine type is {self.eng_type}.Body type is " \
               f"{self.body_type} and number of passenger seats is {self.seats_num}"

    def __repr__(self):
        return f"{self.__class__.__name__}(region={self.region!r}, brand={self.brand!r}, engine type={self.eng_type!r}, " \
               f"body_type={self.body_type!r}, seats_num={self.seats_num})"


class Truck(Car):
    """Класс-конструктор для грузового типа"""
    AVALIBLE_CHASSIS = ('4*2', '6*2', '6*4')
    MIN_WEIGHT = 3500
    MAX_WEIGHT = 15000

    def __init__(self, region: str, brand: str, eng_type: str, chassis_type: str, weight: int):
        super().__init__(region, brand, eng_type)
        self.set_chassis_type(chassis_type)
        self.set_max_weight(weight)

    def set_chassis_type(self, chassis_type):
        if chassis_type not in Truck.AVALIBLE_CHASSIS:
            raise ValueError("This type of chassis is not avalible")
        self.chassis_type = chassis_type

    def set_max_weight(self, weight):
        if weight not in range(Truck.MIN_WEIGHT, Truck.MAX_WEIGHT + 1):
            raise ValueError("Wrong value for max weight")
        self.weight = weight

    @classmethod
    def check_max_weight(cls, weight):
        if weight not in range(cls.MIN_WEIGHT, cls.MAX_WEIGHT):
            return f"Car weight not in truck weight range"
        else:
            return f"Truck weight is {cls.MAX_WEIGHT - weight} kg lower then maximum truck weight"

    @staticmethod
    def lbs_to_kg_converter(value):
        return f"{value} lbs = {value * 0.453592} kg"

    def __str__(self):
        return f"Passenger car from {self.region}, brand is {self.brand} and engine type is {self.eng_type}, " \
               f"chassis type is {self.chassis_type}, maximum weight is {self.weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(region={self.region!r}, brand={self.brand!r}, engine type={self.eng_type!r}, " \
               f"chassis_type={self.chassis_type!r}, weight={self.weight!r})"


if __name__ == '__main__':
    car1 = Passenger_Car('GE', 'VAZ', 'gazoline', 'coupe', 7)
    truck1 = Truck('RU', 'MAZ', 'DIESEL', '4*2', 15000)
    print(Truck.lbs_to_kg_converter(2000))
    print(Passenger_Car.speed_converter(40))
    print(Truck.check_max_weight(14000))
    print(Passenger_Car.BODY_TYPES)
