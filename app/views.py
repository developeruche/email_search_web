from django.shortcuts import render, redirect
import re
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'

# Create your views here.
""" 
This is where all the fucntinality would be done.
one of the veiws would recive image from the fortend and another view would
recive just a string of words.
"""
# Util functions


def genereateEmalList(x):
    email_list = []
    for word in x:
        if len(word) > 50:
            print(word, 'greater')
        else:
            print(word)
            if re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', word):
                email_list.append(word)
            else:
                pass

    print(email_list)
    return email_list


# Defining the function that would render the home page


def index(request):
    return render(request, 'app.html', {

    })
# Alogirthm of the fucntional view that would receive a string from the frontend


def ReceiveString(request):
    context = {}
    # Retriving string from the request.data
    if request.method == 'POST':
        try:
            input_string = request.POST['data']
        except:
            context['error'] = 'Could not location the form data.'

        if input_string:
            # Now if the file exist i would be converting all the worlds to a array
            input_string_list = input_string.replace(
                "'", "").replace(",", "").split()

            # This function would with the power of regexp locate all the array list item with that is an email and return a list of them
            list_of_found_email = genereateEmalList(input_string_list)
            context['data'] = list_of_found_email
        return render(request, 'result.html', {
            'data': context['data'],
            'count': len(list_of_found_email),
        })

# Defining the Alogirthm that would recieve image data then convert it to string and work on the convert string and get all the email therein


def ReceiveImage(request):
    context = {}
    # Extracting image data
    if request.method == 'POST':
        try:
            input_image = request.FILES['data']
        except:
            context['error'] = 'Image not founded'

        if input_image:
            # A functionanlity to extract text from the image
            input_image_string = tess.image_to_string(input_image)
            # Then the string retrived from the image if now formated to a list dataset
            input_image_string_list = input_image_string.replace(
                "'", "").replace(",", "").split()
            # The fuction which was defined above would be called to get all the email availble in the input_image_string_list
            list_of_found_email = genereateEmalList(input_image_string_list)
            context['data'] = list_of_found_email

        return render(request, 'result.html', {
            'data': context['data']
        })
