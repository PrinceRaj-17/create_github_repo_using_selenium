from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromeBot = webdriver.Chrome(<enter_your_chromedriver_location>)


class Github:

	def __init__(self, userId, password):
		self.userId =  userId
		self.password = password

	def login(self):

		github_login_url = "https://github.com/login"
		chromeBot.get(github_login_url)

		userId = chromeBot.find_element_by_id("login_field")
		userId.send_keys(self.userId)

		password = chromeBot.find_element_by_id("password")
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)

		# In Case Of an OTP verification you can pause the program until you enter your OTP by uncommenting the line below
		#time.sleep(20)

	def create_repo(self, repo_name):

		chromeBot.get("https://github.com/new")

		repo = chromeBot.find_element_by_id("repository_name")
		repo.send_keys(repo_name)

		time.sleep(1)
		
		repo.send_keys(Keys.RETURN)




github = Github(<your_userID>, <your_password>)

github.login()

github.create_repo(<your_repo_name>)

