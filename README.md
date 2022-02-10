# CLI-Email-Sender
Command line program to send simple text emails as well as emails with multiple attachments in Python

A script in Python to
+ Send text emails.
+ Send multiple attachments (including images, videos, audios and compressed files).

To send email from the gmail server you need to allow access for less secure apps. Go to https://myaccount.google.com/lesssecureapps in your Google account that will generate
a password for apps other than google. Or you can disable 2 step verification on your account to send email through third party apps (less secure).

In text_email_sender, for sending an email with default email address, you have to provide your default email address and less secure apps password in environments variables.
(always provide your credentials as environment variables for safety).
