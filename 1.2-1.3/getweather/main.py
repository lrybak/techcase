#!/usr/bin/env python3

import logging
import os
import sys

from pyowm import OWM
from pyowm.commons.exceptions import UnauthorizedError, NotFoundError


def main():
    """
    Fetches weather information for a specified city using the OpenWeatherMap API and prints the result.

    Environment Variables:
        OWM_API_KEY (str): The API key for OpenWeatherMap.
        OWM_CITY (str): The city for which to fetch weather information.
        TEMP_UNIT (str, optional): Temperature unit. Options: 'celsius', 'fahrenheit'. Default: 'fahrenheit'.

    Note:
        This script expects the OWM_API_KEY and OWM_CITY environment variables to be set.

    Example Usage:
        OWM_API_KEY='your_api_key' OWM_CITY='London' getweather

    Output:
        A string representing weather information in the following format:
        'city="London", description="clear sky", temp=20.3C, humidity=53'

    Errors:
        The script will exit with a status code of 1 if the OWM_API_KEY or OWM_CITY environment variables are not set,
        or if the API request encounters an UnauthorizedError or NotFoundError.
    """
    try:
        # Fetch required environment variables
        owm_api_key = os.environ['OWM_API_KEY']
        owm_city = os.environ['OWM_CITY']
    except KeyError as ke:
        # Handle missing variable definition
        logging.error(f"Environment variable {ke} not set")
        sys.exit(1)

    try:
        # Initialize OpenWeatherMap Api and fetch weather observation
        owm = OWM(owm_api_key)
        owm_manager = owm.weather_manager()
        observation = owm_manager.weather_at_place(owm_city)
    except (UnauthorizedError, NotFoundError) as error:
        # Handle errors in API request
        logging.error(error)
        sys.exit(1)

    # Retrieve, format and print weather information
    w = observation.weather
    temp_unit = 'celsius' if os.environ.get('TEMP_UNIT', '').lower() == 'celsius' else 'fahrenheit'
    current_temp = w.temperature(temp_unit).get('temp')

    print(f'city="{owm_city}", description="{w.detailed_status}", temp={current_temp:.1f}{temp_unit.upper()[0]}, humidity={w.humidity}')


if __name__ == '__main__':
    main()
