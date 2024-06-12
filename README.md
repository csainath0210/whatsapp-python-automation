#WhatsApp Automation Script
  This Python script automates WhatsApp messaging using Selenium WebDriver and Pandas. The script can be used to send personalized messages to multiple contacts by reading contact information and message content from an Excel file.

#Features
  Automated WhatsApp Web Login: Uses Selenium to open WhatsApp Web and wait for the user to scan the QR code.
  Message Sending: Reads contacts and messages from an Excel file and sends them via WhatsApp.
  Error Handling: Includes basic error handling to manage situations where contacts are not found or messages fail to send.

#Prerequisites
  Python 3.x
  Google Chrome
  ChromeDriver (compatible with your Chrome version)
  Required Python packages: selenium, pandas

#Installation
  Clone the repository:
  ```
  git clone https://github.com/csainath0210/whatsapp-python-automation.git
  cd whatsapp-python-automation
  cd src
  ```


#Download and install ChromeDriver:

  Download from ChromeDriver official site.
  Ensure ChromeDriver is in your system's PATH or place it in the same directory as your script.

#Setup
Prepare your Excel file:

Create an Excel file (contactsAndMessages.xlsx) with at least two columns: Contact Number (phone number) and Message (message to send).
Example:
Contact Number	Message
91345678901	Hello, how are you?
91987654321	Good morning!

#Configure the script:
  Update the path to your Excel file in the script if necessary.

#Usage

Run the script:

```
python wa_script.py
```

Login to WhatsApp Web:
  The script will open a Chrome window with WhatsApp Web.
  Scan the QR code with your phone to log in.

#Automated Messaging:

  The script will read the contacts and messages from the Excel file and send the messages automatically.

#Notes
  Make sure your phone stays connected to the internet during the automation process.
  This script is intended for educational purposes. Use it responsibly and ensure you comply with WhatsApp's terms of service.
