from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings


class SendMailView(APIView):

    def get(self, request):

        send_mail(
            subject="Auto Mail",
            message="Hi Hello How are you",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["receiver@gmail.com"],
        )

        return Response({
            "status": "success",
            "message": "Mail sent successfully"
        })