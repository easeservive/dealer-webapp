import requests
from django.conf import settings

def send_text_message(receiver, message):

    if not settings.SMS_BLOCK:
        message_response = requests.get(
            "http://login.bulksmsgateway.in/sendmessage.php?user=%s&password=%s&message=%s&sender=%s&mobile=%s&type=3" \
            % (settings.SMS_GATEWAY['USER'], settings.SMS_GATEWAY['PASSWORD'], message, settings.SMS_GATEWAY['SENDER'], receiver)
        )

        print(message_response.json())

    pass