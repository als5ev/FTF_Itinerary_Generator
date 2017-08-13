import sys
from cx_Freeze import setup, Executable

base = "Win32GUI"

setup(
    name = "FTF_Itinerary_Generator",
    executables = [Executable("main.py", base=base)]
)
