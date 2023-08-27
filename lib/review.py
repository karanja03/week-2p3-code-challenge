class Review:
    reviews=[]

    def __init__(self, customer, restaurant, rating):
        self.customer= customer
        self.restaurant=restaurant
        self.rating= rating

        Review.review.append(self)

    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
        