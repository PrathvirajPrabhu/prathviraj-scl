from pprint import pprint


def clean_url(url):
    if url:
        uh = url.split('_')
        jpg = uh[-1].split('.')
        return uh[0] + jpg[1]
    else:
        return ' '


def cast_details(cast_class):
    query = []
    if cast_class:
        for cast in cast_class:
            query.append([cast.data.get('name'), cast.currentRole.__str__()])
        return query
    else:
        return [' ']


def director_details(director_class):
    query = []
    if director_class:
        for director in director_class:
            query.append(director.data.get('name'))
        return query
    else:
        return ['']


def search_result(ia, movie):
    movie = ia.search_movie(movie)
    query_set = []
    for m in movie:
        dictionary = {
            'cover': clean_url(m.get('cover url')),
            'kind': m.get('kind'),
            'title': m.get('title'),
            'year': m.get('year'),
            'id': m.movieID,
        }
        query_set.append(dictionary)
    pprint(query_set)
    return query_set


def detail_result(ia, id):
    movie = ia.get_movie(id)

    m = movie.data
    query_set = {
        'title': m.get('title'),
        'cover': clean_url(m.get('cover url')),
        'year': m.get('year'),
        'rating': m.get('rating'),
        'kind': m.get('kind'),
        'genres': m.get('genres'),
        'plot': m.get('plot'),
        'release': m.get('original air date'),
        'languages': m.get('languages'),
        'cast': cast_details(m.get('cast')),
        'directors': director_details(m.get('directors'))
    }
    return query_set

