import pandas as pd

print("````````````````````````````````````````````````````````````````````````````````````````````````````")
print("Welcome to the Anime Recommendation Engine!")
df = pd.read_csv('animes.csv')
all_genres = ["Action", "Adventure", "Comedy", "Drama", "Slice of Life",
              "Fantasy", "Magic", "Supernatural", "Horror", "Mystery",
              "Psychological", "Romance", "Sci-Fi", "Game", "Ecchi", "Demons",
              "Harem", "Josei", "Martial Arts", "Kids", "Historical", "Hentai",
              "Isekai", "Military", "Mecha", "Music", "Parody", "Police",
              "Reverse Harem", "School", "Shoujo ai", "Shounen", "Shounen ai",
              "Space", "Sports", "Super Power", "Tragedy", "Vampire", "Yuri", "Yaoi"]

while True:
    game_input = input("Press 1 to get started, 2 for instructions and anything else to exit!\n")
    if game_input == "1":
        print("````````````````````````````````````````````````````````````````````````````````````````````````````")
        while True:
            episodes = input("Whats the highest number of episodes you are willing to watch? {Input: (1 - ∞) || d if it"
                             " doesnt matter}\n")
            if episodes == "d":
                episodes = 1000000
                df_episdoes = (df["episodes"] < episodes)
                break
            elif episodes.isalpha():
                print("Invalid Input")
            else:
                df_episdoes = (df["episodes"] < int(episodes))
                break

        print("````````````````````````````````````````````````````````````````````````````````````````````````````")
        while True:
            rankings = input("Whats the highest number of ranking you want your anime to have? {Input: (1 - ∞) || d if "
                             "it doesnt matter}\n")
            if rankings == "d":
                rankings = 1000000
                df_ranked = (df["ranked"] < rankings)
                break
            elif rankings.isalpha():
                print("Invalid Input")
            else:
                df_ranked = (df["ranked"] < int(rankings))
                break

        genre_list = []
        temp_list = []
        genre = True
        while genre:
            print("````````````````````````````````````````````````````````````````````````````````````````````````````")
            print("You can pick any of the following genres! :\n {}".format(all_genres))
            genre_input = input("What genres would you like to watch? {Input: genre1, genre2, genre3, etc}\n")
            genre_list = genre_input.split(",")
            for word in genre_list:
                temp = word.strip()
                temp = temp.title()
                if temp == "Slice Of Life":
                    temp = "Slice of Life"
                temp_list.append(temp)
            genre_list = temp_list

            for item in genre_list:
                if item not in all_genres:
                    genre = True
                    print("Invalid genre!")
                    genre_list.clear()
                    break
                else:
                    genre = False

        df_genre = df['genre'].apply(lambda x: all([i in x for i in genre_list]))
        new_df = df.loc[df_ranked & df_episdoes & df_genre, "title": "link"]
        if new_df.empty:
            print('No such anime exists! Try again!\n')
            continue
        else:
            print("````````````````````````````````````````````````````````````````````````````````````````````````````")
            print("This is the list of recommendations I compiled for you!\n")
            print(new_df)
            new_df.to_csv('Result.csv', index=False)
            print("You can view the full Spreadsheet by opening \"Result.csv\"")
            print("````````````````````````````````````````````````````````````````````````````````````````````````````")

    elif game_input == "2":
        print("This is an anime recommendation engine! We will ask you a series of questions to find out the best set\n"
              "of animes according to your preferences!\n")
    else:
        exit(0)
        
   
# THINGS I WANT TO ADD:
# Add a search option for the anime where after the name is searched, the title, synopsis and the link is outputed
