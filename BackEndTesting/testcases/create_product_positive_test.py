from TestProject.BackEndTesting.tools.request import REQ
from TestProject.BackEndTesting.tools.dbconnect import DBConnect
import json

# creating our object to be used to make API call and db connections
rq = REQ()
qry = DBConnect()

def test_create_a_product():

    """
    Function to make 'products' API call to create a product.
    Some value for payload are hardcoded, the call made and then the data in the response verified.
    """

    # set global variables to be used in different functions
    global product_id
    global title
    global price


    title = 'TEST1 TITLE'
    price = '9.99'
    input_data = {
                        'product':{
                            'title':title,
                            'type':'simple',
                            'regular_price':price}}

    info = rq.post('products', input_data)
    # print("The HTTP Response code is: "+ str(info[0]))
    # print(json.dumps(info[1], indent = 4))
    status_code = info[0]
    response_body = info[1]

    response_title = response_body["product"] ["title"]
    response_price = response_body["product"]["regular_price"]
    product_id = response_body["product"]["id"]

    if status_code == 201:
        print("The HTTP Response Codes MATCH, EXPECTED VALUE: 201 and ACTUAL VALUE: " + str(status_code))
    else:
        print("The HTTP Response Codes DID NOT MATCH, EXPECTED VALUE: 201 and ACTUAL VALUE: " + str(status_code))

    if  response_title == title:
        print("The Expected and Actual Product title values MATCH")
    else:
        print("The Expected and Actual Product title values DO NOT MATCH. EXPECTED VALUE: "
              + title + " and ACTUAL VALUE " + response_title)

    if  response_price == price:
        print("The Expected and Actual Product price values MATCH")
    else:
        print("The Expected and Actual Product price values DO NOT MATCH. EXPECTED VALUE: "
              + price + " and ACTUAL VALUE " + response_price)


def test_verify_product_created_in_db():
    """
    Function to query the data base and verify product is created with the correct information.

    Note:
        This function depends on the first function 'test_create_a_product()' being called first. The variables
        set in that function are used in this function.
    """


    sql ='''SELECT p.post_title, p.post_type, pm.meta_value FROM ak_posts p JOIN ak_postmeta pm
            ON p.id=pm.post_id WHERE p.id={} AND pm.meta_key='_regular_price' '''.format(product_id)
    qrs = qry.select('wp218', sql)

    # extracting the data
    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]


    if db_title == title:
        print("The Expected and Actual Product title values in DB MATCH")
    else:
        print("The Expected and Actual Product title values in DB DO NOT MATCH. EXPECTED VALUE: "
              + title + " and ACTUAL VALUE " + db_title)

    if db_type == 'product':
        print("The Expected and Actual DB Type values MATCH")
    else:
        print("The Expected and Actual DB Type values in DB DO NOT MATCH. EXPECTED VALUE: Product and ACTUAL VALUE "
              + db_type)

    if db_regular_price == price:
        print("The Expected and Actual Product price values in DB MATCH")
    else:
        print("The Expected and Actual Product price values In DB DO NOT MATCH. EXPECTED VALUE: "
              + price + " and ACTUAL VALUE " + db_regular_price)


test_create_a_product()
test_verify_product_created_in_db()