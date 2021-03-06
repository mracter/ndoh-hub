import responses


# Mocks used in testing
def mock_get_identity_by_id(identity_id):
    identity = {
        "id": identity_id,
        "version": 1,
        "details": {
            "foo": "bar",
            "lang_code": "afr_ZA"
        },
        "communicate_through": None,
        "operator": None,
        "created_at": "2016-03-31T09:28:29.506591Z",
        "created_by": None,
        "updated_at": "2016-08-17T09:44:31.812532Z",
        "updated_by": 1
    }

    responses.add(
        responses.GET,
        'http://is/api/v1/identities/%s/' % identity_id,
        json=identity,
        status=200, content_type='application/json'
    )


def mock_patch_identity(identity_id):
    patched_identity = {
        "id": identity_id,
        "version": 1,
        "details": {
            "foo": "bar",
            "risk": "high"
        },
        "communicate_through": None,
        "operator": None,
        "created_at": "2016-03-31T09:28:29.506591Z",
        "created_by": None,
        "updated_at": "2016-08-17T09:44:31.812532Z",
        "updated_by": 1
    }

    responses.add(
        responses.PATCH,
        'http://is/api/v1/identities/%s/' % identity_id,
        json=patched_identity,
        status=200, content_type='application/json'
    )


def mock_get_messageset_by_shortname(short_name):
    messageset_id = {
        "pmtct_prebirth.patient.1": 11,
        "pmtct_prebirth.patient.2": 12,
        "pmtct_prebirth.patient.3": 13,
        "pmtct_postbirth.patient.1": 14,
        "pmtct_postbirth.patient.2": 15,
        "momconnect_prebirth.hw_full.1": 21,
        "momconnect_prebirth.hw_full.2": 22,
        "momconnect_prebirth.hw_full.3": 23,
        "momconnect_prebirth.hw_full.4": 24,
        "momconnect_prebirth.hw_full.5": 25,
        "momconnect_prebirth.hw_full.6": 26,
        "momconnect_postbirth.hw_full.1": 31,
        "momconnect_postbirth.hw_full.2": 32,
        "momconnect_prebirth.patient.1": 41,
        "momconnect_prebirth.hw_partial.1": 42,
        "loss_miscarriage.patient.1": 51,
        "loss_stillbirth.patient.1": 52,
        "loss_babyloss.patient.1": 53,
        "nurseconnect.hw_full.1": 61
    }[short_name]

    default_schedule = {
        "pmtct_prebirth.patient.1": 111,
        "pmtct_prebirth.patient.2": 112,
        "pmtct_prebirth.patient.3": 113,
        "pmtct_postbirth.patient.1": 114,
        "pmtct_postbirth.patient.2": 115,
        "momconnect_prebirth.hw_full.1": 121,
        "momconnect_prebirth.hw_full.2": 122,
        "momconnect_prebirth.hw_full.3": 123,
        "momconnect_prebirth.hw_full.4": 124,
        "momconnect_prebirth.hw_full.5": 125,
        "momconnect_prebirth.hw_full.6": 126,
        "momconnect_postbirth.hw_full.1": 131,
        "momconnect_postbirth.hw_full.2": 132,
        "momconnect_prebirth.patient.1": 141,
        "momconnect_prebirth.hw_partial.1": 142,
        "loss_miscarriage.patient.1": 151,
        "loss_stillbirth.patient.1": 152,
        "loss_babyloss.patient.1": 153,
        "nurseconnect.hw_full.1": 161
    }[short_name]

    responses.add(
        responses.GET,
        'http://sbm/api/v1/messageset/?short_name=%s' % short_name,
        json={
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{
                "id": messageset_id,
                "short_name": short_name,
                "default_schedule": default_schedule
            }]
        },
        status=200, content_type='application/json',
        match_querystring=True
    )
    return default_schedule


def mock_get_messageset(messageset_id):
    short_name = {
        11: "pmtct_prebirth.patient.1",
        12: "pmtct_prebirth.patient.2",
        13: "pmtct_prebirth.patient.3",
        14: "pmtct_postbirth.patient.1",
        15: "pmtct_postbirth.patient.2",
        21: "momconnect_prebirth.hw_full.1",
        22: "momconnect_prebirth.hw_full.2",
        23: "momconnect_prebirth.hw_full.3",
        24: "momconnect_prebirth.hw_full.4",
        25: "momconnect_prebirth.hw_full.5",
        26: "momconnect_prebirth.hw_full.6",
        31: "momconnect_postbirth.hw_full.1",
        32: "momconnect_postbirth.hw_full.2",
        41: "momconnect_prebirth.patient.1",
        42: "momconnect_prebirth.hw_partial.1",
        51: "loss_miscarriage.patient.1",
        52: "loss_stillbirth.patient.1",
        53: "loss_babyloss.patient.1",
        61: "nurseconnect.hw_full.1"
    }[messageset_id]

    default_schedule = {
        "pmtct_prebirth.patient.1": 111,
        "pmtct_prebirth.patient.2": 112,
        "pmtct_prebirth.patient.3": 113,
        "pmtct_postbirth.patient.1": 114,
        "pmtct_postbirth.patient.2": 115,
        "momconnect_prebirth.hw_full.1": 121,
        "momconnect_prebirth.hw_full.2": 122,
        "momconnect_prebirth.hw_full.3": 123,
        "momconnect_prebirth.hw_full.4": 124,
        "momconnect_prebirth.hw_full.5": 125,
        "momconnect_prebirth.hw_full.6": 126,
        "momconnect_postbirth.hw_full.1": 131,
        "momconnect_postbirth.hw_full.2": 132,
        "momconnect_prebirth.patient.1": 141,
        "momconnect_prebirth.hw_partial.1": 142,
        "loss_miscarriage.patient.1": 151,
        "loss_stillbirth.patient.1": 152,
        "loss_babyloss.patient.1": 153,
        "nurseconnect.hw_full.1": 161
    }[short_name]

    responses.add(
        responses.GET,
        'http://sbm/api/v1/messageset/%s/' % messageset_id,
        json={
            'id': messageset_id,
            'short_name': short_name,
            'notes': None,
            'next_set': 10,
            'default_schedule': default_schedule,
            'content_type': 'text',
            'created_at': "2016-06-22T06:13:29.693272Z",
            'updated_at': "2016-06-22T06:13:29.693272Z"
        }
    )


def mock_get_schedule(schedule_id):
    day_of_week = {
        111: "1",
        112: "1,4",
        113: "1,3,5",
        114: "1,4",
        115: "1",
        121: "1,4",
        122: "1,3,5",
        123: "1,3,5",
        124: "1,2,3,4",
        125: "1,2,3,4,5",
        126: "1,2,3,4,5,6,7",
        131: "1,4",
        132: "1",
        141: "1,4",
        142: "1,4",
        151: "1,4",
        152: "1,4",
        153: "1,4",
        161: "1,3,5"
    }[schedule_id]

    responses.add(
        responses.GET,
        'http://sbm/api/v1/schedule/%s/' % schedule_id,
        json={"id": schedule_id, "day_of_week": day_of_week},
        status=200, content_type='application/json',
    )
