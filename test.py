import pandas as pd

df = pd.read_csv('animes.csv')

genre = True
genre_list = []

while genre:
    genre_input = input("What genres would you like to watch?, input \"done\" when done listing!\n")
    if genre_input == "done":
        genre = False
    else:
        genre_list.append(genre_input)

# List of all cells and their genre put into a list
col_list = df["genre"].values.tolist()
temp_list = []

# Each val in the list is compared with the genre_list to see if there is a match
for index, val in enumerate(col_list):
    if all(x in val for x in genre_list):
        # If there is a match, the UID of that cell is added to a temp_list
        temp_list.append(df['uid'].iloc[index])
print(temp_list)

# This checks if the UID is contained in the temp_list of UIDs that have these genres
df_genre = df["uid"].isin(temp_list)
new_df = df.loc[df_genre, "title"]
# Prints all Anime with the specified genres
print(new_df)