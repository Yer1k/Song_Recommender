"""Song recommendation system based on popularity."""
from parse_data import parse_data


class SongRecommendationSystem:
    """Song recommendation system Class."""

    def __init__(self, file_path: str) -> None:
        """Initialize SongRecommendationSystem class."""
        self.song_dict = parse_data(file_path)
        self.artist_avg_popularity = self.calculate_artist_avg_popularity()

    def __str__(self) -> str:
        """Return string representation of SongRecommendationSystem."""
        return (
            "SongRecommendationSystem with "
            f"{len(self.song_dict)} songs and "
            f"{len(self.artist_avg_popularity)} artists."
        )

    def calculate_artist_avg_popularity(self) -> dict[str, float]:
        """Calculate average popularity for each artist."""
        artist_popularity: dict[str, list[float]] = {}
        for song in self.song_dict.values():
            for artist in song.artist_name.split(" & "):
                artist = artist.strip()
                if artist not in artist_popularity:
                    artist_popularity[artist] = []
                artist_popularity[artist].append(float(song.popularity))

        return {
            artist: sum(popularities) / len(popularities)
            for artist, popularities in artist_popularity.items()
        }

    def recommend_songs(self, num_songs: int) -> list[str]:
        """Recommend songs based on popularity."""
        recommended_songs = sorted(
            self.song_dict.values(),
            key=lambda song: sum(
                self.artist_avg_popularity.get(artist.strip(), 0)
                for artist in song.artist_name.split("&")
            )
            / len(song.artist_name.split("&")),
            reverse=True,
        )[:num_songs]

        return [song.song_name for song in recommended_songs]
