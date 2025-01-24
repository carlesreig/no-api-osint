import requests

# Get user input for email
email = input("Enter an email address: ")

# Make HTTP request
url = f"https://api.x.com/i/users/email_available.json?email={email}"
response = requests.get(url)

# Show the result from the response
print(response.text)