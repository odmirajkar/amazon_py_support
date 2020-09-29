import unittest
from selenium_support import selenium_support
import time
import sys
import HtmlTestRunner
from os import path

class Test_ATT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.support=selenium_support()
        cls.support.init()
        url="https://www.amazon.in/"
        cls.support.driver.get(url)
        cls.support.take_screenshot('home.png')
        print(cls.support.driver.title)

    
    def test_signin_amazon(self):
        self.support.driver.get('https://www.amazon.in/')
        time.sleep(5)
        self.support.driver.find_element_by_xpath("//span[.='Hello, Sign in']").click()
        print("Sign in clicked")

        time.sleep(7)

        userid=self.support.driver.find_element_by_xpath('//*[@type="email"]')
        userid.send_keys('soumyajit2pal@gmail.com')

        self.support.driver.find_element_by_xpath("//*[@id='continue']").click()
        time.sleep(5)
        password=self.support.driver.find_element_by_xpath(".//*[@type='password']")
        password.send_keys('test@test')
        self.support.take_screenshot('login.png')
        signin_button=self.support.driver.find_element_by_xpath("//*[@id='signInSubmit']")
        signin_button.click()
        time.sleep(3)

        if self.support.driver.find_element_by_xpath("//h1[@class='a-spacing-small']").text == "Login":
            print("Login failed")

    def test_add_to_cart(self):
        self.support.driver.get('https://www.amazon.in/')

        time.sleep(5)

        self.support.driver.find_elements_by_xpath('.//*[@id="twotabsearchtextbox"]')[0].send_keys("Echo Dot (Black) bundle with Fire TV Stick")
        self.support.driver.find_element_by_xpath('//*[@value="Go"]').click()
        

        time.sleep(3)
        self.support.driver.find_element_by_xpath('//span[.="Echo Dot (Black) bundle with Fire TV Stick"]').click()
    
        after_click=self.support.driver.window_handles[1]
        self.support.driver.switch_to_window(after_click)
        self.support.take_screenshot('echo.png')
        print("switch to" +self.support.driver.title +"done")
        time.sleep(2)
        
        self.support.driver.find_element_by_xpath('//input[@id="add-to-cart-button"]').click()
        print("added to cart ")
	

    @classmethod
    def tearDownClass(cls):
        cls.support.driver.quit()    

        
def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
    #import os

    #module=os.path.splitext(os.path.basename(__file__))[0]
    #suite = loader.loadTestsFromName(module+'.TestCases.test_b')
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    print(suite)
    #unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
    #output_file = open("HTML_Test_Runner_ReportTest.txt", "w")
    if path.exists("/tmp"):
        report_filder='/tmp/report'
    else:
        report_filder='./report'

    html_runner = HtmlTestRunner.HTMLTestRunner(
        #    stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner',
            output=report_filder
        )
    #unittest.TestRunner()
    html_runner.run(suite)


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store', dest='config_value',help='Store a simple value')
    results = parser.parse_args()
    print ('config_value     =', results.config_value)
    Test_Zypher.config=results.config_value
    #unittest.main(verbosity=2)
    """
    
    main()
    #with open('testing.out', 'w') as f: 
    #    main(f)
