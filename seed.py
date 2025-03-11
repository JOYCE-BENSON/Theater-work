
from models import Session, Role, Audition

def seed_database():
    session = Session()
    
    # To be able to delete existing data
    session.query(Audition).delete()
    session.query(Role).delete()
    
    # Create roles
    hamlet = Role(character_name="Hamlet")
    ophelia = Role(character_name="Ophelia")
    gertrude = Role(character_name="Gertrude")
    
    # Add roles to session
    session.add_all([hamlet, ophelia, gertrude])
    session.commit()
    
    # Create auditions
    auditions = [
        Audition(actor="John Smith", location="Main Stage", phone=5551234, role=hamlet),
        Audition(actor="Emily Johnson", location="Room 101", phone=5555678, role=hamlet),
        Audition(actor="Sarah Williams", location="Main Stage", phone=5559876, role=ophelia),
        Audition(actor="Jessica Brown", location="Room 102", phone=5554321, role=ophelia),
        Audition(actor="Michael Davis", location="Main Stage", phone=5552468, role=gertrude),
    ]
    
    # Add auditions to session
    session.add_all(auditions)
    session.commit()
    
    # Callback some auditions that may qualify (hire them)
    auditions[0].call_back()  # John Smith as Hamlet (lead)
    auditions[1].call_back()  # Emily Johnson as Hamlet (understudy)
    auditions[2].call_back()  # Sarah Williams as Ophelia
    
    session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()