lyrics= "Salty air, and the rusty door, I never needed anything more Whispers of Are you sure? Never have I ever before"

noun1= input("Noun1: ").upper()
noun2= input("Noun2: ").upper()
adj1= input("Adjective1: ").upper()
adj2= input("Adjective2: ").upper()

lyrics = lyrics.replace("Salty", adj1, 1)
lyrics = lyrics.replace("I", noun1, 1)
lyrics = lyrics.replace("you", noun2, 1)
lyrics = lyrics.replace("rusty", adj2, 1)

print(lyrics)