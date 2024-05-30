# Importing requests module to handle HTTP requests
import requests

class EmailSender:
    # Initializing Gmail SMTP server
    def __init__(self, service_url):
        self.service_url = service_url

    # Function to send email
    def send_email(self, from_email, to_email, subject, plain_text, html_text=None):
        email_inputs = {
            "from_email": from_email,
            "to_email": to_email,
            "subject": subject,
            "plain_text": plain_text,
            "html_text": html_text
        }
        # Sending the email
        try:
            # Sending post request to mailer service
            response = requests.post(f"{self.service_url}/send_email", json=email_inputs)
            response.raise_for_status()
            print(f"Email sent to {to_email}")
        # Exception to handle errors 
        except requests.exceptions.RequestException as e:
            print(f"Failed to send email to {to_email}: {e}")

# Usage example:
if __name__ == "__main__":
    # Set up the email sender with the service URL
    email_sender = EmailSender(service_url="http://localhost:5000")
    
    # Send an email
    email_sender.send_email(
        from_email="your-email",
        to_email="recepient-email",
        subject="Test Email",
        plain_text="This is the plain text content of the email.",
        html_text="<h1>This is the HTML content of the email.</h1>"
    )