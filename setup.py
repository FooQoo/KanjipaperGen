from setuptools import setup,find_packages

setup(name='KanjipaperGen',
      version='0.0',
      description='KanjipaperGen',
      packages=find_packages(),
      entry_points= '''
      [console_scripts]
      KanjipaperGen=KanjipaperGen:main
      ''',
)
