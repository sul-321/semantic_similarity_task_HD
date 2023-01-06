import spacy


def find_similar_movie(description):
    nlp = spacy.load("en_core_web_md")
    planet_hulk = nlp(description)

    file = open("movies.txt", "r")
    movies = file.readlines()
    similarity_scores = {}

    for movie in movies:
        movie_title = movie[:movie.index(":")]
        movie_desc = nlp(movie[movie.index(":") + 1:])
        similarity = movie_desc.similarity(planet_hulk)
        similarity_scores[movie_title] = similarity

    max_similarity = max(similarity_scores.values())
    for movie_title, score in similarity_scores.items():
        if score == max_similarity:
            return movie_title

# Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him to a space planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.


similar_movie = find_similar_movie(
    "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him to a space planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

print(
    f"As you have watched Planet Hulk, the most similar movie is {similar_movie}.")
