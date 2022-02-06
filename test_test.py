from Main_page import Mail

def test_mail(browser):
    page=Mail(browser)
    page.go_to_site()                      
    page.go_to_login_page()
    page.login_password()
    page.write_message(page.find_mail())
    

