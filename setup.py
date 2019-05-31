#Setup script to turn Monstrous into a .exe file

import sys
from cx_Freeze import setup, Executable

includefiles = ['Art/icon.png', 'Music/Anamalie.mp3', 'Music/Lone Harvest.mp3', 'Music/Morgana Rides.mp3', 'Music/Sovereign Quarter.mp3', 'Music/Evening of Chaos.mp3', "Art/MonstrousTitleScreen.png", "Credits.txt", "Art/Hand Monster.png", "Art/Teeth Monster.png", "Art/Eye Monster.png", "Art/Throat Monster.png"]
includes = []
packages = ['pygame']

setup(
    name = 'Monstrous',
    version = '1.0',
    options = {'build_exe': {'includes':includes,'packages':packages,'include_files':includefiles}},
    executables = [Executable(script = 'Monstrous.py', icon = 'Art/icon.ico')]
)
