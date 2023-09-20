from setuptools import setup, find_packages

setup(
    name='getweather',
    description="Application to retrieve current weather observation from OpenWeatherMap API",
    author='lrybak',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "pyowm==3.3.0"
    ],
    entry_points={
        'console_scripts': [
            'getweather = getweather.main:main'
        ]
    }
)