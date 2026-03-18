import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException

def get_phone_number_status(phone_number_str):
    """Parses and retrieves information for a given phone number."""
    try:
        # Parse the phone number string
        number = phonenumbers.parse(phone_number_str)

        # Check for validity and possibility
        is_valid = phonenumbers.is_valid_number(number)
        is_possible = phonenumbers.is_possible_number(number)

        print(f"Number: {phone_number_str}")
        print(f"Is valid: {is_valid}")
        print(f"Is possible: {is_possible}")
        
        if is_valid:
            # Get general location (region/country)
            location = geocoder.description_for_number(number, "en")
            print(f"Location: {location}")

            # Get carrier information
            service_provider = carrier.name_for_number(number, "en")
            print(f"Service provider: {service_provider}")
            
            # Get timezone
            tz = timezone.time_zones_for_number(number)
            print(f"Timezone: {tz}")

    except NumberParseException as e:
        print(f"Error parsing number: {e}")

# Example usage with a US mobile number +17730078005
user_input=input("Enter a phone number:")
get_phone_number_status(user_input)

# Example usage with an invalid number
#get_phone_number_status(user_input)
