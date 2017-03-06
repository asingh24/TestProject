import string
import random
from datetime import datetime
from BackEndTesting.tools.dbconnect import DBConnect

class Helper():
    """
    This is a class for function to be shared between test cases.
    Common tasks or tools go here.
    """
    qry = DBConnect()

    def __init__(self):
        pass


    def generate_random_info(self):
        """
        This generates random strings. The strings generated are for email, username, first name and last name.

        :return: info - dictionary containing the randomly generted info
        """

        info = {}

        # "Generating random stings for email and user_namee"
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        info['email'] = "api_user_" + stamp + "@gmail.com"
        info['user_name'] = "backend." + stamp

        # "Generating random strings for first_name and last_nam"
        all_letters = string.ascii_lowercase
        info['first_name'] = "".join(random.sample(all_letters, 8))
        info['last_name'] = "".join(random.sample(all_letters, 8))
        info['address_1'] = "101 " + "".join(random.sample(all_letters, 6))
        info['city'] = "".join(random.sample(all_letters, 5))

        # Generating random number for zip code
        info['postcode'] = random.randint(11111, 99999)


        print("The generated email: {}".format(info['email']))
        print("The generated user name: {}".format(info['user_name']))
        print("The generated first name: {}".format(info['first_name']))
        print("The generated last name: {}".format(info['last_name']))
        print("The generated billing address_1: {}".format(info['address_1']))
        print("The generated billing city: {}".format(info['city']))
        #print("The generated post code: "'{0:05d}'.format(info['postcode']))
        print("The generated post code: "'{:5}'.format(info['postcode']))

        return info


    def get_customer_info_from_db_provided_customer_id(self, cust_id):
        """
        Method to get customer info.
        :param cust_id:
        :return:
        """

        customer_db_info = {}

        # get the customer id and some info from the 'ak_users' table
        sql = "SELECT user_login, user_nicename, user_email, display_name FROM akstore.ak_users Where ID = {}".format(cust_id)
        cust = self.qry.select('akstore', sql)

        print(cust)
        customer_db_info['user_login'] = cust[0][0]
        customer_db_info['user_nicename'] = cust[0][1]
        customer_db_info['user_email'] = cust[0][2]
        customer_db_info['username'] = cust[0][3]

        # get the customers metadata from the 'aK_usermeta' table
        sql = "SELECT meta_key, meta_value FROM akstore.ak_usermeta WHERE user_id = {};".format(cust_id)
        cust_meta = self.qry.select('akstore', sql)
        #print(cust_meta)
        # lets add all the user meta data to the customer_db_info dictionary
        for row in cust_meta:
            customer_db_info[row[0]] = row[1]

        return customer_db_info
       # print(customer_db_info)

x =  Helper()
x.generate_random_info()