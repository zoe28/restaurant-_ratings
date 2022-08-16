"""Restaurant rating lister."""
"""Restaurant rating lister."""

def reading_the_file(file_name):
    """reading_the_file is displaying rating in alphabeted order by restaurant name"""
    score_file = open(file_name)
    ratings = {}
    
    for line in score_file:
        line = line.rstrip()
        tokenized = line.split(":")  
        name, rating = tokenized

        ratings[name] = rating

    sorted_ratings = {key: value for key, value in sorted(ratings.items())}
    
    for name, rating in sorted_ratings.items():
        print(f"{name} is rated at {rating}")

    return sorted_ratings


def add_rating(ratings):
    """add_rating allows user to give restaurant ratings"""

    restaurant_name = input("What restaurant would you like to rate? ")
    restaurant_rating = input("What's your rating? ")

    ratings[restaurant_name] = restaurant_rating

    ratings = {key: value for key, value in sorted(ratings.items())}

    for name, rating in ratings.items():
        print(f"{name} is rated at {rating}")
        
    return ratings
    
add_rating(reading_the_file("scores.txt"))


# put your code here
