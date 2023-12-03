from django.core.mail import send_mail

def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Hello, activate your account!',
        f'You need to follow the link for activation: {full_link}',
        'kutmanvip01@gmail.com',    #TODO: use a configurable sender address,
        [user],
        fail_silently=False,
    )
