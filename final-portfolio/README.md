# Introduction
Hi, dad! This is Dorothy. For my final project in machine learning, I got the opportunity to make a final portfolio showcasing the work I completed over the course of the semester. This portfolio aims to share the highlights with you. I have structured this portfolio in a similar way to how the class was structured. It starts with an introduction to unsupervised machine learning and moves into supervised machine learning. It ends with a short introduction into the basics of neural networks. The portfolio uses a dataset that was scraped from the Spotify API, so all of the algorithms could be replicated on mine or your spotify data. You can learn more about the data below. The algorithms used in this portfolio include some I have written from scratch and built in implementations from Python libraries like sklearn and tensorflow. I hope you enjoy! I know that you were really excited to hear I was taking this class so I hope you are excited to learn more about what I did. 

# About the data
The dataset is from the Spotify API, where users can access data about songs. I aquirred the dataset by following directions posted on the following documentation: https://developer.spotify.com/console/get-playlist-tracks/ and https://developer.spotify.com/console/get-audio-features-several-tracks/. The dataset is comprimised of 195 songs. 100 songs are some of my favorite songs and the other 95 are songs that I hate. To get the data, I forst got the list of all the playlist ids on my spotify. Then, I got the list of all the song ids in the two playlists I was interested in: 100 Songs I Love and 95 Songs I Hate. Then, I got the data for each song in both playlist and added them all to a dataframe. I then converted the dataframe to a csv, which is the data.csv file used in each coding element of my portfolio. All the code I used to get the data csv is in the folder titled data. The data is a set of songs with attributes and whether or not the I liked the song. Each observation represents a song. Below I talk about each of the variables in depth:
* **danceability** describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* **energy** is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. 
* **key** is the key the track is in
* **loudness** is the overall loudness of a track in decibels (dB)
* **mode** indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* **speechiness** detects the presence of spoken words
* **acousticness** is a confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic
* **instrumentalness** predicts whether a track contains no vocals.
* **liveness** detects the presence of an audience in the recording.
* **valence** is a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track

# Questions about the data
My exploration of the dataset in the portfolio aims to develop an algorithm that can decide whether or not a song will be liked by a given user. I also explore some characteristics of songs that are important in making this decision. 

# K-means
The first coding element of my portfolio is on a machine learning algorithm called k-means. It is an unsupervised classification algorithm, meaning it classifies data without knowing correct answers or not. In the context of the spotify data, the algorithm has no information about whether or not the user likes the song. It aims to discover hidden patterns. In this section, I walk through my own implementation of k-means using the Spotify data. I also include some visualizations to see how the algorithm classifies each song. 

# Comparing decision trees, support vector machines, and Random Forests
The second coding element of my portfolio compares the effectiveness of decison trees, support vector machines, and random forests. These are supervised classification algorithms, meaning the model knows the correct answers. I explain what each model is. I build the model and then evaluate its performance on the dataset. I also included some visualizations of the models that show how they classify the data. 

# Neural Networks
The last component of my portfolio uses neural networks. This is a type of supervised machine learning. I implemented two neural networks on the spotify data using tensorflow. I then compared the networks accuracy using data visualizations and decided which one woul dbe the better model to use. 