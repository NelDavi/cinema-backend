# configuration de la base de données
from sqlalchemy import  create_engine
from sqlalchemy.orm import  declarative_base
from sqlalchemy.orm import  sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./cinema.db"


# création d'un moteur de base de données (engine) qui 
# établit la connexion avec notre base SQLite(movies.db)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #gestion du multi threading
)


# définir SessionLocal, qui permet de créer des sessions pour 
# intéragir avec la base de données

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

# définir Base, qui servire de classe de base pour nos modèles SQLAlchemy
Base = declarative_base()


if __name__== "__main__":
    try:
        with engine.connect() as conn:
            print("connexion à la database réussie")
    except Exception as e:
        print(f"Erreur lors de la connexion à la database: {e}")
