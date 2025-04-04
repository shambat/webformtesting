import requests
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# URL of the Web3Forms API endpoint
url = "https://api.web3forms.com/submit"

# You can change the access_key value here
access_key = ""  # Replace with your chosen access key

# Function to send fake form data
def send_message():
    data = {
        "access_key": access_key,
        "subject": "New Waitlist",  # You can also modify this if necessary
        "email": fake.email(),  # Generate a fake email
        "phone": fake.phone_number(),  # Generate a fake phone number
    }

    # Send POST request to Web3Forms
    response = requests.post(url, data=data)
    
    # Print response status and message
    print(f"[+] Sent to API | Status: {response.status_code} | Response: {response.text}")

# Send 5 fake messages (you can change this number as needed)
for i in range(5):
    print(f"\n[+] Sending fake message #{i + 1}")
    send_message()
