import sys
from cx_Freeze import setup, Executable

includefiles = ['icon.png', 'Anamalie.mp3', 'Lone Harvest.mp3', 'Morgana Rides.mp3', 'Sovereign Quarter.mp3']
includes = []
packages = ['pygame']

setup(
    name = 'Monstrous',
    version = '1.0',
    options = {'build_exe': {'includes':includes,'packages':packages,'include_files':includefiles}},
    executables = [Executable(script = 'Monstrous DEMO.py', icon = 'icon.ico')]
)
