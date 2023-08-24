# Excercise 1.2
## Install
```
make install
```

## Uninstall
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

# Exsercise 1.2

## Build image

```
docker build . --no-cache -t getweather:dev
```

## Run container

```
docker run --rm -e OWM_API_KEY="xxxx" -e OWM_CITY="Kraków,PL" getweather:dev
```