# ISSUE 75
#
# Problem:
# Write a program that accepts a list of movie records containing title, genre and rating and calculates the average rating for every genre, rounded to one decimal place. A genre with only a single movie is not a meaningful average, so leave those genres out of the result.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def genre_ratings(movies):
    totals, counts = {}, {}
    for movie in movies:
        genre, rating = movie["genre"], movie["rating"]
        # TODO: Check how ratings are accumulated per genre.
        totals[genre] = totals.get(genre,0) + movie["rating"]
        counts[genre] = counts.get(genre, 0) + 1
    # TODO: Check the divisor used to calculate each genre average.
    # TODO: Check how many decimal places the result should keep.
    averages = {genre: round(total / (counts[genre]), 1) for genre, total in totals.items()}
    # TODO: Check which genres have too few movies to be included.
    print({genre: average for genre, average in averages.items() if counts[genre] > 1})
    return {genre: average for genre, average in averages.items() if counts[genre] > 1}

def check_solution():
    movies = [
        {"title":"A","genre":"comedy","rating":5},{"title":"B","genre":"comedy","rating":4},
        {"title":"C","genre":"comedy","rating":3},{"title":"D","genre":"horror","rating":2},
        {"title":"E","genre":"horror","rating":5},{"title":"F","genre":"drama","rating":4},
    ]
    assert genre_ratings(movies) == {"comedy":4.0,"horror":3.5}
    assert genre_ratings([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
