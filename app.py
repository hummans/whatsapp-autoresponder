from time import sleep
from selenium import webdriver, common

try:
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com')

    MESSAGES_BEFORE_RESPONSE = 5
    people_list = []

    # Run an infinite loop to keep checking for new messages
    while True:
        # Delay by 1 second
        sleep(1)

        # Get unread messages
        unread_elements = browser.find_elements_by_class_name("CxUIE")

        # Print number of unread messages
        # print("Unread messages : " + str(len(unread_elements)))

        for message in unread_elements:
            try:
                # Click on the first message
                message.click()

                # Span containing the name of the user
                name_span = browser.find_element_by_xpath("//div[@class='_2zCDG']/span[@class='_1wjpf']")

                # Get person's name and add it to the list
                name = name_span.text

                # Remove name from list if its time to auto respond again
                if people_list.count(name) == MESSAGES_BEFORE_RESPONSE:
                    # Remove all occurrence of the given name
                    # people_list = list(filter((name).__ne__, people_list))

                    # Remove all occurrences of the given name but keep 1
                    people_list = [word for word in people_list if word != name]
                elif (people_list.count(name) < MESSAGES_BEFORE_RESPONSE) and (people_list.count(name) > 0):
                    # Add the name to the list and skip responding
                    people_list.append(name)
                    continue
                elif people_list.count(name) == 0:
                    # Add the user to the list and auto respond
                    people_list.append(name)


                # Get the text box element
                textbox_element = browser.find_element_by_class_name("_2S1VP")

                # Set some text in the text field
                response_message = "Sorry, I'm busy at the moment, will reply in a while. _Note that this is an auto generated message_"
                textbox_element.send_keys(response_message)

                # Get reference to the send button
                send_button = browser.find_element_by_class_name("_35EW6")

                # Click on the send button
                send_button.click()
            except common.exceptions.WebDriverException:
                print("New message received!")

except common.exceptions.WebDriverException:
    print("Browser closed. Quitting program...")
