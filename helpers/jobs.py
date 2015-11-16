import schedule
import time
import FHIR
import FitbitAPI

schedule.every(60).minutes.do(sync_all_the_things)


def sync_all_the_things():
    # TODO: make this into a list of all users
    user_ids = [333, 444, 555]

    fitbit = FitbitAPI()

    for user_id in user_ids:
        recent_actvity = fitbit.pull(user_id)

    fhir = FHIR()
