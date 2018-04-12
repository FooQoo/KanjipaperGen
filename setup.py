from setuptools import setup

setup(name='KanjipaperGen',
      version='0.0',
      description='KanjipaperGen',
      packages=setuptools.find_packages(),
      entry_points= """
                    [console_scripts]
                    KanjipaperGen=KanjipaperGen:main
                    """
)
