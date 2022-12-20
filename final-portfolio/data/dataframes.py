from dislikes_info import dislikes_info
from likes_info import likes_info
import pandas as pd


'''songs = likes_info["audio_features"][0][0]
print(songs)
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]
#print(songs_ids)
with open("like.txt","w") as f:
    f.write(songs_ids)'''

'''songs = dislikes["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]

with open("dislike.txt","w") as f:
    f.write(songs_ids)'''

#making a dataframe of all the disliked songs
df_dislike = pd.json_normalize(dislikes_info)
print(df_dislike)

#making a dataframe of all the liked songs
df_like = pd.json_normalize(likes_info)
print(df_like)

#adding a column for the liked ratings
liked = [1] * df_like.shape[0]
df_like['liked'] = liked
#print(df_like)
print(df_like)

#adding a column for the disliked ratings
disliked = [0] * df_dislike.shape[0]
df_dislike['liked'] = disliked
#print(df_dislike)

#making one dataframe with liked and disliked songs
df = pd.concat([df_like, df_dislike])
#resetting index
df = df.reset_index(drop=True)
#include only numeric data
final_df = df.select_dtypes(include='number')

#saving dataframe as a csv
data_csv = final_df.to_csv()
print(data_csv)