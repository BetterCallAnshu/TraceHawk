import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from utils import printer
from colorama import Style

class LookUp:
    """
    Looks up information about a given phone number.
    """

    def __init__(self, no) -> None:
        try:
            ph_no = phonenumbers.parse(no)
            country = phonenumbers.region_code_for_country_code(ph_no.country_code)
            no_carrier = carrier.name_for_number(ph_no, "en")
            no_valid = phonenumbers.is_valid_number(ph_no)
            no_possible = phonenumbers.is_possible_number(ph_no)
            time_zone = timezone.time_zones_for_number(ph_no)
            region = geocoder.description_for_number(ph_no, "en")

            printer.info(f"Trying to find information about {Style.BRIGHT}{no}{Style.RESET_ALL}...")
            time.sleep(1)
            printer.success(f"Phone Number - {no}")
            printer.success(f"Valid Number - {no_valid}")
            printer.success(f"Possible Number - {no_possible}")
            printer.success(f"Sim Provider - {no_carrier}")
            printer.success(f"Country - {country}")
            printer.success(f"Region - {region}")
            printer.success(f"Time Zone - {time_zone}")

        except Exception as e:
            printer.error(f"Error: {e}")
