import random, string
import self as self


class TestData:
    homepage_url = "https://magento.softwaretestingboard.com/"
    sign_up_url = "https://magento.softwaretestingboard.com/customer/account/create/"
    log_in_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/"

    # create random first name
    def create_first_name(self, length=6, chars=string.ascii_lowercase):
        first_name = ''.join(random.choice(chars) for i in range(length))
        return first_name

    first_name = create_first_name(self)

    # create random last name
    def create_last_name(self, length=6, chars=string.ascii_lowercase):
        last_name = ''.join(random.choice(chars) for i in range(length))
        return last_name

    last_name = create_first_name(self)

    # create random email
    def create_email(self, length=7, chars=string.ascii_lowercase):
        email_address = ''.join(random.choice(chars) for i in range(length))
        return email_address + "@email.com"
    email_address = create_email(self)

    password = "test123!"
    confirm_password = "test123!"


    log_in_email = "hjmm@gfgr.com"
    log_in_password = "test123!"
