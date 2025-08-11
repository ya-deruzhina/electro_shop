from shop_api.tasks import send_message_task
from apps.shop.models import ShopsModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import qrcode, io, base64

class QRcodeSendView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):        
        try:
            user = request.user
            email = request.user.email            
            
            if user.is_superuser:
                contacts = ShopsModel.objects.all()
            else:
                shop_id = user.shop_employee
                if not shop_id:
                    return Response ({"Status": "User Has not Shops"})
                else:
                    shop_id = shop_id.id
                    contacts = ShopsModel.objects.filter(pk=shop_id)
                

        except:
            return Response ({"Status": "Error In Getting Data"}, status=status.HTTP_404_NOT_FOUND)

        else:                
            for contact in contacts:
                qr_text = (f'{contact.country}, {contact.city}, {contact.street}, {contact.house_number}')

                try:
                    qr = qrcode.make(qr_text)
                    buffer = io.BytesIO()
                    qr.save(buffer, format='PNG')
                    buffer.seek(0)

                    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                    
                except:
                    return Response ({"Status": "QR-Code generation error"})

                send_message_task.delay(user.username, email, qr_base64)
            return Response ({'Status':'Successful - Message Sent'})                    

        # else:
        #     qr_text = (f'{contact.country}, {contact.city}, {contact.street}, {contact.house_number}')

        #     try:
        #         qr = qrcode.make(qr_text)
        #         buffer = io.BytesIO()
        #         qr.save(buffer, format='PNG')
        #         buffer.seek(0)

        #         qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
        #     except:
        #         return Response ({"Status": "QR-Code generation error"})

        #     send_message_task.delay(user, email, qr_base64)
        #     return Response ({'Status':'Successful - Message Sent'})