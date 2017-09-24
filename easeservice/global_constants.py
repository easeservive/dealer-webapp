service_types = {
    'j4j5b67l': {'service_type': 'Paid Service', 'classification': 'Oil Change'},
    '5s5d5f5g': {'service_type': 'Paid Service', 'classification': 'General Service'},

    's7s9dkf9': {'service_type': 'Running Repairs', 'classification': 'Major Job'},

    'dkfd9ndf': {'service_type': 'Accidental Repairs', 'classification': 'Dent Removal'},
    '0o5s7j8g': {'service_type': 'Accidental Repairs', 'classification': 'Tinkering & Painting'},
    '9i90o0id': {'service_type': 'Accidental Repairs', 'classification': 'Rubbing & Polishing'},

    'pg7g8h8j': {'service_type': 'Water Wash', 'classification': 'Full Vehicle Wash'},
    'a8k5hj6g': {'service_type': 'Water Wash', 'classification': 'Interior & Exterior Cleaning'},
    'h8h9hljk': {'service_type': 'Water Wash', 'classification': 'Body Wash'},

    'default': {'service_type': 'Not Available', 'classification': 'Not Available'}
}

service_types_dropdown = [
    {
        "service_type_name": "Paid-Service",
        "classifications": [
            {'id': 'j4j5b67l', 'name': 'Oil Change', 'selected': False},
            {'id': '5s5d5f5g', 'name': 'General Service', 'selected': False}
        ]
    },
    {
        "service_type_name": "Running-Repairs",
        "classifications": [
            {'id': 's7s9dkf9', 'name': 'Major Job', 'selected': False}
        ]
    },
    {
        "service_type_name": "Accidental-Repairs",
        "classifications": [
            {'id': 'dkfd9ndf', 'name': 'Dent Removal', 'selected': False},
            {'id': '0o5s7j8g', 'name': 'Tinkering & Painting', 'selected': False},
            {'id': '9i90o0id', 'name': 'Rubbing & Polishing', 'selected': False}
        ]
    },
    {
        "service_type_name": "Water-Wash",
        "classifications": [
            {'id': 'pg7g8h8j', 'name': 'Full Vehicle Wash', 'selected': False},
            {'id': 'a8k5hj6g', 'name': 'Interior & Exterior Cleaning', 'selected': False},
            {'id': 'h8h9hljk', 'name': 'Body Wash', 'selected': False}
        ]
    },

]

class ResponseMessages(object):

    MOBILE_VERIFICATION_LINK = "A verification link has been sent to your mobile, please verify by clicking on it."

    LOGIN_VERIFICATION = "Sorry, the account has to be verified and activated by admin before you can login."