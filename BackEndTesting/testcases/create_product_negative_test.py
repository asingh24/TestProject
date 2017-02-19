from TestProject.BackEndTesting.tools.request import REQ

rq = REQ()

def test_ng_tc1_product_empty_payload():

    """
    Negative test case for 'products' endpoint. Try to create a product with empty payload and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    input_data = {}
    info = rq.post('products', input_data)

    tc = 'EMPTY INPUT DATA'
    expected_message = "No product data specified to create product"
    expected_error_code = "woocommerce_api_missing_product_data"

    verify_ng_test_response(info, tc, expected_message, expected_error_code)


def test_ng_tc2_product_missing_title_key_in_payload():
    """
    Negative test case for 'products' endpoint. Try to create a product with missing parameter 'title'. Title is a
    required parameter. Making the call with no 'title' and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'

    input_data["product"] = product
    info = rq.post('products', input_data)


    tc = 'OMITTING TITLE PARAMETER'
    expected_message = "Missing parameter title"
    expected_error_code = "woocommerce_api_missing_product_title"

    verify_ng_test_response(info, tc, expected_message, expected_error_code)



def test_ng_tc3_product_empty_sting_for_title_in_payload():
    """
    Negative test case for 'products' endpoint. Try to create a product with empty sting for parameter 'title' in the
    payload. Title is a required parameter. Making the call with no 'title' and verify the response is error.
    Verify the response_code, the error message, and the error code.
    """

    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'
    product["title"] = ''

    input_data["product"] = product
    info = rq.post('products', input_data)

    tc = 'EMPTY TITLE STRING'
    expected_message = "Content, title, and excerpt are empty."
    expected_error_code = "woocommerce_api_cannot_create_product"

    verify_ng_test_response(info, tc, expected_message, expected_error_code)



def verify_ng_test_response(response_list, test_case, exp_error_msg, exp_error_code):
    """
    Function to verify the response of the negative test cases.

    Args:
        response_list - the response of the call as a list. the has elements status code, response body and url
        test_case - the name of the test case (string)
        exp_err_msg - the expected error message
        exp_err_code - the expected error code
    """

    # verify response code
    status_code = response_list[0]
    if status_code == 400:
        print("Test Case {tc}: The HTTP response Codes MATCH, EXPECTED VALUE: 400 and ACTUAL VALUE: {act}".format
                                                                             (tc = test_case, act = str(status_code)))
    else:
        print("Test Case {tc}: The HTTP response Codes DO NOT MATCH, EXPECTED VALUE: 400 and ACTUAL VALUE: {act}".format
                                                                             (tc = test_case, act = str(status_code)))

    # verify there is key 'errors' in the response
    response_body = response_list[1]
    if 'errors' in response_body.keys():
        print("Test Case {tc}: The Response body does have 'Errors' as key".format(tc=test_case))
    else:
        print("Test Case {tc}: The Response body does NOT have 'Errors' as key".format(tc=test_case))


    # verify the content of the error message
    act_error_msg = response_body['errors'][0]['message']
    if exp_error_msg == act_error_msg:
        print("Test Case {tc}: The Error messages MATCH. Expected: {exp} and Actual: {act}".format(tc = test_case,
                                                                        exp = exp_error_msg, act = act_error_msg))
    else:
        print("Test Case {tc}: The Error messages DO NOT MATCH. Expected: {exp} and Actual: {act}".format(tc = test_case,
                                                                        exp = exp_error_msg, act = act_error_msg))

    # verify the error code in the response
    act_error_code = response_body['errors'][0]['code']
    if exp_error_code == act_error_code:
        print("Test Case {tc}: The Error Codes MATCH. Expected: {exp} and Actual: {act}".format(tc = test_case,
                                                                        exp = exp_error_code, act = act_error_code))
    else:
        print("{tc}: The Error Codes DO NOT MATCH. Expected: {exp} and Actual: {act}".format(tc = test_case,
                                                                        exp = exp_error_code, act = act_error_code))

    print("Test Case '{tc}' -- PASS".format(tc = test_case))

test_ng_tc1_product_empty_payload()
test_ng_tc2_product_missing_title_key_in_payload()
test_ng_tc3_product_empty_sting_for_title_in_payload()