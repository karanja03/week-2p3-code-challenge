class Restaurant:
    restaurants=[]

    def __init__(self, name) :
        self.name=name
        set.review=[] # stored reviews for every restaurant created

        Restaurant.restaurants.append(self)
    
def name(self):
    return self._name

def get_reviews(self):
        return self.reviews
    
def get_customers(self):
    customers = set()
    for review in self.reviews:
     customers.add(review.get_customer())
    return list(customers)

# def average_star_rating(self):
