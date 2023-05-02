"""Test the attr_recommender module."""

from attr_recommender import SongRecommender
from fake_files import fake_files


def test_SongRecommender() -> None:
    """Test SongRecommender class."""
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
                "Piano Concerto No. 3 in D Minor",
                "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
                "1921",
                "4",
                "0",
                "0.654",
                "0.499",
                "0.189",
                "0.0",
            ],
            [
                "7xPhfUan2yNtyFG0cUWkt8",
                "Clancy Lowered the Boom",
                "Dennis Day",
                "1921",
                "5",
                "0",
                "0.732",
                "0.548",
                "0.186",
                "0.0",
            ],
            [
                "1o6I8BglA6ylDMrIELygv1",
                "Gati Bali",
                "KHP Kridhamardawa Karaton Ngayogyakarta Hadiningrat",
                "1921",
                "5",
                "0",
                "0.961",
                "0.602",
                "0.0452",
                "0.93",
            ],
        ]
    ) as (songfile,):
        song_recommender = SongRecommender(songfile)
        recommended_songs_1 = song_recommender.recommend_songs(
            acousticness=0.6,
            danceability=0.8,
            instrumentalness=0.9,
            energy=0.7,
        )
        assert recommended_songs_1 == ["Piano Concerto No. 3 in D Minor"]
