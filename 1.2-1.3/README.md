# Exercise 1.2
## Install

```
make install
```

After executing **make install** make sure to relogin to refresh $PATH envvar or manually update $PATH
```
export PATH=$HOME/.local/bin:$PATH
```

## Uninstall
Uninstall package if no longer required
```
make uninstall
```

## Usage
```
OWM_API_KEY='your_api_key' OWM_CITY='London' getweather

# optionally you can specify temperature unit preffered
export TEMP_UNIT=celsius # or fahrenheit

ex.
OWM_API_KEY='your_api_key' OWM_CITY='London' TEMP_UNIT=celsius getweather
```

## Cleanup
```
make clean
```

# Exercise 1.3

## Build image
Run below command to build docker image 
```
docker build . --no-cache -t getweather:dev
```

## Run container

```
docker run --rm -e OWM_API_KEY="your_api_key" -e OWM_CITY="Kraków,PL" getweather:dev
```