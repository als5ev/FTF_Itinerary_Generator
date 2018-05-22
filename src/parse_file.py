import geopy
from queue import Queue
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from tsp_solver import solve_tsp


class Vertex:
    def __init__(self, geoloc, adjacencies=[], path=None, distance=None):
        self.geoloc = geoloc
        self.adjacencies = adjacencies



def get_distance(v1, v2):

    lat_long1 = (v1.geoloc.latitude, v1.geoloc.longitude)
    lat_long2 = (v2.geoloc.latitude, v2.geoloc.longitude)
    return vincenty(lat_long1, lat_long2).miles



#Takes in a list of addresses in string format
def construct_matrix(locations):

    if locations[-1] == "":
        return "Remove comma at end of last address", -1

    vertices = []

    #geocode the locations
    geolocator = Nominatim()
    for loc in locations:
        geopy_loc = geolocator.geocode(loc)

        #if a location breaks the app, return it and display on screen
        try:
            test = geopy_loc.address
        except AttributeError:
            return loc, -1

        vert = Vertex(geopy_loc)
        vertices.append(vert)

    #set adjacency lists
    for vert in vertices:
        copy_vertices = vertices[:]
        vert.adjacencies = copy_vertices

    #construct distance matrix
    D = [[0 for col in range(len(vertices))] for row in range(len(vertices))]
    for i in range(0, len(vertices)):
        for j in range(0, len(vert.adjacencies)):
            vert_start = vertices[i]
            vert_end = vertices[i].adjacencies[j]
            distance = get_distance(vert_start, vert_end)
            D[i][j] = distance

    return D, vertices



def get_itinerary(addresses):

    #return nothing if no input
    if len(addresses) == 1 and addresses[0] == "":
        return []

    # if fails vertices is -1 and D is the address for which there is a format error
    D, vertices = construct_matrix(addresses)

    if vertices == -1:
        return ["Format Error: " + str(D)]

    path = solve_tsp(D, optim_steps=10)

    ordered_addresses = []
    for entry in path:
        ordered_addresses.append(vertices[entry].geoloc.address)

    return ordered_addresses








