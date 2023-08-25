from setuptools import setup, find_packages

setup(
    name='scanner',
    description="Application to scan ip/network against opened ports",
    author='lrybak',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "python-nmap==0.7.1",
        "pydantic==1.10.1",
        "humanize==4.8.0"
    ],
    entry_points={
        'console_scripts': [
            'scanner = scanner.main:main'
        ]
    }
)