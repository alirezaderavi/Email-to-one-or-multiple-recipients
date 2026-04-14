# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(sender_email, password, recipients, subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject

        # Email body
        msg.attach(MIMEText(body, "plain"))

        # Attachment (if provided)
        if attachment_path:
            if not os.path.exists(attachment_path):
                print("Attachment file not found!")
                return

            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            filename = os.path.basename(attachment_path)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            msg.attach(part)

        # Connect to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipients, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)


def main():
    print("Email Sender Program")
    print("1. Single Recipient")
    print("2. Multiple Recipients")
    print("3. Email with Attachment")

    choice = input("Choose an option (1/2/3): ")

    sender_email = input("Enter your email: ")
    password = input("Enter your app password: ")
    subject = input("Enter subject: ")
    body = input("Enter email body: ")

    if choice == "1":
        recipient = input("Enter recipient email: ")
        send_email(sender_email, password, [recipient], subject, body)

    elif choice == "2":
        recipients_input = input("Enter multiple emails (comma-separated): ")
        recipients = [email.strip() for email in recipients_input.split(",")]
        send_email(sender_email, password, recipients, subject, body)

    elif choice == "3":
        recipients_input = input("Enter recipient(s) (comma-separated): ")
        recipients = [email.strip() for email in recipients_input.split(",")]
        attachment_path = input("Enter file path for attachment: ")
        send_email(sender_email, password, recipients, subject, body, attachment_path)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()