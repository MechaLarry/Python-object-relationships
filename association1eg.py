# person class definition
class Person:
    def _init_(self, name):
        self.name = name

# address class definition
class Address:
    def _init_(self, city):
        self.city = city

# person and adress class
class PersonAddress:
    def _init_(self, person, address):
        self.person = person
        self.address = address

# create instances here
person = Person("Aleph")
address = Address("United Kingdom, Manchester")
person_address = PersonAddress(person, address)

print(person_address.person.name) # output person input
print(person_address.address.city) # output adress input