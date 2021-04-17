from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_srting = ''
for letter, landmark in landmark_choices.items():
    landmark_srting += '{0} - {1}\n'.format(letter, landmark)
stations_under_construction = ['Bridgeport', 'King Edward']


def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n")
    print(landmark_srting)


def skyroute():
    greet()
    new_route()
    again = input('Would you like to see another route? Enter y/n:')
    if again == 'y' or again == 'Y':
        show_landmarks()
        new_route()
    goodbye()


def get_start():
    start_point_letter = input('where are you coming from? type in the corresponding letter: ')
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        start_point = get_start()

    return start_point


def get_end():
    end_point_letter = input('where are you headed? type in the corresponding letter: ')
    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        end_point = get_end()
    return end_point


def set_start_and_end(start_point, end_point):
    if start_point:
        change_point = input(
            " change point: \nWhat would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print('worong option.please try again!')
    else:
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print('the shorest metro route from {0} to {1} is: \n{2}'.format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point,
                                                                                                         end_point))


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_merto
            if not stations_under_construction:
                possible_route = dfs(merto_system, start_station, end_station)
                if not possible_route:
                    return None
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    shortest_route = min(routes, key=len)
    return shortest_route


def show_landmarks():
    see_landmarks = input('Would you like to see the list of landmarks again? Enter y/n: ')
    if see_landmarks == 'y' or see_landmarks == 'Y':
        print(landmark_srting)


def goodbye():
    print('Thanks for using SkyRoute!')


def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])
    return updated_metro


skyroute()


# BONUS: Add more features!
#
#     What happens if the user enters the same station for their origin and destination?
#     What if Vancouver’s system wants a user interface for employees to update the stations under construction?
#     Can you think of other ways to improve this program?



