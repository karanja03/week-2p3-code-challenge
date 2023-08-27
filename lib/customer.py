  
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def set_givenname(self, given_name):
        self._given_name = given_name

    def familyname(self):
        return self._family_name

    def set_familyname(self, family_name):
        self._family_name = family_name

    def fullname(self):
        return f"{self._given_name} {self._family_name}"
    
    def get_reviews(self):
        return self.reviews
    
      
    def get_restaurants(self):
        restaurants = set()
        for review in self.reviews:
            restaurants.add(review.get_restaurant())
        return list(restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.reviews.append(review)


    @classmethod
    def all(cls):
        return cls.all_customers
