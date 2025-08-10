from shop_api.celery import app
from django.core.mail import EmailMessage
import base64


@app.task
def send_message_task(username, email, qr_base64):
    qr_bytes = base64.b64decode(qr_base64)

    email_message = EmailMessage(
        subject=f'QR Code for {username}',
        body='Attached QR code',
        to=[email],
    )
    email_message.attach(f"{username}_qrcode.png", qr_bytes, 'image/png')
    email_message.send()

    print('Message Sent')