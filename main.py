from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "FRA"

iata_codes = [row["iataCode"] for row in sheet_data]
if "" in iata_codes:
    for row in sheet_data:
        if row["iataCode"] == "":
            location = row["city"]
            row["iataCode"] = flight_search.get_destination_code(location)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# date_departure = datetime.now() + timedelta(days=1)
from_departure_dt = "2023-10-16"
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
to_departure_dt = "2023-11-12"


for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=from_departure_dt,
        to_time=to_departure_dt
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        body_text = f"Niedrig Preisalarm Euro {flight.price} fur Flug von {flight.origin_city}-{flight.origin_airport} zu {flight.destination_city}-{flight.destination_airport}, von  {flight.out_date} zu {flight.return_date}. \n gehe zu {flight.deep_link}"
        notification_manager.send_mail(
            body=body_text
        )
    if flight.stop_overs > 0:
        body_text = f"Niedrig Preisalarm Euro {flight.price} fur Flug von {flight.origin_city}-{flight.origin_airport} zu {flight.destination_city}-{flight.destination_airport}, von  {flight.out_date} zu {flight.return_date}. \n gehe zu {flight.deep_link}"
        body_text_more_step_overs = body_text + f"\n\nFlug hat {flight.stop_overs} Flughafenwechsel, und geht ueber {flight.via_city}."
        notification_manager.send_mail(
            body=body_text_more_step_overs
        )
