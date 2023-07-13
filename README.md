# E-commerce Image Search App

📸🔍🛍️

An E-commerce Image Search app built with Flutter and Django. The app allows users to choose an image from the gallery or take a photo using the camera. The selected image is then sent to the backend server for image recognition using the ResNet50 model. The app receives a JSON response with recommended images based on the analyzed image and displays them in a grid view.
## Installation

1. Clone the repository:
   run : git clone https://github.com/your-username/django-project.git
2. Create a virtual environment (optional but recommended)
3. Install the project dependencies using `pip` and the `requirements.txt` file:
    run the command:pip install -r requirements.txt
4. Apply migrations to set up the database:
    run the command: python manage.py migrate
5.To start the development server, run the following command:
    run the command:python manage.py runserver
   youll get a localhost url with port number navigate to the api end point and send a post request with an image for examplelocalhost:8000/api/similar-images/

## Hosted api link

Check out the Hosted api: [API Link](http://110.227.255.212:6021/api/similar-images/)
## Demo

Check out the demo of the app: [Demo Link](https://drive.google.com/file/d/18QHjAHwCdP2N7N076v8aYIM5907EIC6M/view?usp=drivesdk)

## APK

Check out the demo of the app: [Demo Link](https://drive.google.com/file/d/1F5IyMUECJ7UFZ6Z0Hzxtz2lpvK5hiFZc/view?usp=drivesdk)

## Dataset

check out the dataset used : [Dataset link](https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images)


## Features

**Frontend (Flutter):**

- 🖼️ Choose an image from the gallery or take a photo using the camera.
- 🖌️ Crop the selected image to focus on the desired area.
- 🚀 Send the cropped image to the backend server for image recognition.
- 📥 Receive a JSON response with recommended images.
- 📷 Display the recommended images in a grid view.

**Backend (Django):**

- 🌐 Implement an API endpoint using Django's REST Framework.
- 📸 Receive the cropped image from the frontend as a multipart/form-data request.
- 🧠 Perform image recognition using the ResNet50 model.
- 📋 Generate a JSON response with recommended images.
- 💾 Integrate with Django's database for data storage and retrieval (if required).



