# 📧 Python Email Sender

A simple Python program to send emails using SMTP.
Supports:

* Single recipient
* Multiple recipients
* Email with attachment

---

## 🚀 Features

* Send emails via Gmail SMTP
* Multiple recipients support
* File attachments
* Simple CLI interface

---

## 🛠️ Requirements

* Python 3.x
* Gmail account

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Email-to-one-or-multiple-recipients.git
cd Email-to-one-or-multiple-recipients
```

---

### 2. Enable 2-Step Verification

Before using this program, you must enable **2-Step Verification** on your Google account.

Go to:
https://myaccount.google.com/security

---

### 3. Generate an App Password

This project uses an **App Password** instead of your real Gmail password for security.

Steps:

1. Go to: https://myaccount.google.com/apppasswords
2. Select:

   * App → Mail
   * Device → Other → type "Python Script"
3. Click **Generate**
4. Copy the generated password

⚠️ Important:

* Remove spaces before using it
* Example:

  ```
  abcd efgh ijkl mnop
  ```

  becomes:

  ```
  abcdefghijklmnop
  ```

---

### 4. Run the Program

```bash
python Email_to_one_or_multiple_recipients.py
```

---

## 📌 Usage

You will be prompted to choose:

1. Single Recipient
2. Multiple Recipients
3. Email with Attachment

Follow the CLI instructions.

---

## 🔐 Security Notes

* Never share your App Password
* Do NOT upload credentials to GitHub
* Consider using environment variables for production use

---

## 💡 Future Improvements

* GUI (Tkinter)
* Bulk email from CSV
* HTML email support
* Logging system

---

## 📄 License

MIT License
