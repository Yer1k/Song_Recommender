# Song Recommendation System

**Music Recommendation System Using Python**

#### Team Members: [Pragya Raghuvanshi](https://github.com/pr-124), [Sukhpreet Sahota](https://github.com/5ukhy21), [Dingkun Yang](https://github.com/Yer1k)

## Introduction
This Github Repo supports a song recommendation system that is built by data pulled from Kaggle via Spotify API. The recommendation system enables users to get suggestions based on Popularity of the music/song

## Dataset
The dataset used for this project is from Kaggle and can be found here: 
Spotify dataset extracted by VATSAL MAVANI and posted on Kaggle, link: [Dataset](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset)

**Some features of the data:**

Songs releasing years from *1921 - 2020*

Songs Count: *133,638*

Genres Count: *2,973*

## Approach
To create this recommendation system, we divided the project into 4 key steps:
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Building out a song popularity recommender
4. Incorporating song features recommender into the song feature recommender 
5. Testing all components

Below is an illustrative flow chart outlining these 4 steps:

<img width="350" alt="image" src="https://user-images.githubusercontent.com/112578035/235789126-14ee239c-effc-4217-8616-9d2005a0cd85.png">

## Installation

To replicate the results, please fork this git repository or clone it using `git clone git@github.com:Yer1k/Song_Recommender.git`

Upon doing so, please ensure all test files and source/code files are within the same directory. Please move all test files into your tests/directory if running this code locally. Please also install all libraries outlined within the `requirements.txt` file.
In addition to the libraries specified within the requirements file, please also `pip install pytest` before importing/executing the test files.

## Test Case Examples

*test_song_class* and *test_parse_data* Example

Start by creating a set of songs before passing the Song class to ensure the song attributes are returned correctly. In testing the parse_data function, after creating these structures, pass this through the parse_data function and assert to make sure the song file returns are the same as dictionaries created when using the `data.txt` file.


> Example usage:
> ```
> import pytest
> 
> from parse_data import (
>    Song,
>    parse_data,
>)
> from fake_files import fake_files
> 
> def test_song_class() -> None:
>    #  set up
>    """Test Song class."""
>    song = Song(
>        "4BJqT0PrAfrxzMOxytFOIz",
>        "Piano Concerto No. 3 in D Minor",
>        "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
>        "1921",
>        "4",
>    )
>                
>     #  run and assert
>    assert song.song_id == "4BJqT0PrAfrxzMOxytFOIz"
>    assert song.song_name == "Piano Concerto No. 3 in D Minor"
>    assert (
>        song.artist_name
>        == "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker"
>    )
>    assert song.year == "1921"
>    assert song.popularity == "4"
>    assert song.__repr__() == (
>        "Song Name: Piano Concerto No. 3 in D Minor "
>        + "by Sergei Rachmaninoff & James Levine & Berliner Philharmoniker, "
>        + "Year: 1921"
>    )
>
> def test_parse_data() -> None:
>     """Test parse_data function."""
>     with fake_files(
>         [
>             [
>                 "id",
>                 "name",
>                 "artists",
>                 "year",
>                 "popularity",
>             ],
>             [
>                 "4BJqT0PrAfrxzMOxytFOIz",
>                 "Piano Concerto No. 3 in D Minor",
>                 "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
>                 "1921",
>                 "4",
>             ],
>         ]
>     ) as (song_file,):
>         song_dict = parse_data(song_file)
>         assert (
>             song_dict["4BJqT0PrAfrxzMOxytFOIz"].song_id
>             == "4BJqT0PrAfrxzMOxytFOIz"
>         )
>         assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].song_name == (
>             "Piano Concerto No. 3 in D Minor"
>         )
>         assert (
>             song_dict["4BJqT0PrAfrxzMOxytFOIz"].artist_name
>             == "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker"
>         )
>         assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].year == "1921"
>         assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].popularity == "4"
> 
> ```

*test_popularity_recommender* Example

For testing the popularity recommender, we are analyzing the dictionary created after fake files develops the associated list of artists and songs. The assert statements ensure that the average popularity is returned and the number of songs provided back to the users are based on their preferred number of songs. Additionally, we want to make sure the user gets the summary stats on the number of songs and artists within a given file.

> Example usage:
> ```
> from fake_files import fake_files
> from popularity_recommender import *
> 
> 
> def test_calculate_artist_avg_popularity() -> None:
>     # set up
>     
>     with fake_files(
>         [
>             [
>                 "id",
>                 "name",
>                 "artists",
>                 "year",
>                 "popularity",
>             ],
>             [
>                 "4BJqT0PrAfrxzMOxytFOIz",
>                 "Pragya is a genius",
>                 "Dingkun Yang",
>                 "1921",
>                 "4",
>             ],...
>         ]
>     ) as (song_file,):
>         # run
>         s = SongRecommendationSystem(song_file)
> 
>         # assert
>         assert s.calculate_artist_avg_popularity() == {
>             "Sergei Rachmaninoff": 5,
>             "James Levine": 5,
>             "Berliner Philharmoniker": 5,
>             "Dingkun Yang": 3,
>             "Pragya R": 3,
>             "Sukhpreet S": 6,
>         }
>         assert s.recommend_songs(2) == [
>             "Dingkun is a genius",
>             "Piano Concerto No. 3 in C Major",
>         ]
>         assert (
>             s.__str__()
>             == "SongRecommendationSystem with 5 songs and 6 artists."
> ```


## Future Work
As we look to build out this song recommendation system and make it more comprehensive, we will incorporate the following recommendation suggestion abilities into the system: By Artist, and By Distinguishing musical characteristics of the song

To build on our exisiting recommendation system, we will incorporate the following 4 steps into this project:
1. Building out a song similarity recommender based on artist
2. Testing all components
3. Combining into a single song recommendation system

Below is an illustrative flow chart depicting how our future work will be integrating into our existing system:

<img width="569" alt="Screenshot 2023-04-10 at 4 14 49 AM" src="https://user-images.githubusercontent.com/112578035/230861811-337834dc-09df-48ef-befe-9db940c443a7.png">
