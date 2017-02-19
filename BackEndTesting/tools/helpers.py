import string
import random
from datetime import datetime

class Helper():
    """
    This is a class for function to be shared between test cases.
    Common tasks or tools go here.
    """

    def __init__(self):
        pass

    def generate_random_info(self):
        """
        This generates random strings. The strings generated are for email, username, first name and last name.

        :return: info - dictionary containing the randomly generted info
        """

        info = {}

        print("Generating random stings for email and user_namee")
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        info['email'] = "api_user_" + stamp + "@gmail.com"
        info['user_name'] = "backend." + stamp

        print("Generating random strings for first_name and last_nam")
        all_letters = string.ascii_lowercase
        info['first_name'] = "".join(random.sample(all_letters, 8))
        info['last_name'] = "".join(random.sample(all_letters, 8))

        print("The generated email: {}".format(info['email']))
        print("The generated user name: {}".format(info['user_name']))
        print("The generated first name: {}".format(info['first_name']))
        print("The generated last name: {}".format(info['last_name']))

        return info
