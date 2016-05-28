from setuptools import setup

setup(name='camilley-camille',
      version='0.1',
      description='camilley test stuff for pycon tutorial',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
)
