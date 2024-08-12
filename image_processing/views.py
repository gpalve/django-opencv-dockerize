# Create your views here.
from django.shortcuts import render
import cv2
from django.http import HttpResponse
import numpy as np

def index(request):
    # Create a simple black image
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.putText(img, 'OpenCV with Django', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Convert the image to JPEG format
    ret, jpeg = cv2.imencode('.jpg', img)
    return HttpResponse(jpeg.tobytes(), content_type='image/jpeg')
