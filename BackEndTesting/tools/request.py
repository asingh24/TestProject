from woocommerce import API #pip install woocommerce # This package needs to be provided by the developer to access the API's

class REQ():

    def __init__(self):

        consumer_admin_key = "ck_86a0e8e0a15d8a38332a893bed6057de519e8694"
        consumer_admin_secret = "cs_87ad46417c09d8982badd6162185cc38f1591eb9"

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
