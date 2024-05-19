

#A function that takes an input empty dictionary and add values to it
def define_dic (input_dict, id, name, year, rank):
    # Your code goes here
    input_dict [id] = {
        'name':name,
        'year':year,
        'rank':rank
    }
    return input_dict

#A function that thakes an empty dictionary and a list of dictionaries to full the empty dictionary and return it
def define_dic_list (input_dict, input_list):
    
    for e in input_list:
        #Elements willbe according to the dictionary structure an list
        input_dict [e['id']] = {
        'first_e':e ['first_e'],
        'second_e':e ['second_e']
    }
    return input_dict

# Combine 7 dictionaries in one
def combine_movie_data (movies, directors, actors, roles, movies_genres, directors_genres, movies_directors):
    films = {}  # Initialize the resulting dictionary

    # Iterate through movies dictionary
    for movie_id, movie_info in movies.items():
        film = {}  # Create a new dictionary to store movie details
        film['name'] = movie_info['name']
        film['year'] = movie_info['year']
        film['rank'] = movie_info['rank']

        # Add directors
        director_ids = movies_directors.get(str(movie_id), [])
        directors_list = []
        for director_id in director_ids:
            director_info = directors.get(director_id)
            if director_info:
                director_name = f"{director_info['first_name']} {director_info['last_name']}"
                directors_list.append(director_name)
        film['directors'] = directors_list

        # Add actors and their roles
        actor_roles = roles.get(str(movie_id), {})
        actors_list = []
        for actor_id, actor_roles_info in actor_roles.items():
            actor_info = actors.get(actor_id)
            if actor_info:
                actor_name = f"{actor_info['first_name']} {actor_info['last_name']}"
                actor_gender = actor_info['gender']
                roles_list = actor_roles_info['role']
                actor_data = {
                    'name': actor_name,
                    'gender': actor_gender,
                    'roles': roles_list
                }
                actors_list.append(actor_data)
        film['actors'] = actors_list

        # Add genres
        genres_list = movies_genres.get(str(movie_id), [])
        film['genres'] = genres_list

        # Add director genres
        if director_ids:
            director_genre_probs = directors_genres.get(director_ids[0], {})
            director_name = directors.get(director_ids[0], {}).get('first_name', '')
            directors_genres_data = {
                'name': director_name,
                'genres': director_genre_probs
            }
            film['directors_genres'] = directors_genres_data

        # Add the movie to the films dictionary
        films[str(movie_id)] = film
    
    return films

