# phase3week3challange
Phase 3 Code Challenge: Restaurants
Overview
This code challenge focuses on building a system for restaurant reviews. We have three main models: Restaurant, Review, and Customer. The relationships between these models include:

A Restaurant has many Reviews.
A Customer has many Reviews.
A Review belongs to both a Restaurant and a Customer.
The challenge covers a range of topics, including SQLAlchemy Migrations, SQLAlchemy Relationships, Class and Instance Methods, and SQLAlchemy Querying.

Instructions
Setting up the Environment

Make sure you have SQLAlchemy installed in your environment:

Copy code
pip install SQLAlchemy
Database Models and Migrations

Define the database models for Restaurant, Customer, and Review.
Create migrations for these models to set up the database schema.
Use the seeds.py file to populate the database with sample data for testing.
Object Relationship Methods

Implement the following methods in the respective classes:
In the Review class:
Review customer(): Returns the Customer instance for this review.
Review restaurant(): Returns the Restaurant instance for this review.
In the Restaurant class:
Restaurant reviews(): Returns a collection of all the reviews for the restaurant.
Restaurant customers(): Returns a collection of all the customers who reviewed the restaurant.
In the Customer class:
Customer reviews(): Returns a collection of all the reviews left by the customer.
Customer restaurants(): Returns a collection of all the restaurants reviewed by the customer.
Aggregate and Relationship Methods

In the Customer class:
Customer full_name(): Returns the full name of the customer in Western style (concatenating first name and last name).
Customer favorite_restaurant(): Returns the restaurant instance that has the highest star rating from this customer.
Customer add_review(restaurant, rating): Takes a restaurant (an instance of the Restaurant class) and a rating and creates a new review for the restaurant with the given restaurant_id.
Customer delete_reviews(restaurant): Takes a restaurant (an instance of the Restaurant class) and removes all their reviews for this restaurant by deleting rows from the reviews table.
In the Review class:
Review full_review(): Returns a string formatted as "Review for {restaurant name} by {customer's full name}: {review star rating} stars."
In the Restaurant class (class method):
Restaurant fanciest(): Returns one restaurant instance for the restaurant that has the highest price.
Restaurant all_reviews(): Returns a list of strings with all the reviews for this restaurant, formatted as specified.
