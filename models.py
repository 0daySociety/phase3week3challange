from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker, relationship,declarative_base
from seed import session




Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')
   
    def full_review(self):
      
        return f"Reviews for {self.restaurant.name} by {self.customer.full_name()} got  {self.star_rating} stars."
    
    



class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        print(f"{self.first_name}  {self.last_name}")

    def favorite_restaurant(self):
       
        from sqlalchemy import func

        subquery = (
            session.query(Review.restaurant_id, func.max(Review.star_rating).label("max_rating"))
            .filter(Review.customer_id == self.id)
            .group_by(Review.restaurant_id)
            .subquery()
        )

        favorite_restaurant_id = (
            session.query(subquery.c.restaurant_id)
            .filter(subquery.c.max_rating == func.max(subquery.c.max_rating))
            .scalar()
        )

        favorite_restaurant = session.query(Restaurant).get(favorite_restaurant_id)

        return favorite_restaurant

    def add_review(self, restaurant, rating):
    
        review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
      
        session.query(Review).filter(Review.customer == self, Review.restaurant == restaurant).delete()
        session.commit()


        



class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key=True) 
    price = Column(Integer())
    name = Column(String())
    reviews = relationship('Review', back_populates='restaurant')

    def fanciest(cls):
      return session.query(Restaurant).order_by(Restaurant.price.desc()).first()
     

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]




