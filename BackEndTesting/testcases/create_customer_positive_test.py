from TestProject.BackEndTesting.tools.request import REQ
from TestProject.BackEndTesting.tools.dbconnect import DBConnect
from TestProject.BackEndTesting.tools.helpers import Helper


rq = REQ()
qry = DBConnect()
help = Helper()

def test_create_customer():
    """
    One happy path test. It will provide all the required and optional fields then verify that the response is as expected
    and also the database entry is as expected.
    """
    global customer_id
    global expected_info_dict

    print('TC1, customers, create new customer...')
    # generating random user info
    print('Generating random user info')
    #user_info = generate_random_info()
    user_info = help.generate_random_info()

    email = user_info['email']
    user_name = user_info['user_name']
    first_name = user_info['first_name']
    last_name = user_info['last_name']

    input_data = {
    "customer": {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "username": user_name,
        "password": "test123",
        "billing_address": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US",
            "email": email,
            "phone": "(555) 555-5555"
        },
        "shipping_address": {
            "first_name": last_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US"
                }
            }
        }
    expected_info_dict = input_data['customer']
    rs = rq.post('customers', input_data)

    print(rs)
    print('verifying response')
    # verify the status code before attempting to parse the response data. There may not be response data
    status_code = rs[0]
    if status_code == 201:
        print("The HTTP Response Codes MATCH, EXPECTED VALUE: 201 and ACTUAL VALUE: " + str(status_code))
    else:
        print("The HTTP Response Codes DID NOT MATCH, EXPECTED VALUE: 201 and ACTUAL VALUE: " + str(status_code))

    # if call is successful then get the response body
    response_body = rs[1]['customer']
    customer_id = response_body['id']
    print(response_body)
    print(customer_id)

    # start verification
    assert response_body["email"] == email, "'email' in response is not as expected. " \
                                            "Expected: {exp}, Actual: {act}".format(exp=response_body["email"], act=email)

    assert response_body["username"] == user_name, "'username' in response is not as expected." \
                                                   " Expected: {exp}, Actual: {act}".format(exp=response_body["username"], act=user_name)

    assert response_body["first_name"] == first_name, "'first_name' in response is not as expected." \
                                                      " Expected: {exp}, Actual: {act}".format(exp=response_body["first_name"], act=first_name)

    assert response_body["last_name"] == last_name, "'last_name' in response is not as expected. " \
                                                    "Expected: {exp}, Actual: {act}".format(exp=response_body["last_name"], act=last_name)

    print('PASS - Test Case: create customer happy path')


# def test_verify_customer_info_in_db():
#     """
#     Verifies customer info in DB.
#
#     Globals:
#         customer_id
#     """
#
#     db_info = helper.get_customer_info_from_db_provided_customer_id(customer_id)
#
#     failed_list = []
#     for key, value in expected_info_dict.items():
#         print(key)
#         print(value)
#         if db_info[key] != value:
#             msg = 'Bad value for {key} in db. Payload value: {pl}, DB value: {db}'.format(key=key,pl=value, db=db_info[key])
#             failed_list.append(msg)
#
#     if failed_list:
#         raise Exception("There are failed values for created customer in db. Failed items are: {}".format(failed_list))
#     else:
#         print("DB verification for create customer PASS!!!")



test_create_customer()
