import datetime
class Date():
    def __init__(self, _day, _month, _year):
        self.day = _day
        self.month = _month
        self.year = _year
class Traveller():
    def __init__(self, _surname_and_initials, _profession,_day_of_birth, _month_of_birth, _year_of_birth):
        self.surname_and_initials = _surname_and_initials
        self.profession = _profession
        self.day_of_birth = Date
        self.adress = Adress_of_traveller

class Adress_of_traveller():
    def __init__(self, _country, _region, _city_or_village, _street, _house, _term, _date):
        self.country = _country
        self.region = _region
        self.city_or_village = _city_or_village
        self.street = _street
        self.house = _house
        self.term = _term
        self.info = Traveller
    def get_terms(self):
        allowed_to_stay = int(input('enter days of staying = '))
        current = datetime.datetime.today()
        terms = current - self.term
        if terms < allowed_to_stay:
            return "can stay"
        def get_rest(self):
            return allowed_to_stay - terms








