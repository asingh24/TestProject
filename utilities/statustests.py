"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the results

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.selenium_driver import PageElements
import utilities.custom_logger as cl
import logging


class StatusTests(PageElements):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super().__init__(driver)
        self.resultList = []


    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("--- VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("--- VERIFICATION FAILED :: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL, RESULT VALUE IN 'setResult' METHOD IS NONE")
                self.resultList.append(" --- VERIFICATION FAILED IN 'setResult' METHOD")
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error(" --- EXCEPTION OCCURRED !!!")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)


    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " --- FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " --- PASSED")
            self.resultList.clear()
            assert True == True
