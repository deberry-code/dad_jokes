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
jokelist=[]
def fetchjoke():
    for i in answers:
        j=i['joke']
        jokelist.append(j)
    x=choice(jokelist)
    print(f"\nI've got {len(jokelist)} jokes about {topic}. Here's one: ",x,'\n')
    jokelist.pop(jokelist.index(x))
    return jokelist

def keepgoing():
  newjoke=choice(jokelist)
  pos=jokelist.index(newjoke)
  jokelist.pop(pos)
  print('\n',newjoke, '\n')
  b=len(jokelist)
  loop=input("Would you like another one? ")
  if loop.upper()=='N':
     print(f'Thanks for playing!')
  if b==1:
    print('\n', jokelist[0],'\n')
    print(f"That was my last joke about {topic}!\n")
    return
  else: return jokelist, loop, b

if total_jokes > 1:
  fetchjoke()
  print(f'Would you like another one? ')
  loop=input("Y/N:")
  if loop.upper()=="Y":
   keepgoing()
  elif loop.upper()=="N":
     print(f'Thanks for playing!')
  else: print(f'Thanks for playing!')



elif total_jokes == 1:
    print(f"I've got one joke about {topic}. Here it is: ",(answers[0]['joke']).strip())
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")