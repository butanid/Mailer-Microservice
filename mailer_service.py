# Importing modules and specific classes from Flask and Mailer
from flask import Flask, request, jsonify
from mailer import Message, Mailer

app = Flask(__name__)

# Setting up gmail SMTP Server details
mailer = Mailer(
    host="smtp.gmail.com",
    port=587,
    use_tls=True,
    usr="your-email",
    pwd="your-password"
)

# Defining route to send email via POST request
@app.route('/send_email', methods=['POST'])
# Function to handle email sending process
def send_email():
    try:
        # Requesting JSON data
        data = request.json
        # Create email message with provided data
        message = Message(From=data['from_email'], To=data['to_email'], Subject=data['subject'])
        message.Body = data['plain_text']

        # Checks if HTML content provided
        if 'html_text' in data:
            message.Html = data['html_text']
        # Sending the email message
        mailer.send(message)
        return jsonify({"status": "Success"}), 200
    # Exception to handle errors
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
