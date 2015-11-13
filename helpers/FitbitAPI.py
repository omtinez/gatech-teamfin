import fitbit


class FitbitAPI:
    def __init__(self):
        # fitbit application credentials
        self.consumerKey = "13b47115d569d875827788c94a053506"
        self.consumerSecret = "358a5919f827330726ec84349ec8b640"

        # fitbit = 1
        # userId = "3S2Y3M"

        self.unauthfb = fitbit.Fitbit(client_key=self.consumerKey,
                        client_secret=self.consumerSecret)

    def pull(self, userId):
        states = self.unauthfb.activity_stats(userId)

        steps = states[u'lifetime'][u'total'][u'steps']
        distance = states[u'lifetime'][u'total'][u'distance']

        ret = {"Steps": steps, "Distance": distance}
        return ret


# if __name__ == "__main__":
#     fbapi = FitbitAPI()
#     print fbapi.pull("3S2Y3M")
