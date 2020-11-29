import os
import random

gif_links = [
    "https://tenor.com/view/crab-rave-dancing-dancing-crab-gif-16543314",
    "https://tenor.com/view/disco-crab-dancing-crab-crab-party-gif-16543317",
    "https://tenor.com/view/crab-dancing-crab-party-rave-cool-moves-gif-15701153",
    "https://tenor.com/view/bikini-bodhi-crab-rave-crab-dance-gif-15172853",
    "https://tenor.com/view/futurama-zoidberg-dance-crab-happy-gif-4568258",
    "https://tenor.com/view/zoidberg-naked-wiggle-laugh-futurama-gif-5382440",
    "https://tenor.com/view/kekcrab-crabkek-crabkekw-kekwceab-crab-gif-19258334",
    "https://tenor.com/view/krabby-pokemon-pokemongo-crab-crab-dance-gif-17755646",
    "https://tenor.com/view/headcrab-half-life-funny-alyx-spin-gif-17864567",
    "https://tenor.com/view/headcrab-half-life-half-life-alyx-afraid-gaming-gif-17329251"
]

facts = [
"There are more than 4,500 species of crabs.",
"Most species live in coastal areas of salty, fresh or brackish water.",
"Crabs are super old! They showed up during the Jurassic period, 200 million years ago.",
"The Pea Crab is the smallest known species. It measures between 0.27 and 0.47 inches long.",
"The Japanese Spider Crab is the biggest, measuring about 12 feet between its claws!",
"Crabs have an “exoskeleton” made of chitin. It protects their soft tissue.",
"Crabs walk and swim sideways.",
"Crabs eat both meat and plants, making them omnivores.",
"Pregnancy in female crabs only last one or two weeks. Then they lay between 1,000 and 2,000 eggs!",
"Groups of crabs living together are known as “casts.”",
"The average lifespan of a crab is 3 to 4 years.",
"Both crabs and lobsters are decapods, or crustaceans with 10 legs. Other decapods include crayfish, prawns, and shrimp.",
"While lobsters have a long, segmented abdomen that sticks out at the back of their bodies, crabs have a similar but smaller abdomen that is curled up underneath the main shell.",
"Most crabs have flat bodies that enable them to squeeze into very narrow crevices.",
"A crab’s shell is really a skeleton on the outside of its body. Insects and spiders also have external skeletons.",
]

# parses the cmd passed from the user
def parse_cmd(cmd):
    cmd = cmd.lower()
   
    if (cmd == "help"):
        return print_help()
    elif(cmd == "fact"):
        return "🦀 Here's a crab fact!🦀\n ```" + facts[random.randint(0,len(facts) - 1)] + "```"
    elif(cmd == "rave" or cmd == "gif"):
        return "🦀Here's a crab gif! 🦀\n" + gif_links[random.randint(0,len(gif_links) - 1)]
    else:
        return "🦀 Command not found! Type '!crab help` for a list of commands. 🦀"

def print_help():
    return "crab-bot v0.1\n```available commands:\n- help: shows this message\n- fact: shows a random crab fact\n- gif: shows a random crab gif```"
