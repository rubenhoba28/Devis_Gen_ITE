from setuptools import setup

APP = ['Interface.py']
DATA_FILES = ['logo_senergie_final.png']
OPTIONS = {
    'argv_emulation': False,
    'packages': ['tkinter'],
    'iconfile': 'icon_senergie.icns',  # Spécifiez le chemin vers votre fichier .icns ici

    # Ajoutez d'autres options spécifiques à py2app ici
}

setup(
    app=APP,
    name='Interface_devis',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
