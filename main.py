"""
Name(s): Tiffany Xue
Name of Project: House of Cards
""" 

def start():
  print("Welcome! A willing visitor to the House of Cards, are you?No? You fell down here? Ah, that's quite unfortunate, because you can't leave just yet. That wouldn't be any fun, would it? Oh,look... what's over there?")
  print("You see a bottle labeled DRINK ME. Do you drink it?")
  choice = input("Enter Y to drink and N to not: ")
  if choice == "Y":
    drink()
  elif choice == 'B':
    notdrink()

def drink():
  print("After drinking a mysterious liquid, you have shrunk to the size of a quarter. Then, you see a cake labeled EAT ME. Do you eat it?")
  choice = input("Enter Y to eat and N to not: ")
  if choice == "Y":
    eat()
  elif choice == 'B':
    noteat()

def eat():
  print("After eating the cake, you have inflated to the size of a house. It is impossible for you to move, but you see Mad Hatter not far away. Do you call for help?")
  choice = input("Enter Y to call and N to not: ")
  if choice == "Y":
    call()
  elif choice == 'B':
    notcall()

def call():
  print("After calling for help, Mad Hatter comes over. He looks slightly crazed, and his pocketwatch is visibly broken. Do you ask him if he's all right?")
  choice = input("Enter Y to ask and N to not: ")
  if choice == "Y":
    ask()
  elif choice == 'B':
    notask()

def ask():
  print("After asking, Mad Hatter looks very annoyed. He approaches you with a knife. Maybe we'll see you in your next dream?")

def notask():
  print("After staying silent, Mad Hatter looks at you and shrugs before leaving. That's too bad! There's nobody else around. Maybe we'll see you in your next dream, though?")

def notcall():
  print("After staying silent, two days have passed since you became trapped in the house. There is nothing you can do now. Farewell! Maybe we'll see you in your next dream, though?")

def noteat():
  print("After deciding not to eat it, you decide to place the cake on the ground for birds to eat. However, you return to see Caterpillar eating it. Do you sit down and talk to him?")
  choice = input("Enter Y to sit down and talk and N to not: ")
  if choice == "Y":
    sit()
  elif choice == 'B':
    notsit()

def sit():
  print("After sitting down and talking to Caterpillar. He tells you to eat a mushroom to satisfy your hunger. Do you eat it?")
  choice = input("Enter Y to eat it and N to not: ")
  if choice == "Y":
    shroom()
  elif choice == 'B':
    notshroom()

def shroom():
  print("Caterpillar laughs. The mushroom is poisonous! Didn't think you'd be fooled so easily... how sad. Maybe we'll see you in your next dream, though?")

def notshroom():
  print("Caterpillar is not happy. Nobody rejects his offers. He forces you to swallow the mushroom. You should know it's poisonous, so maybe say your farewells? Nice try, though. Maybe we'll see you in your next dream?")

def notsit():
  print("Caterpillar is not happy about the silent treatment, and is heading towards you with a spear. That's unfortunate. Maybe we'll see you in your next dream, though?")


def notdrink():
  print("After throwing the bottle away, suddenly, Cheshire Cat appears. Do you greet it?")
  choice = input("Enter Y to greet and N to not: ")
  if choice == "Y":
    greet()
  elif choice == 'B':
    notgreet()

def greet():
  print("After greeting Cheshire Cat, it sits down next to you. It is decidedly not leaving you, but you must find something to eat soon. Do you take it with you?")
  choice = input("Enter Y to take it with you and N to not: ")
  if choice == "Y":
    take()
  elif choice == 'B':
    nottake()

def take():
  print("After taking Cheshire Cat with you, it continues to grin nonstop. Suddenly, it sees Mouse and beings chasing. Do you chase after it?")
  choice = input("Enter Y to chase after it and N to not: ")
  if choice == "Y":
    chase()
  elif choice == 'B':
    notchase()

def chase():
  print("Baited! Cheshire Cat and Mouse are best friends, and have lured you to the edge of a cliff. It is either jump or be viciously attacked. What a sad turn of events. Maybe we'll see you in your next dream, though?")

def notchase():
  print("You are now alone. Suddenly, your vision starts turning hazy... was it all a dream?")

def nottake():
  print("After deciding to leave Cheshire Cat, you notice a flock of birds in its place. You are in their space, but you're so tired. Do you move?")
  choice = input("Enter Y to move and N to not: ")
  if choice == "Y":
    move()
  elif choice == 'B':
    notmove()

def move():
  print("After deciding to move, you stumble upon Dormouse. It is purple, and looks sickly. Do you help it?")
  choice = input("Enter Y to help and N to not: ")
  if choice == "Y":
    aid()
  elif choice == 'B':
    notaid()

def aid():
  print("Nothing's wrong with Dormouse. It is very angry though. See all those sharp teeth coming at you? Not sure if anyone can help you now. Nice try. Maybe we'll see you in your next dream, though?")

def notaid():
  print("How incompassionate you are! Dormouse is throwing a fit a rage. Good luck fending him off. Share how many times you were bitten afterwards! Maybe we'll see you in your next dream?")

def notmove():
  print("You're in their way, and they're not happy about it. Good luck fending off a flock of metal-beaked birds. All the best, really. Maybe we'll see you in your next dream, though?")

def notgreet():
  print("After ignoring Cheshire Cat, its grin fades. It scratches you on the face, making you bleed. Do you search for something to relieve it?")
  choice = input("Enter Y to search and N to not: ")
  if choice == "Y":
    search()
  elif choice == 'B':
    notsearch()

def search():
  print("After searching for herbs, you stumble across a patch of purple flowers. They look like they'll help. Do you eat them?")
  choice = input("Enter Y to eat and N to not: ")
  if choice == "Y":
    herb()
  elif choice == 'B':
    notherb()

def herb():
  print("Aw. Who knew flowers could be poisonous? Unfortunate, really. Maybe we'll see you in your next dream?")

def notherb():
  print("It got infected? Oh, come on, what did you expect? Too good... Maybe we'll see you in your next dream?")

def notsearch():
  print("After deciding not to search for herbs, you see March Hare from a distance. Maybe he'll have some tea for you to drink. Do you call him over?")
  choice = input("Enter Y to call and N to not: ")
  if choice == "Y":
    hare()
  elif choice == 'B':
    nothare()

def hare():
  print("March Hare looks deranged because he is. Who knows what the Queen of Hearts can do? Oh well. Best of luck fighting him. (You're not going to win.) Maybe we'll see you in your next dream?")

def nothare():
  print("You're thirsty? Aw, come on! You can push through the fourth day. Trust... or not. Doesn't matter. Maybe we'll see you in your next dream?")

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
