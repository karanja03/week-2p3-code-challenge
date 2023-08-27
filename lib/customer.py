from review import Review



class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews=[] # stores the reviews of that particular client that has been initialized and added
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def set_givenname(self, given_name):
        self.given_name = given_name

    def familyname(self):
        return self.family_name

    def set_familyname(self, family_name):
        self.family_name = family_name

    def fullname(self):
        return f"{self.given_name} {self.family_name}"
    
    def get_reviews(self):
        return self.reviews
    
      
    def get_restaurants(self):# to gives a list of restaurants a client given reviews to
        restaurants = set() # created an empty set of resturants ensuring each restuarnt reviewed by a client is unique
        for review in self.reviews:#check and iterate all reviews amde by this client
            restaurants.add(review.get_restaurant())
        return list(restaurants)

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)# tis two lines link back to he new custoer that hass been created and takes the review associated with the customer and it append the new review to the list of reveiws a client has made
        restaurant.reviews.append(review)

    def  num_reviews(self):
        return len(self.reviews)
    # to be completed
    def find_by_name(self,name):
        self.name=full_name()



    @classmethod
    def all(cls):
        return cls.all_customers
    
    
