import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
TEST_EMAIL = "youremail@example.com"


def choose_scopes():
    print("\nWhat would you like to do?")
    print("1. Google Drive only")
    print("2. Gmail only")
    print("3. Both Drive and Gmail")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == '1':
        return ['https://www.googleapis.com/auth/drive']
    elif choice == '2':
        return [
            'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/gmail.modify',
        ]
    else:
        return [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/gmail.send',
            'https://www.googleapis.com/auth/gmail.modify',
        ]


def generate_token(scopes):
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("🔄 Token refreshed successfully.")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, scopes)
            creds = flow.run_local_server(port=0)
            print("✅ Logged in successfully.")
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            print(f"💾 Token saved to '{TOKEN_FILE}'.")
    else:
        print("✅ Credentials are already valid.")
    return creds


def send_test_email(creds, recipient):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText('This is a test message sent via the Gmail API.')
        message['to'] = recipient
        message['from'] = 'me'
        message['subject'] = 'Test Email from Gmail API'
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        send_message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f"📧 Email sent to {recipient} with ID: {send_message['id']}")
        return send_message['id']
    except HttpError as error:
        print(f"❌ Error sending email: {error}")
        return None


def upload_test_file(creds):
    try:
        service = build('drive', 'v3', credentials=creds)

        folder_name = "TestFolder"
        response = service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",
            spaces='drive'
        ).execute()
        items = response.get('files', [])

        if items:
            folder_id = items[0]['id']
        else:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = service.files().create(body=file_metadata, fields='id').execute()
            folder_id = folder.get('id')

        file_metadata = {
            'name': 'test_upload.txt',
            'parents': [folder_id]
        }
        from googleapiclient.http import MediaInMemoryUpload
        media_body = MediaInMemoryUpload("This is a test file.".encode("utf-8"), mimetype='text/plain')
        file = service.files().create(body=file_metadata, media_body=media_body, fields='id').execute()
        print(f"📂 File uploaded to Google Drive with ID: {file['id']}")
        return file['id']
    except HttpError as error:
        print(f"❌ Error uploading file to Drive: {error}")
        return None


def delete_drive_file(creds, file_id):
    try:
        service = build('drive', 'v3', credentials=creds)
        service.files().delete(fileId=file_id).execute()
        print(f"🗑️ File with ID {file_id} deleted from Drive.")
    except HttpError as error:
        print(f"❌ Error deleting file: {error}")


if __name__ == '__main__':
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
        print(f"🧹 Token file '{TOKEN_FILE}' removed.")

    scopes = choose_scopes()
    creds = generate_token(scopes)

    if 'drive' in ''.join(scopes):
        file_id = upload_test_file(creds)
        if file_id:
            delete_drive_file(creds, file_id)

    if 'gmail' in ''.join(scopes):
        send_test_email(creds, TEST_EMAIL)
