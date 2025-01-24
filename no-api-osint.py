import csv
import requests

def parse_emails_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            emails = [row[0] for row in reader if row]  # Extract emails from each row
        return emails
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def process_email(email):
    # Make HTTP request to check email availability
    url = f"https://api.x.com/i/users/email_available.json?email={email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Email: {email}, Response: {response.text}")
        else:
            print(f"Email: {email}, Error: HTTP {response.status_code}")
    except requests.RequestException as e:
        print(f"Email: {email}, Request failed: {e}")

def main():
    choice = input("Would you like to (1) enter an email manually or (2) provide a CSV file? Enter 1 or 2: ")

    if choice == "1":
        email = input("Enter an email address: ")
        process_email(email)
    elif choice == "2":
        csv_file_path = input("Enter the path to your CSV file: ")

        # Parse emails from the provided CSV file
        emails = parse_emails_from_csv(csv_file_path)

        if not emails:
            print("No emails found or file could not be read.")
            return

        print(f"Found {len(emails)} email(s) to process.")

        # Process each email
        for email in emails:
            process_email(email)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
