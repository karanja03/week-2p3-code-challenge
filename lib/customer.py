
    

from review import Review  

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name  
        self._family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def set_given_name(self, given_name):
        self._given_name = given_name

    def family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        self._family_name = family_name

    def full_name(self):
        return f"{self._family_name} {self._given_name}"

    def get_reviews(self):
        return self.reviews

    def get_restaurants(self):
        restaurants = set()
        for review in self.reviews:
            restaurants.add(review.restaurant())
        return list(restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            full_name = customer.full_name()
            if full_name == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer._given_name == name:
                matching_customers.append(customer)
        return matching_customers

    @classmethod
    def all(cls):
        return cls.all_customers

customer1 = Customer("Wambui", "karanja")
customer2 = Customer("Enoch", "Njoroge")
customer3 = Customer("John", "kariuki")

found_customer = Customer.find_by_name("John kariuki")
if found_customer:
    print(f"Found: {found_customer.full_name()}")
else:
    print("Customer not found")

all_johns = Customer.find_all_by_given_name("Enoch")
for customer in all_johns:
    print(f"Found: {customer.full_name()}")

