import random

films = ["Shazam", "Life", "Twelve Monkeys", "Shawshank Redemption"]
# Key: 0 --> 0 (death of cinema), 1-2 --> 1 (really bad), 3-4 --> 2 (bad), 5 --> 3 (meh), 6-7 --> 4 (good), 8-9 --> 5 (great), 10 --> 6 (masterpiece)
critiques = {
    0 : ["The death of cinema", "Should be thrown into the depths of hell", "Incites hatred", "Made this viewer gouge out their eyes", "Up there with the bubonic plague", "Y know how we all say cinema is art? Well, this is the signular exception", "If cinema was like the Notre Dame, this is the fire that burnt it down", "Left no survivors, except this 0/viewer, who is currently recovering at a mental hospital"],
    1 : ["Bad bad bad bad bad bad bad bad bad"],
    2 : ["We're not angry, we're just dissapointed"],
    3 : ["So average it's name is John Smith", "So meh it would give that emoji a run for it's money", "The cinematic equivalent of the color gray", "The vanilla of movies"],
    4 : ["The cinematic equivalent of a cool breeze on an autumn morning"],
    5 : ["Deserves an Oscar for being a Good Boy"],
    6 : ["God's final message to his creation", "The immaculate conception of cinema", "What [director] intended for cinema", "What [world leaders,] would've wanted", "Pure, unrefined cinema", "Indistinguishable from magic", "Should be legally classed as a drug"]
}

for film in films:
    rating = random.randint(0, 10);
    if rating == 0 :
        level = 0
    elif rating < 3:
        level = 1
    elif rating < 5:
        level = 2
    elif rating == 5:
        level = 3
    elif rating < 8:
        level = 4
    elif rating < 10:
        level = 5
    else:
        level = 6
    print ("Our review of " + film + ": " + str(rating) + "/10.")
    print (random.choice(critiques[level]))