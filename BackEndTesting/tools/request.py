from woocommerce import API #pip install woocommerce # This package needs to be provided by the developer to access the API's

class REQ():

    def __init__(self):

        consumer_admin_key = "ck_f1d3d8d97e19a69835796d7ad5bf7511971620af"
        consumer_admin_secret = "cs_8dc071e9fbfefb6f38c23500838465bf6e011a6f"

        self.wcapi = API(url="http://127.0.0.1/akstore", consumer_key= consumer_admin_key,
                         consumer_secret= consumer_admin_secret, version="v3")


    def test_api(self):
        """

        :return:
        """
        print(self.wcapi.get("").json())



    def post(self, endpoint, data):
        """

        :param endpoint:
        :param data:
        :return:
        """
        result = self.wcapi.post(endpoint, data)

        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return (rs_code, rs_body, rs_url)


    def get(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        result = self.wcapi.get(endpoint)

        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return (rs_code, rs_body, rs_url)


    def wc_cust_delete(self, id):

        result = self.wcapi.delete("customers/" + str(id) + "?force=true")
        return(result).json()


    def wc_product_delete(self, id):

        result = self.wcapi.delete("products/" + str(id) + "?force=true")
        return(result).json()


x = REQ()
x.test_api()