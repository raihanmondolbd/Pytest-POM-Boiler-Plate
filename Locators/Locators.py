from selenium.webdriver.common.by import By


class Locators:
    userNameTextBox = (By.XPATH, '//input[@name="username"]')
    passwordTextBox = (By.XPATH, '//input[@name="password"]')
    loginButton = (By.XPATH, '//button[@type="submit"]')
    employeeList = (By.XPATH, '//a[contains(text(), "Employee List")]')
