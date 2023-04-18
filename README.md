# Sky-Search App

This application checks the prices of flights for various destinations and sends a notification via WhatsApp if the price is lower than a specific threshold.

## Setup
Before running the app, you need to set up the following environment variables:
- `ENDPOINT_SHEETY`: The endpoint of the Google Sheet that contains the data about the destinations and their IATA codes.
- `TEQUILA_API_KEY`: Your API key for the Kiwi Tequila API.
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_ACCOUNT_AUTH_TOKEN`: Your Twilio account authentication token.
- `TWILIO_BOT_NR`: Your Twilio bot's phone number.
- `MY_PHONE_NR`: Your phone number.

## Usage
To run the app, simply execute the `main.py` file. The app will retrieve the destination data from the Google Sheet, check the flight prices for each destination, and send a notification if the price is below the threshold.

You can adjust the following parameters in the code to customize the search:
- `ORIGIN_CITY_IATA`: The IATA code of the origin city.
- `from_departure_dt`: The departure date of the flight.
- `to_departure_dt`: The return date of the flight.
- `destination["lowestPrice"]`: The lowest price for the destination.

## Dependencies
This app requires the following dependencies:
- `requests`
- `twilio`
- `datetime`
- `timedelta`

These dependencies can be installed using pip by running `pip install -r requirements.txt`.
