from cx_Freeze import setup, Executable
import idna
import random

base = None    

executables = [Executable("Contacts.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "GuessNumber_Game",
    options = options,
    version = "1.1",
    description = 'Play with Numbers',
    executables = executables
)
#changes
#added new code to the base
#0218 changes