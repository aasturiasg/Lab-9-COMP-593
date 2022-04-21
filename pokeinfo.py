from requests import get

def retrieve_pokemon_data(pokemon_name):

    """
    Gets information from the PokeAPI for a specified pokemon and formats it as a dictionary.

    :param pokemon_name: name or index of the desired pokemon
    :returns: dictionary containing pokemon information if successful; None if unsuccessful
    """

    print('Getting Pokemon data from PokeAPI...')

    #make sure the input is valid
    pokemon_name = pokemon_name.strip().lower()
    if pokemon_name == '':
        return None

    #establish a connection and get all the iformation for a pokemon
    request_response = get('https://pokeapi.co/api/v2/pokemon/' + str(pokemon_name))

    #determine the outcome of the request
    if request_response.status_code == 200:
        print('Request successful, data for ' + pokemon_name + ' gathered.')
        return request_response.json()
    elif request_response.status_code == 404:
        print('Unable to establish connection: ' + str(request_response.status_code) + "\nMake sure to input a valid pokemon name/number.")
        return None
    else:
        print('Unable to establish connection: ' + str(request_response.status_code) + ".")
        return None

def retrieve_pokemon_list(limit=1800, offset=0):
    
    """
    Obtains a list with all pokemon names in the PokeAPI.

    :param limit: maximum number of pokemons that can be retrieved
    :param offset: index of the first pokemon to get
    :returns: list containing all pokemon names if successful; None if unsuccessful
    """

    print('Obtaining all pokemon names...', end=' ')

    #define parameters for the request
    URL = 'https://pokeapi.co/api/v2/pokemon'
    api_parameters = {'limit': limit, 'offset': offset}

    #get a response from the pokeapi corresponding to the url and parameters specified
    response_message = get(URL, params=api_parameters)

    #if the request was successful, exrtact the name of each pokemon and return it
    if response_message.status_code == 200:
        pokemon_dictionary = response_message.json()
        print('done!')
        return [pokemon['name'].capitalize() for pokemon in pokemon_dictionary['results']]

    #for any other scenarion, show the response conde and return none
    else:
        print('unexpected error encountered. Response code: ' + str(response_message.status_code))
        return None

def get_image_url(pokemon_name):

    """
    Gets the URL to the image of a specified pokemon.

    :param pokemon_name: name or index of the desired pokemon
    :returns: string containing the url to the pokemon's image if successful; None if unsuccessful
    """

    #get a dictionary with all the information corresponding to the specified pokemon
    pokemon_dictionary = retrieve_pokemon_data(pokemon_name)

    #if the request was successful, return the url to the pokemon's image
    if pokemon_dictionary:
        return pokemon_dictionary['sprites']['other']['official-artwork']['front_default']
    
    #for any other scenarion, return none
    else:
        return None