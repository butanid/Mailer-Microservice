# README - Mailer-Microservice
Mailer Microservice for my partners weather app

This README provides clear instructions on how to programmatically request and receive data from the mailer microservice designed for my partner, which sends emails using the Gmail SMTP server.

## Prerequisites

Requirements for the software and other tools to build, test and push 
- Python 'mailer', 'Flask', and 'requests' libraries
- Configure Python app password on Google account

## Installation

### Download the Python library modules by running:

    pip install mailer
    pip install Flask
    pip install requests

### Setting up a Python app password

First, log into your Google account and go into your account settings

From there modify your current web URL to look something like this:

    https://myaccount.google.com/u/3/apppasswords

The 'apppasswords' at the end of the URL is important here!

Type in 'Python' in the App Name input prompt

This will then generate a randomized app password, which is what you will use in your program to allow it access to send an email from the Gmail account specified.

You may need to enable 2-factor authentication on your Google account prior to being allowed to set an app password

## Requesting Data (Sending an Email)

Below are the steps required to setting up the mailer service with example inputs provided

### Initilize 'EmailSender'

First, you need to initialize your Gmail credentials within the mailer service file

    mailer = Mailer(
        host="smtp.gmail.com",
        port=587,
        use_tls=True,
        usr="your-email",
        pwd="your-password"
    )
    
Remember the password input is the app password you configuered earlier!

### Sending an Email

This method requires the sender's email, recipient's email, subject, plain text content, or HTML content within the test program file

    email_sender.send_email(
        from_email="your-email@gmail.com",
        to_email="recipient-email@email-provider.com",
        subject="Test Email",
        plain_text="This is the plain text content of the email.",
        html_text="<h1>This is the HTML content of the email.</h1>")

## Receiving Data

The mailer microservice primarily focuses on reqesting and packaging the data, which is handled internally through try-except blocks and print statements

     try:
          data = request.json
          message = Message(From=data['from_email'], To=data['to_email'], Subject=data['subject'])
          message.Body = data['plain_text']
          if 'html_text' in data:
            message.Html = data['html_text']
          mailer.send(message)
          return jsonify({"status": "Success"}), 200
      except Exception as e:
          return jsonify({"status": "Error", "message": str(e)}), 500

The reception of data pertains to handling the success or failure feedback of the email-sending process, which is managed internally through try-except blocks and print statements

     try:
          response = requests.post(f"{self.service_url}/send_email", json=email_inputs)
          response.raise_for_status()
          print(f"Email sent to {to_email}")
      except requests.exceptions.RequestException as e:
          print(f"Failed to send email to {to_email}: {e}")

Upon calling the send_email method, the microservice will print a success message if the email is sent otherwise, it will print a failure message along with the exception details

## UML Sequence Diagram

The UML below illustrates the process of sending an email using the mailer microservice:

![UML Diagram](https://github.com/butanid/Mailer-Microservice/assets/129903890/c057cf89-63a7-4d25-a9a5-ab15b3160fef)
