import json
import os
import psycopg2
import requests


class Invoice:
    def __init__(self, amount, buyer_address, api_key, store_id):
        self.api_key = api_key
        self.amount = amount
        self.buyer_address = buyer_address
        self.store_id = store_id
        self.url = "https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC"

    def create_json_payload(self, amount, buyer_address):
        payload = {
            "metadata": {
                "buyerAddress1": buyer_address,
            },
            "checkout": {
                "speedPolicy": "HighSpeed",
                "paymentMethods": [
                    "BTC"
                ],
                "defaultPaymentMethod": "string",
                "expirationMinutes": 20,
                "monitoringMinutes": 1440,
                "redirectAutomatically": "true",
                "requiresRefundEmail": "true",
            },
            "receipt": {
                "enabled": "true",
                "showQR": "null",
                "showPayments": "null"
            },
            "amount": amount,
            "currency": "BTC",
        }
        # convert to json
        return json.dumps(payload)

    def post_invoice(self):
        payload = self.create_json_payload(self.amount, self.buyer_address)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + self.api_key,
        }
        response = requests.request("POST", self.url, headers=headers, data=payload)
        return response

    def save_invoice(self):
        sql = """INSERT INTO "Invoices"(amount, "currency", "address")
                    VALUES(%s, %s, %s) returning "Invoices"."id";"""
        conn = None
        id = None
        try:
            conn = psycopg2.connect(
                host=os.environ.get("DB_HOST"),
                database=os.environ.get("DB_NAME"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"))
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (self.amount, self.buyer_address, 'BTC'))
            # get the generated id back
            id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return id



if __name__ == '__main__':

    while True:
        #check for new orders
        # todo
        # orders = get_new_orders()
        orders = [{
            "id": 1,
            "amount": 0.0001,
            "address": "xpub6Bng2EukGQoAjSwW7MjRkC4aKSYsNRBXV9BB3V7FoqetKce4dBg91SLWa37ZozCa744PaTCudU7vYTGw7VrQrZuFgHdsVPzFWKXWoKBWTEK"
        }]

        while orders:
            #get the order
            order = orders.pop()
            #create the invoice
            invoice = Invoice(order.amount, order.address, os.environ.get("APIKey"), os.environ.get("APIKey"))
            #post the invoice
            response = invoice.post_invoice()
            #save invoice in db
            invoice.save_invoice()

        time.sleep(60)
        #check for new orders
        # to do
        # orders = get_new_orders()
        orders.append({
            "id": 1,
            "amount": 0.0001,
            "address": "xpub6Bng2EukGQoAjSwW7MjRkC4aKSYsNRBXV9BB3V7FoqetKce4dBg91SLWa37ZozCa744PaTCudU7vYTGw7VrQrZuFgHdsVPzFWKXWoKBWTEK"}
        )
