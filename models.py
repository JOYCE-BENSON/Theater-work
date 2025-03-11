
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    character_name = Column(String())
    
    # Establish one-to-many relationship with Audition
    auditions = relationship('Audition', back_populates='role')
    
    def actors(self):
        """Returns a list of names from the actors associated with this role."""
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        """Returns a list of locations from the auditions associated with this role."""
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        """Returns the first instance of the audition that was hired for this role."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if hired_auditions:
            return hired_auditions[0]
        return 'no actor has been hired for this role'
    
    def understudy(self):
        """Returns the second instance of the audition that was hired for this role."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) >= 2:
            return hired_auditions[1]
        return 'no actor has been hired for understudy for this role'


class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer, primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    # Establish many-to-one relationship with Role
    role = relationship('Role', back_populates='auditions')
    
    def call_back(self):
        """Changes the hired attribute to True."""
        self.hired = True


# Create like an engine for database connection
engine = create_engine('sqlite:///moringa_theater.db')

# Create a session factory
Session = sessionmaker(bind=engine)