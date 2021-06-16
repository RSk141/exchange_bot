import requests


class api:
    url = "https://fxmarketapi.com/"
    params = {"api_key": "iyMIWmmUDBESp6Ix9J2E"}

    def get_curr(self):
        # get a list of all available currencies
        url_curr = self.url + "apicurrencies"
        resp_curr = requests.get(url_curr, params=self.params)
        keys = resp_curr.json()['currencies'].keys()
        currencies = ",".join(keys)
        return currencies

    def get_apilive(self):
        # get a json output of rates
        url_live = self.url + "apilive"
        params_live = {
            "api_key": "iyMIWmmUDBESp6Ix9J2E",
            "currency": self.get_curr()
        }
        resp_live = requests.get(url_live, params=params_live)
        return resp_live.json()

    def process_rates(self):
        # processing rates into user-friendly view and get timestamp
        curr = self.get_apilive()
        curr_rates = curr['price']
        curr_timestamp = curr['timestamp']
        prices = []
        for key, value in curr_rates.items():
            line = key[3:] + ': ' + str(round(value, 2))
            prices.append(line)
        return prices, curr_timestamp

    def convert_curr(self, from_curr, to_curr, amount_curr):
        # converting one curr into another
        params_conv = {
            'api_key': "iyMIWmmUDBESp6Ix9J2E",
            'from': from_curr,
            'to': to_curr,
            'amount': amount_curr
        }
        url_conv = self.url + "apiconvert"
        resp_conv = requests.get(url_conv, params=params_conv)
        price = round(resp_conv.json()['total'], 2)
        return price

    def get_history(self, curr, start_date, end_date):
        # returns history of asked currency
        params_hist = {
            'api_key': "iyMIWmmUDBESp6Ix9J2E",
            'currency': curr,
            'start_date': start_date,
            'end_date': end_date
        }
        url_hist = self.url + 'apipandas'
        resp_hist = requests.get(url_hist, params=params_hist)
        return resp_hist.text
