from .models import User
from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def send_email(username):
    context = {'username':username}
    template = get_template('registro/cumple.html')
    content = template.render(context)

    email = EmailMultiAlternatives (
        'Registro de Membresia',
        'Socio MEDIRED',
        settings.EMAIL_HOST_USER,
        [username],
    )
    email.attach_alternative(content,'text/html')
    email.send()
def Felicitaciones(request):
    queryset = User.objects.filter(fecha_nacimiento =  timezone.now()).only('username')
    for i  in queryset:
        send_email(queryset)