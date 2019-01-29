# Whatsapp Web Autoresponder
Whatsapp Web Autoresponder is a small program that allows you to send automatic replies to your whatsapp messages. You might be busy or away for a while and instead of letting your friends or family wait on you for a long time without any reply, you could let the program take care of that while you're away! You can specify a message to send when you receive new messages and the program will take care of sending it.

The program uses [Selenium](https://www.seleniumhq.org) to perform the automation. It constantly checks if there is a new message and for every new message, it opens the chat and sends the automated reply.


**Note**: This is only for **Whatsapp Web** and not the mobile application.

## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- A web browser, preferably [Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/en-US/firefox/new/)

## Running the program
- Step 0, download the repository and open a console inside the folder.
- First step is to download the required dependencies. To do that, run the following command on your console:
    ```
    pip install -r requirements.txt
    ```
- After that, you're ready to run the program! Enter the following command:
    ```
    python app.py
    ```
    Running this command will use the default settings. To modify them, move to the next section.
    
## Options
The following options can be added to the `python app.py` command to change default behaviour. Multiple options can be used at once. Here is the list of options:
- **-b, --browser**

    **Type**: String
    
    This option allows you to specify a web browser that you would like to run Whatsapp Web on. Currently, only 4 browsers are supported. They are:
    - Chrome
        ```
        python app.py -b chrome
        ```
    - Firefox
        ```
        python app.py -b firefox
        ```
    - Microsoft Edge
        ```
        python app.py -b edge
        ```
    - Internet Explorer
        ```
        python app.py -b ie
        ```
- **-m, --message**

    **Type**: String
    
    This option specifies the message that should sent by the program when a new message is received. The default message is: "Sorry, I'm busy at the moment, will reply in a while. _Note that this is an auto generated message_".
    ```
    python app.py -m "Hey, I'll get back to you soon"
    ```
- **-n, --mbr**
    
    **Type**: Integer

    This option allows you to tell the program, how many messages should it wait before autoresponding again. For example, the first time you receive a message, the program sends an automated reply. If the sender repeatedly sends messages, it will wait until **n** messages are received before autoresponding again. Default number of messages before autoresponding is 5.
    ```
    python app.py -n 10
    ```
- **-h, --help**
This option just displays the list of optional arguments and their descriptions. It does not take any value.
    ```
    python app.py --help
    ```
## Example Usage
```
python app.py
```
```
python app.py -m "Hey, I'll get back to you soon" -n 3 -b chrome
```
```
pyhon app.py -mbr 3 -browser chrome
```
