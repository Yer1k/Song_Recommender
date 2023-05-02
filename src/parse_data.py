"""Parse song data from file_path."""


class Song:
    """Song class."""

    def __init__(
        self,
        song_id: str,
        song_name: str,
        artist_name: str,
        year: str,
        popularity: str,
        explicit: str,
        acousticness: str,
        danceability: str,
        instrumentalness: str,
        energy: str,
    ) -> None:
        """Initialize Song class."""
        self.song_id = song_id
        self.song_name = song_name
        self.artist_name = artist_name
        self.year = year
        self.popularity = popularity
        self.explicit = explicit
        self.acousticness = acousticness
        self.danceability = danceability
        self.instrumentalness = instrumentalness
        self.energy = energy

    def __repr__(self) -> str:
        """Return string representation of Song."""
        print_out = (
            f"Song Name: {self.song_name} by {self.artist_name}, "
            + f"Year: {self.year}"
        )
        return print_out


def song_data(file_path: str) -> dict[str, dict[str, str]]:
    """Parse data from file_path."""
    song_dict: dict[str, dict[str, str]] = {}
    with open(file_path, "r", encoding="utf-8-sig") as song_file:
        song_column_names = song_file.readline().strip().split("\t")
        for line in song_file:
            obs_values = line.strip().split("\t")
            song = {
                song_column_names[i]: obs_values[i]
                for i in range(len(song_column_names))
            }
            song_id = song["id"]
            song_dict[song_id] = song
    return song_dict


def parse_data(file_path: str) -> dict[str, Song]:
    """Parse data from file_path."""
    song_dict = song_data(file_path)
    song = {}
    for song_id in song_dict:
        song[song_id] = Song(
            song_dict[song_id]["id"],
            song_dict[song_id]["name"],
            song_dict[song_id]["artists"],
            song_dict[song_id]["year"],
            song_dict[song_id]["popularity"],
            song_dict[song_id]["explicit"],
            song_dict[song_id]["acousticness"],
            song_dict[song_id]["danceability"],
            song_dict[song_id]["instrumentalness"],
            song_dict[song_id]["energy"],
        )
    return song
