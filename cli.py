
from models import Session, Role, Audition

def main():
    session = Session()
    
    while True:
        print("\nMoringa Theater Company Auditions")
        print("1. List all roles")
        print("2. List all auditions")
        print("3. View role details")
        print("4. Schedule an audition")
        print("5. Call back an actor")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            roles = session.query(Role).all()
            print("\nAvailable Roles:")
            for role in roles:
                print(f"{role.id}. {role.character_name}")
        
        elif choice == "2":
            auditions = session.query(Audition).all()
            print("\nScheduled Auditions:")
            for audition in auditions:
                status = "Hired" if audition.hired else "Not Hired"
                print(f"{audition.id}. {audition.actor} for {audition.role.character_name} at {audition.location} - {status}")
        
        elif choice == "3":
            role_id = input("Enter role ID: ")
            role = session.query(Role).filter_by(id=role_id).first()
            
            if role:
                print(f"\nRole: {role.character_name}")
                print(f"Actors who auditioned: {', '.join(role.actors())}")
                print(f"Audition locations: {', '.join(role.locations())}")
                
                lead = role.lead()
                if isinstance(lead, Audition):
                    print(f"Lead actor: {lead.actor}")
                else:
                    print(f"Lead actor: {lead}")
                
                understudy = role.understudy()
                if isinstance(understudy, Audition):
                    print(f"Understudy: {understudy.actor}")
                else:
                    print(f"Understudy: {understudy}")
            else:
                print("Role not found.")
        
        elif choice == "4":
            roles = session.query(Role).all()
            print("\nAvailable Roles:")
            for role in roles:
                print(f"{role.id}. {role.character_name}")
            
            role_id = input("Enter role ID: ")
            actor_name = input("Enter actor name: ")
            location = input("Enter audition location: ")
            phone = input("Enter actor phone: ")
            
            role = session.query(Role).filter_by(id=role_id).first()
            if role:
                new_audition = Audition(
                    actor=actor_name,
                    location=location,
                    phone=int(phone),
                    role=role
                )
                session.add(new_audition)
                session.commit()
                print("Audition scheduled successfully!")
            else:
                print("Role not found.")
        
        elif choice == "5":
            audition_id = input("Enter audition ID to call back: ")
            audition = session.query(Audition).filter_by(id=audition_id).first()
            
            if audition:
                audition.call_back()
                session.commit()
                print(f"{audition.actor} has been called back (hired) for the role of {audition.role.character_name}!")
            else:
                print("Audition not found.")
        
        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()