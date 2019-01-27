import argparse
from time import sleep
from selenium import webdriver, common
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager

###############################################################################
#                          ARGUMENT PARSING START                             #
###############################################################################

parser = argparse.ArgumentParser(prog="app", description="Options for customizing program")
parser.add_argument('-n', '--mbr', type=int, metavar="", help="Number of messages to ignore before sending the auto response again")
parser.add_argument('-m', '--message', type=str, metavar="", help="Message to display as an automated response")
parser.add_argument('-b', '--browser', type=str.lower, metavar="", help="Browser to use Whatsapp Web on [Chrome is default]", choices=['chrome', 'firefox', 'edge', 'ie'])
args = vars(parser.parse_args())

# Get --mbr command line argument value or assign a default
messages_before_response = 5 if args['mbr'] is None else args['mbr']

# Get --message command line argument value or assign a default
if args['message'] is None:
	response_message = "Sorry, I'm busy at the moment, will reply in a while. _Note that this is an auto generated message_"
else:
	response_message = args['message']

# Get --browser command line argument value or assign a default
selected_browser = args['browser']

try:
	# Support for Chrome
	if (selected_browser is None) or (selected_browser == 'chrome'):
		browser = webdriver.Chrome(ChromeDriverManager().install())

	# Support for Firefox
	elif selected_browser.lower() == 'firefox':
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

	# Support for Microsoft Edge
	elif selected_browser.lower() == 'edge':
		browser = webdriver.Edge(EdgeDriverManager().install())

	# Support for Microsoft Internet Explorer
	elif selected_browser.lower() == 'ie':
		browser = webdriver.Ie(IEDriverManager().install())

	else:
		exit("Invalid choice. Quitting now...")

except:
	exit('Error! Make sure you\'re selecting the right browser! Quitting now...')

###############################################################################
#                           AUTO RESPONSE LOGIC                               #
###############################################################################

# Create a list that holds the names of people who message
# Names will be duplicated if the person sends multiple messages
# Once the count of duplicates for a name equals to --mbr value,
# all the duplicates will be removed from the list and only one stays
people_list = []

# Try to access Whatsapp on the browser
try:
	browser.get('https://web.whatsapp.com')

	# Run an infinite loop to keep on checking for new messages
	while True:
		# Delay by 1 second
		sleep(1)

		# Get unread messages
		unread_elements = browser.find_elements_by_class_name("CxUIE")

		for message in unread_elements:
			try:
				# Click on the first message
				message.click()

				# Span containing the name of the sender
				name_span = browser.find_element_by_xpath("//div[@class='_2zCDG']/span[@class='_1wjpf']")

				# Get person's name and add it to the list
				name = name_span.text

				# Count of duplicates for a name in the list
				name_count = people_list.count(name)

				# First time the user receives a message from someone
				if name_count == 0:
					# Add the sender to the list and auto respond
					people_list.append(name)

				# Remove name from list if its time to auto respond again
				elif name_count == messages_before_response:
					# Remove all occurrences of the given name but keep 1
					people_list = [word for word in people_list if word != name]

				elif (name_count > 0) and (name_count < messages_before_response):
					# Add the name to the list and skip responding
					people_list.append(name)
					continue


				# Get the text box element
				textbox_element = browser.find_element_by_class_name("_2S1VP")

				# Set response text in the text field
				textbox_element.send_keys(response_message)

				# Get reference to the send button
				send_button = browser.find_element_by_class_name("_35EW6")

				# Click on the send button
				send_button.click()
			except common.exceptions.WebDriverException:
				print("New message received!")
except common.exceptions.WebDriverException:
	exit("Quitting now...")