E-commerce Image Search app
demo link-https://drive.google.com/file/d/14NEXouCcqeNHqASsVvN0iv2XHEGzvi6o/view?usp=drivesdk
Frontend (Flutter)
Choose an image from the gallery or take a photo using the camera.
Crop the selected image.
Send the cropped image to the backend server for image recognition.
Receive a JSON response with recommended images.
Display the recommended images in a grid view.
Backend (Django)
Implement an API endpoint using Django's REST Framework.
Receive the cropped image from the frontend as a multipart/form-data request.
Perform image recognition using the ResNet50 model.
Generate a JSON response with recommended images.
Integrate with Django's database (if required) for data storage and retrieval.
