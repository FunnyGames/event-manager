from django.core.mail import send_mail


def sendResetPasswordEmail(email):
    key = '123'
    link = f'http://localhost:8000/reset/password?email={email}&key={key}'
    send_mail(
        subject='Reset Password',
        message=f'You received this email because you clicked reset password.\n' +
        'Copy the following link to address in browser:\n{link}\nIf you did not request a reset password, please ignore this email',
        recipient_list=[email],
        html_message='You received this email because you clicked reset password.<br/>' +
        'Please click the following link to reset the password:<br/>' +
        f'<a href={link}>Click here</a><br/>' +
        f'If you don\'t see the link, copy it to address:<br/>{link}<br/>'
        'If you did not request a reset password, please ignore this email',
        fail_silently=False,
        from_email=''
    )
