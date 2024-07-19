"""
Mad Libs is a word game where you replace words with different 
categories (noun, verb, adjective, etc.) to create a 
funny or nonsensical story.
Based on "12 Beginner Python Projects - Coding Course" Youtube video
"""

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
