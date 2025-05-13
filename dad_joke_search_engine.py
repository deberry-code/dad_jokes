import requests
link="https://icanhazdadjoke.com/search"
response = requests.get(link, headers={'Accept':'application/json'},
params = {'term':'dog', 'limit':1})
data=response.json()

topic=input("Let me find you a joke! Enter a search term: ")
jokeset=requests.get("https://icanhazdadjoke.com/search",headers={"Accept": "application/json"},params={"term": topic}).json()
from random import choice
answers=jokeset["results"]
total_jokes=jokeset["total_jokes"]

jokelist = [j["joke"] for j in answers]

def tell_joke(jokelist):
    if not jokelist:
        print(f"That was my last joke about {topic}!\n")
        return False
    x = choice(jokelist)
    print(f"\n{x}\n")
    jokelist.remove(x)
    return True


if total_jokes > 1:
    print(f"I've got {total_jokes} jokes about {topic}. Here's one:")
    still_joking = tell_joke(jokelist)
    while still_joking:
        loop = input("Would you like another one? (Y/N): ")
        if loop.upper() == "Y":
            still_joking = tell_joke(jokelist)
        else:
            print("Thanks for playing!")
            break

elif total_jokes == 1:
    print(f"I've got one joke about {topic}. Here it is:\n{answers[0]['joke']}")
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again!")

