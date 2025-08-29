from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Bill
from .serializers import BillSerializer
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

class BillUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'no image file provided'}, status=status.HTTP_400_BAD_REQUEST)

        bill = Bill.objects.create(image=image_file)

        # On Windows, you may need to set:
        pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

        try:
            img_path = bill.image.path
            img = Image.open(img_path)
            raw_text = pytesseract.image_to_string(img)
            bill.raw_text = raw_text
            bill.save()            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


