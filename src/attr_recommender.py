"""Recommender based on k-nearest neighbors (KNN) algorithm."""


from sklearn.neighbors import NearestNeighbors
from parse_data import parse_data


class SongRecommender:
    """Recommender based on k-nearest neighbors (KNN) algorithm."""

    def __init__(self, filepath: str):
        """Initialize recommender."""
        # Load data from file and create song dictionary
        self.song_dict = parse_data(filepath)

        # Fit KNN model
        X = []
        for song_id in self.song_dict:
            song = self.song_dict[song_id]
            X.append(
                [
                    float(song.acousticness),
                    float(song.danceability),
                    float(song.instrumentalness),
                    float(song.energy),
                ]
            )
        self.knn_model = NearestNeighbors(n_neighbors=1)
        self.knn_model.fit(X)

    def recommend_songs(
        self,
        acousticness: float,
        danceability: float,
        instrumentalness: float,
        energy: float,
    ) -> list[str]:
        """Recommend songs based on input features."""
        # Create input feature vector
        input_vector = [[acousticness, danceability, instrumentalness, energy]]

        # Find similar songs using KNN
        _, indices = self.knn_model.kneighbors(input_vector)

        # Return recommended songs
        recommended_songs = [
            self.song_dict[list(self.song_dict.keys())[song_id]].song_name
            for song_id in indices[0]
        ]
        return recommended_songs


if __name__ == "__main__":
    # Create recommender
    recommender = SongRecommender("data/data.txt")

    # Get recommendations
    recommended_songs = recommender.recommend_songs(0.3, 0.2, 0.4, 0.5)

    # Print recommendations
    print("Recommended Songs:")
    for song in recommended_songs:
        print(song)
