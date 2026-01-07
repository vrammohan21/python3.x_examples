import os
from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
# It's best practice to use environment variables for sensitive info
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    print("Please set your TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables.")
else:
    client = Client(account_sid, auth_token)
    phone_number_to_check=input("Enter a phone number:")

    try:
        phone_number = client.lookups \
                             .v2 \
                             .phone_numbers(phone_number_to_check) \
                             .fetch(fields='line_type_intelligence')

        print(f"Number: {phone_number_to_check}")
        print(f"Line type intelligence: {phone_number.line_type_intelligence}")

        # This will return details like line_type, carrier_name, and if it's a prepaid number
        carrier_name = phone_number.line_type_intelligence.get('carrier_name')
        line_type = phone_number.line_type_intelligence.get('type')

        print(f"Carrier: {carrier_name}")
        print(f"Line type: {line_type}")

    except Exception as e:
        print(f"Error looking up number: {e}")
