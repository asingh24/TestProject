from BackEndTesting.tools.request import REQ
from BackEndTesting.tools.dbconnect import DBConnect
from BackEndTesting.tools.helpers import Helper


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
    global email
    global user_name
    global first_name
    global last_name
    global address_1
    global city
    global postcode
    global customers

    print('TC1, customers, create new customer...')
    # generating random user info
    print('Generating random user info')
    #user_info = generate_random_info()
    user_info = help.generate_random_info()

    email = user_info['email']
    user_name = user_info['user_name']
    first_name = user_info['first_name']
    last_name = user_info['last_name']
    address_1 = user_info['address_1']
    city = user_info['city']
    postcode = user_info['postcode']

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
            "address_1": address_1,
            "address_2": "",
            "city": city,
            "state": "CA",
            "postcode": postcode,
            "country": "US",
            "email": email,
            "phone": "(555) 555-5555"
        },
        "shipping_address": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": address_1,
            "address_2": "",
            "city": city,
            "state": "CA",
            "postcode": postcode,
            "country": "US"
                }
            }
        }
    expected_info_dict = input_data['customer']

    print(str(expected_info_dict))


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
                                            "Expected: {exp}, Actual: {act}".format(exp=response_body["email"],
                                                                                    act=email)

    assert response_body["username"] == user_name, "'username' in response is not as expected." \
                                                   " Expected: {exp}, Actual: {act}".format(exp=response_body["username"],
                                                                                            act=user_name)

    assert response_body["first_name"] == first_name, "'first_name' in response is not as expected." \
                                                      " Expected: {exp}, Actual: {act}".format(exp=response_body["first_name"],
                                                                                               act=first_name)

    assert response_body["last_name"] == last_name, "'last_name' in response is not as expected. " \
                                                    "Expected: {exp}, Actual: {act}".format(exp=response_body["last_name"],
                                                                                            act=last_name)

    print('PASS - Test Case: create customer happy path')


# def test_verify_customer_info_in_db():
#     """
#     Verifies customer info in DB.
#
#     Globals:
#         customer_id
#     """
#
#     db_info = help.get_customer_info_from_db_provided_customer_id(customer_id)
#
#     # failed_list = []
#     # for key, value in expected_info_dict.items():
#     #     print(key)
#     #     print(value)
#     #     if db_info[key] != value:
#     #         msg = 'Bad value for {key} in db. Payload value: {pl}, DB value: {db}'.format(key=key,pl=value, db=db_info[key])
#     #         failed_list.append(msg)
#     #
#     # if failed_list:
#     #     raise Exception("There are failed values for created customer in db. Failed items are: {}".format(failed_list))
#     # else:
#     #     print("DB verification for create customer PASS!!!")
#
#     if db_info.items() in expected_info_dict.items():
#         print("Expected and Actual values Match in DB")
#     else:
#         print("Expected and Actual values do not Match in the DB")

def test_verify_customer_info_in_db(customer_id):
    customer_db_info = {}

    # get the customer id and some info from the 'ak_users' table
    sql = "SELECT user_login, user_email, display_name FROM akstore.ak_users Where ID = {}".format(
        customer_id)
    cust = qry.select('akstore', sql)
    print(cust)

    user_login_db = customer_db_info['user_login'] = cust[0][0]
    user_email_db = customer_db_info['user_email'] = cust[0][1]
    username_db = customer_db_info['username'] = cust[0][2]
    #print(customer_db_info)

    # get the customers metadata from the 'aK_usermeta' table
    customer_meta_db_info = {}
    sql = "SELECT meta_key, meta_value from akstore.ak_usermeta where meta_key in ('billing_first_name', " \
          "'billing_last_name','billing_address_1', 'billing_city', 'billing_postcode'," \
          "'billing_email', 'shipping_first_name','shipping_last_name', 'shipping_address_1', " \
          "'shipping_city', 'shipping_postcode') and user_id = {};".format(customer_id)
    cust_meta = qry.select('akstore', sql)
    print(cust_meta)

    billing_firstname_db = customer_meta_db_info['billing_first_name'] = cust_meta[0][1]
    billing_lastname_db = customer_meta_db_info['billing_last_name'] = cust_meta[1][1]
    billing_address1_db = customer_meta_db_info['billing_address_1'] = cust_meta[2][1]
    billing_city_db = customer_meta_db_info['billing_city'] = cust_meta[3][1]
    billing_postcode_db = customer_meta_db_info['billing_postcode'] = cust_meta[4][1]
    billing_email_db = customer_meta_db_info['billing_email'] = cust_meta[5][1]

    shipping_firstname_db = customer_meta_db_info['shipping_first_name'] = cust_meta[6][1]
    shipping_lastname_db = customer_meta_db_info['shipping_last_name'] = cust_meta[7][1]
    shipping_address1_db = customer_meta_db_info['shipping_address_1'] = cust_meta[8][1]
    shipping_city_db = customer_meta_db_info['shipping_city'] = cust_meta[9][1]
    shipping_postcode_db = customer_meta_db_info['shipping_postcode'] = cust_meta[10][1]


    if user_login_db == user_name:
        print("The Expected and Actual Userlogin values in DB MATCH")
    else:
        print("The Expected and Actual username values in DB DO NOT MATCH. EXPECTED VALUE: "
              + user_name + " and ACTUAL VALUE " + user_login_db)

    if user_email_db == email:
        print("The Expected and Actual EMail values in DB MATCH")
    else:
        print("The Expected and Actual Email values in DB DO NOT MATCH. EXPECTED VALUE: "
              + email + " and ACTUAL VALUE " + user_email_db)

    if username_db == user_name:
        print("The Expected and Actual Username values in DB MATCH")
    else:
        print("The Expected and Actual username values in DB DO NOT MATCH. EXPECTED VALUE: "
              + user_name + " and ACTUAL VALUE " + username_db)

    if billing_firstname_db == first_name:
        print("The Expected and Actual First Name values in DB MATCH")
    else:
        print("The Expected and Actual First name values in DB DO NOT MATCH. EXPECTED VALUE: "
              + first_name + " and ACTUAL VALUE " + billing_firstname_db)

    if billing_lastname_db == last_name:
        print("The Expected and Actual Last Name values in DB MATCH")
    else:
        print("The Expected and Actual Last Name values in DB DO NOT MATCH. EXPECTED VALUE: "
              + last_name + " and ACTUAL VALUE " + billing_lastname_db)

    if billing_address1_db == address_1:
        print("The Expected and Actual Billing Address 1 values in DB MATCH")
    else:
        print("The Expected and Actual Billing Address 1 values in DB DO NOT MATCH. EXPECTED VALUE: "
              + address_1 + " and ACTUAL VALUE " + billing_address1_db)

    if billing_city_db == city:
        print("The Expected and Actual city values in DB MATCH")
    else:
        print("The Expected and Actual city values in DB DO NOT MATCH. EXPECTED VALUE: "
              + city + " and ACTUAL VALUE " + billing_city_db)

    if str(billing_postcode_db) == str(postcode):
        print("The Expected and Actual Postcode values in DB MATCH")
    else:
        print("The Expected and Actual Postcode values in DB DO NOT MATCH. EXPECTED VALUE: "
              + str(postcode) + " and ACTUAL VALUE " + str(billing_postcode_db))

    if billing_email_db == email:
        print("The Expected and Actual Billing Email values in DB MATCH")
    else:
        print("The Expected and Actual Billing Email values in DB DO NOT MATCH. EXPECTED VALUE: "
              + email + " and ACTUAL VALUE " + billing_email_db)



    if shipping_firstname_db == first_name:
        print("The Expected and Actual Shipping Address First Name values  in DB MATCH")
    else:
        print("The Expected and Actual Shipping Address First name values in DB DO NOT MATCH. EXPECTED VALUE: "
              + first_name + " and ACTUAL VALUE " + billing_firstname_db)

    if shipping_lastname_db == last_name:
        print("The Expected and Actual Shipping Address Last Name values in DB MATCH")
    else:
        print("The Expected and Actual Shipping Address Last Name values in DB DO NOT MATCH. EXPECTED VALUE: "
              + last_name + " and ACTUAL VALUE " + billing_lastname_db)

    if shipping_address1_db == address_1:
        print("The Expected and Actual Shipping Address 1 values in DB MATCH")
    else:
        print("The Expected and Actual Shipping Address 1 values in DB DO NOT MATCH. EXPECTED VALUE: "
              + address_1 + " and ACTUAL VALUE " + billing_address1_db)

    if shipping_city_db == city:
        print("The Expected and Actual Shipping Address city values in DB MATCH")
    else:
        print("The Expected and Actual Shipping Address city values in DB DO NOT MATCH. EXPECTED VALUE: "
              + city + " and ACTUAL VALUE " + billing_city_db)

    if str(shipping_postcode_db) == str(postcode):
        print("The Expected and Actual Shipping Address Postcode values in DB MATCH")
    else:
        print("The Expected and Actual Shipping Address Postcode values in DB DO NOT MATCH. EXPECTED VALUE: "
              + str(postcode) + " and ACTUAL VALUE " + str(billing_postcode_db))


def test_customer_delete():
    '''
    deleting the customer created above, the main delete function resides in request.py
    :return:
    '''

    cust_delete = rq.wc_cust_delete(customer_id)
    print(cust_delete)







test_create_customer()
test_verify_customer_info_in_db(customer_id)
test_customer_delete()

