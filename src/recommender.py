"""Song Recommender System based on Popularity."""


def parse_data(file_path: str) -> dict[str, list[dict[str, str]]]:
    """Parse data from file_path."""
    song_dict: dict[str, list[dict[str, str]]] = {}
    with open(file_path, "r", encoding="utf-8-sig") as song_file:
        song_column_names = song_file.readline().strip().split(",")
        for line in song_file:
            obs_values = line.strip().split(",")
            song = {
                song_column_names[i]: obs_values[i]
                for i in range(len(obs_values))
            }
            song_id = song["id"]
            if song_id not in song_dict:
                song_dict[song_id] = []
            song_dict[song_id].append(song)
    return song_dict


if __name__ == "__main__":
    song_dict = parse_data("../data/data.csv")
    print(song_dict)
