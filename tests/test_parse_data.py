"""Test the parse_data module."""

from parse_data import (
    Song,
    parse_data,
)
from fake_files import fake_files


def test_song_class() -> None:
    """Test Song class."""
    song = Song(
        "4BJqT0PrAfrxzMOxytFOIz",
        "Piano Concerto No. 3 in D Minor",
        "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
        "1921",
        "4",
        "0",
        "0.982",
        "0.279",
        "0.211",
        "0.878",
    )
    assert song.song_id == "4BJqT0PrAfrxzMOxytFOIz"
    assert song.song_name == "Piano Concerto No. 3 in D Minor"
    assert (
        song.artist_name
        == "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker"
    )
    assert song.year == "1921"
    assert song.popularity == "4"
    assert song.explicit == "0"
    assert song.__repr__() == (
        "Song Name: Piano Concerto No. 3 in D Minor "
        + "by Sergei Rachmaninoff & James Levine & Berliner Philharmoniker, "
        + "Year: 1921"
    )
    assert song.acousticness == "0.982"
    assert song.danceability == "0.279"
    assert song.instrumentalness == "0.211"
    assert song.energy == "0.878"


def test_parse_data() -> None:
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
                "Piano Concerto No. 3 in D Minor",
                "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker",
                "1921",
                "4",
                "0",
                "0.982",
                "0.279",
                "0.211",
                "0.878",
            ],
        ]
    ) as (song_file,):
        song_dict = parse_data(song_file)
        assert (
            song_dict["4BJqT0PrAfrxzMOxytFOIz"].song_id
            == "4BJqT0PrAfrxzMOxytFOIz"
        )
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].song_name == (
            "Piano Concerto No. 3 in D Minor"
        )
        assert (
            song_dict["4BJqT0PrAfrxzMOxytFOIz"].artist_name
            == "Sergei Rachmaninoff & James Levine & Berliner Philharmoniker"
        )
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].year == "1921"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].popularity == "4"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].explicit == "0"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].acousticness == "0.982"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].danceability == "0.279"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].instrumentalness == "0.211"
        assert song_dict["4BJqT0PrAfrxzMOxytFOIz"].energy == "0.878"
