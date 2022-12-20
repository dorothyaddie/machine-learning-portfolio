from likes import likes
from dislikes import dislikes

songs = likes["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]
print(songs_ids)
with open("like.txt","w") as f:
    f.write(songs_ids)

songs = dislikes["items"]
songs_ids = ""
for track in songs:
    songs_ids += track["track"]["id"] + ","
songs_ids = songs_ids[:-1]

with open("dislike.txt","w") as f:
    f.write(songs_ids)