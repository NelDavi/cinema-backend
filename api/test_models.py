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
# ratings = db.query(Rating).limit(10).all()

# for rating in ratings:
#     print(f"ID: ({rating.movieId}), Note: {rating.rating}, Timestamp: {rating.timestamp}")


#récupération de 10 films avec une note supérieur ou égale à 4
# films_bien_note = db.query(Movie.title, Rating.rating).join(Rating).filter(Rating.rating >= 4).limit(10).all()


# for film in films_bien_note:
#     print(f"Titre: {film.title}, Note: {film.rating}")



# récupération des tags associés aux films

# tags_associe_films = db.query(Movie.title, Tag.tag).join(Tag).limit(10).all()

# for tag in tags_associe_films:
#     print(f"Titre: {tag.title}, Tag: {tag.tag}")


# récupération des liens associés aux films

liens_associe_films = db.query(Movie.title, Link.imdbId, Link.tmdbId).join(Link).limit(5).all()

for lien in liens_associe_films:
    print(f"Titre: {lien.title}, IMDB: {lien.imdbId}, TMDB: {lien.tmdbId}")

