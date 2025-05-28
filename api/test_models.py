from database import SessionLocal
from models import Movie, Link, Rating, Tag

db = SessionLocal()


# test la récupération de quelques films

# movies = db.query(Movie).limit(10).all()

# for movie in movies:
#     print(f"Titre:{movie.title}, ID: ({movie.movieId})")
    
    

# # test la récupération de quelques liens
# links = db.query(Link).limit(10).all()

# for link in links:
#     print(f"ID: ({link.movieId}), IMDB: {link.imdbId}, TMDB: {link.tmdbId}")


# # test la récupération de quelques notes
ratings = db.query(Rating).limit(10).all()

for rating in ratings:
    print(f"ID: ({rating.movieId}), Note: {rating.rating}, Timestamp: {rating.timestamp}")