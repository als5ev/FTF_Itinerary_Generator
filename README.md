# FTF Itinerary Generator
GUI application for Funding the Future (nonprofit). Optimizes travel routes for their organization. More at: http://fundingthefuturelive.org/

Works through geolocating latitude/longitude from addresses using geopy, then applying distances between addresses to a Travelling-Salesman-Solver algorithm.
The GUI is made through pyQt5.

## Setup

#### Executable
1. Download the executable ```main.exe```
2. Run on your device 

#### Manual
1. Clone the repo
2. pip install -r requirements.txt
3. Run main.py

## Usage(GUI)
Once you have run main.py, a window will pop up. You will then be able to type in a comma separated sequence of valid addresses.
As long as the addresses are comma separated, you should get an output. Addresses are very forgiving.

![Alt text](https://github.com/als5ev/FTF_Itinerary_Generator/blob/master/img/Demo.png?raw=true "GUI Screenshot")

## Usage(Development)
The main functionality of this application is provided by the [get_itinerary()](https://github.com/als5ev/FTF_Itinerary_Generator/blob/master/code/parse_file.py#L63) function.
