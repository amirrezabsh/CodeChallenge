# Aban Tether Code Challenge
In order to run the code you just need to build a docker image using the Dockerfile and then just run it. You can follow the steps below to run it.
1. **Building the Docker Image**:  Open a terminal and navigate to your project's root directory. Run the following command to build the Docker image:
```
docker build -t my-django-app .
```
Replace `my-django-app` with a suitable name for your image.

2. **Running the Docker Container**: After the image is built, you can run a Docker container from it:
```
docker run -p 8000:8000 my-django-app
```
This maps port 8000 from the container to port 8000 on your local machine. Adjust the port as needed based on your needs.

# Notes:
1. The default value of the user's balance is 0.0 so in order to test the POST request you should change the value in the admin panel.
2. The route for the POST request is /api/orders/place_order.
3. The tests are written in the orders app. Because the users app didn't have any methods in its views. In order to run the tests just run this command in the terminal:
```
python manage.py test orders
``` 



