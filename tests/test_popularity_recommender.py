"""Test Song Recommendation functions."""


from fake_files import fake_files
from popularity_recommender import *


def test_calculate_artist_avg_popularity() -> None:
    # set up
    """Test parse_data function."""
    with fake_files(
        [
            [
                "id",
                "name",
                "artists",
                "year",
                "popularity",
                "explicit",
                "acousticness",
                "danceability",
                "instrumentalness",
                "energy",
            ],
            [
                "4BJqT0PrAfrxzMOxytFOIz",
                "Pragya is a genius",
                "Dingkun Yang",
                "1921",
                "4",
                "0",
                "0.991",
                "0.598",
                "0.918",
                "0.224",
            ],
            [
                "98557djkf7878fd90dno",
                "Pragya is a genius 2",
                "Dingkun Yang",
                "1925",
                "2",
                "0",
                "0.993",
                "0.598",
                "0.918",
                "0.224",
            ],
            [
                "78i8uidf34870293jjkhf96",
                "Piano Concerto No. 3 in C Major",
                "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
                "1923",
                "5",
                "0",
                "0.994",
                "0.598",
                "0.918",
                "0.224",
            ],
            [
                "kudo778846720923759djfu7f",
                "Sukhpreet is a genius",
                "Pragya R",
                "1919",
                "3",
                "0",
                "0.995",
                "0.598",
                "0.918",
                "0.224",
            ],
            [
                "3829dnsknfjis893940209",
                "Dingkun is a genius",
                "Sukhpreet S",
                "1920",
                "6",
                "0",
                "0.996",
                "0.598",
                "0.918",
                "0.224",
            ],
        ]
    ) as (song_file,):
        # run
        s = SongRecommendationSystem(song_file)

        # assert
        assert s.calculate_artist_avg_popularity() == {
            "Sergei Rachmaninoff": 5,
            "James Levine": 5,
            "Berliner Philharmoniker": 5,
            "Dingkun Yang": 3,
            "Pragya R": 3,
            "Sukhpreet S": 6,
        }
        assert s.recommend_songs(2) == [
            "Dingkun is a genius",
            "Piano Concerto No. 3 in C Major",
        ]
        assert (
            s.__str__()
            == "SongRecommendationSystem with 5 songs and 6 artists."
        )
