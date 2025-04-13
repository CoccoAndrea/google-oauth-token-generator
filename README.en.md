# 🔐 Google Oauth Token Generator

This Python project generates an **OAuth 2.0 access token** to be used in other scripts that interact with **Google APIs**, such as Gmail and Google Drive.

---

## ✅ Features

- Performs OAuth 2.0 authentication via browser
- Saves the token to a `token.json` file
- Sends a test email using the Gmail API
- Uploads a text file to Google Drive (inside the "TestFolder")
- Deletes the test file from Google Drive

---

## 📦 Requirements

- Python 3.7 or higher
- A Google Cloud project with Gmail API and Drive API enabled
- A `credentials.json` file obtained from the Google Cloud Console

---

## ☁️ How to create a Google Cloud project with Gmail and Drive API enabled

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Click on **Select project** > **New project**.
3. Name your project and create it.
4. In the left menu, go to **APIs & Services** > **Library**.
5. Search and enable the following APIs:
   - **Gmail API**
   - **Google Drive API**
6. Go to **Credentials** > **Create credentials** > **OAuth client ID**.
7. If prompted, configure the consent screen (app name, email, etc.).
8. Choose **Desktop application** as the application type.
9. Download the `credentials.json` file and place it in the project root.

---

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your credentials:**

Make sure the `credentials.json` file (from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)) is located in the project root.

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

The program will:

1. Guide you through Google login (first time only).
2. Generate and save the token in `token.json`, ready for use in other scripts.
3. (Optional) Perform test operations: send email, upload file, and delete file.

---

## 🔐 Authentication

The first run will open a browser window to authorize access to your Google account. The token will be saved in `token.json`.

---

## 📬 Change the test email address

In the `main.py` file, edit the `TEST_EMAIL` variable:

```python
TEST_EMAIL = "youremail@example.com"
```

---

## 📄 License

This project is licensed under the **MIT** License.
