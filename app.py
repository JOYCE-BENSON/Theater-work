
from models import Base, engine
import os

def init_db():
    # Create database tables according to model definitions
    Base.metadata.create_all(engine)
    print("Database initialized.")

if __name__ == "__main__":
    # Check if database exists and if does not exist then initialize it
    if not os.path.exists('moringa_theater.db'):
        init_db()
    
    # Run CLI interface
    from cli import main
    main()
