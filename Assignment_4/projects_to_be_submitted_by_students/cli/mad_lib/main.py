print("Welcome to the Personalized Mad Libs Game! Fill in the blanks to create a story about yourself.")
name= input("Enter your name: ")
age= input("Enter your age: ")
hobby= input("Enter your hobby: ")
personality= input("Describe your personality in one word: ")
fav_place= input("Enter your favorite where you often like to visit: ")
dream_job= input("Enter your dream job: ")

story = (f"Meet {name}, a {age}-year-old who is {personality} and loves {hobby}. "
             f"Whenever {name} gets free time, they enjoy visiting {fav_place}. "
             f"In the future, {name} dreams of becoming a {dream_job}. The journey ahead is full of excitement!")

print("\n Here is your story: ")
print(story)
