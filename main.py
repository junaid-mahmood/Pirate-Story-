import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print("""
    📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚
    ╔═══════════════════════════════════╗
    ║    Pirate Story Generator 1.0     ║
    ║    Spin Yer Tale of Adventure     ║
    ╚═══════════════════════════════════╝
    📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚 📚
    """)

def print_scroll():
    print("""
         .--.                   
        /    \              
       /      \        
      /  /~\   \       
     /  /   \   \      
    /  /     \   \     
   /  /       \   \    
  /__/         \___\   
    """)

class PirateStoryGenerator:
    def __init__(self):
        self.saved_stories = []
        self.characters = {
            "Heroes": ["brave captain", "cunning first mate", "mysterious navigator", 
                      "fearless pirate queen", "young cabin boy"],
            "Villains": ["cursed ghost captain", "royal navy admiral", "rival pirate lord",
                        "sea witch", "corrupt governor"],
            "Allies": ["loyal crew", "friendly merchant", "native islanders",
                      "reformed pirate", "mysterious mermaid"]
        }
        self.locations = {
            "Ports": ["Tortuga", "Port Royal", "Nassau", "Singapore", "Havana"],
            "Islands": ["Skull Island", "Treasure Island", "Shipwreck Cove", 
                       "Isla de Muerta", "Devil's Triangle"],
            "Seas": ["Caribbean Sea", "South China Sea", "Mediterranean", 
                    "North Atlantic", "Indian Ocean"]
        }
        self.objectives = {
            "Treasures": ["ancient gold", "cursed jewels", "royal crown", 
                         "magical artifact", "lost city"],
            "Missions": ["revenge against enemies", "proving innocence", 
                        "breaking a curse", "finding lost family", "claiming a throne"],
            "Adventures": ["discovering new lands", "surviving a monster", 
                          "winning a race", "solving a mystery", "leading a rebellion"]
        }

    def generate_story(self):
        clear_screen()
        print_title()
        print_scroll()
        
        print("\n📖 Let's weave a tale of high seas adventure!")
        
        # Character selection
        print("\nChoose yer protagonist:")
        for i, hero in enumerate(self.characters["Heroes"], 1):
            print(f"{i}. The {hero}")
        
        while True:
            hero_choice = input("\nSelect yer hero (1-5): ")
            if hero_choice.isdigit() and 1 <= int(hero_choice) <= 5:
                hero = self.characters["Heroes"][int(hero_choice) - 1]
                break
            print("Invalid choice! Try again, ye scallywag!")

        # Location selection
        print("\nWhere does yer tale begin?")
        for i, (type_name, locations) in enumerate(self.locations.items(), 1):
            print(f"\n{type_name}:")
            for j, location in enumerate(locations, 1):
                print(f"{j}. {location}")
            
        while True:
            location_choice = input("\nSelect yer starting point (1-5): ")
            if location_choice.isdigit() and 1 <= int(location_choice) <= 5:
                location = random.choice(list(self.locations.values()))[int(location_choice) - 1]
                break
            print("Invalid choice! Try again, ye landlubber!")

        # Objective selection
        print("\nWhat be the purpose of this adventure?")
        for i, (type_name, objectives) in enumerate(self.objectives.items(), 1):
            print(f"\n{type_name}:")
            for j, objective in enumerate(objectives, 1):
                print(f"{j}. {objective}")

        while True:
            objective_choice = input("\nSelect yer quest (1-5): ")
            if objective_choice.isdigit() and 1 <= int(objective_choice) <= 5:
                objective = random.choice(list(self.objectives.values()))[int(objective_choice) - 1]
                break
            print("Invalid choice! Try again, ye sea dog!")

        # Generate the story
        villain = random.choice(self.characters["Villains"])
        ally = random.choice(self.characters["Allies"])
        
        story = f"""
        In the treacherous waters near {location}, {hero} embarked on a perilous quest for {objective}.
        The journey seemed promising until {villain} appeared, determined to claim the prize first.
        With the help of {ally}, our hero faced countless challenges and adventures.
        
        Through storms and battles, betrayals and alliances, the tale of {hero} became legend.
        Some say the quest for {objective} changed the very fate of {location} forever.
        
        And so the legend lives on, told in every port from here to the edge of the map...
        """
        
        self.saved_stories.append(story)
        
        print("\n📜 Here's yer tale of adventure:")
        print(story)
        
        return story

    def save_story(self, story):
        with open('pirate_stories.txt', 'a') as f:
            f.write(f"{story}\n{'='*50}\n")
        print("\n💾 Tale recorded in the ship's log! (pirate_stories.txt)")

def main():
    generator = PirateStoryGenerator()
    
    while True:
        clear_screen()
        print_title()
        print_scroll()
        
        print("\n⚓ Choose yer path:")
        print("1. 📖 Generate New Story")
        print("2. 💾 Save Last Generated Story")
        print("3. 📜 View Story History")
        print("4. 🚪 Close the Book (Exit)")
        
        choice = input("\nEnter yer choice (1-4): ")
        
        if choice == '1':
            generator.generate_story()
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            if generator.saved_stories:
                generator.save_story(generator.saved_stories[-1])
            else:
                print("\n❌ No stories generated yet! Create one first!")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            if generator.saved_stories:
                print("\n📜 Your tales of adventure:")
                for i, story in enumerate(generator.saved_stories, 1):
                    print(f"\nTale {i}:{story}")
            else:
                print("\n📜 No stories written yet!")
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            print("\nUntil our next tale, farewell!")
            break
        
        else:
            print("Blimey! That's not a valid choice!")
            input("Press Enter to try again...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nClosing the story book! Fair winds, storyteller! 📚") 
