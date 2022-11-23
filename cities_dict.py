def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    dic = {}
    for i in range(len(cities)):
        dic[i] = cities[i]
    return dic
cities = ["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]
print(cities_dict(cities))