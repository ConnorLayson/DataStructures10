class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}
    
    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
    
    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print(f"Error: One or both cities don't exist!")
    
    def print_network(self): 
        for person_name, person_obj in self.people.items():
            connection_names = [c.name for c in person_obj.friends]
            
            connected_people = ", ".join(connection_names)
            print(f"{person_name} connects to: {connected_people}")

network = SocialNetwork()

network.add_person("Mark Bishop")
network.add_person("Dylan Jude")
network.add_person("Gabriel Clark")
network.add_person("Sloppy Jaboppy")
network.add_person("Link LegendOfZelda")
network.add_person("Pedro Pooptooth")
network.add_person("Aunt Jemima")
network.add_person("Ella Grace")

network.add_friendship("Dylan Jude", "Pedro Pooptooth")
network.add_friendship("Dylan Jude", "Sloppy Jaboppy")
network.add_friendship("Dylan Jude", "Mark Bishop")
network.add_friendship("Gabriel Clark", "Mark Bishop")
network.add_friendship("Gabriel Clark", "Dylan Jude")
network.add_friendship("Gabriel Clark", "Pedro Pooptooth")
network.add_friendship("Gabriel Clark", "Aunt Jemima")
network.add_friendship("Mark Bishop", "Sloppy Jaboppy")
network.add_friendship("Sloppy Jaboppy", "Link LegendOfZelda")
network.add_friendship("Ella Grace", "Ella Grace")

network.print_network()