# FTF Itinerary Generator
GUI application for Funding the Future (nonprofit). Optimizes travel routes for their organization. More at: http://fundingthefuturelive.org/

Works through geolocating latitude/longitude from addresses using geopy, then applying distances between addresses to a Travelling-Salesman-Solver algorithm.
The GUI is made through pyQt5.

## Setup

### Executable

    1 . Download the executable ```main.exe```

    2. Run on your device 

### Manual
1. Download the **code** folder
2. Place the folder where you want it in the future
3. Install dependencies (geopy / pyQt)
4. Run main.py

## Usage(GUI)
Once you have run main.py,a window will pop up. You will then be able to type in a comma separated sequence of valid addresses.
As long as the addresses are comma separated, you should get an output. Addresses are very forgiving.

![Alt text](https://github.com/als5ev/FTF_Itinerary_Generator/blob/master/img/Demo.png?raw=true "GUI Screenshot")

## Usage(Development)
The main functionality of this application is provided by the get_itinerary() function:

```
get_itinerary(addresses):
    print(addresses)
    if len(addresses) == 1 and addresses[0] == "":
        return []

    D, vertices = construct_matrix(addresses)

    path = solve_tsp(D, optim_steps=10)

    ordered_addresses = []
    for entry in path:
        ordered_addresses.append(vertices[entry].geoloc.address)

    return ordered_addresses
```

Similar to the application, the addresses parameter is a comma separated string of valid addresses.

