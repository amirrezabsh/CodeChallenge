# Aban Tether Code Challenge
To run the code, you simply need to build a Docker image using the provided Dockerfile and then execute the image. You can follow the steps below to accomplish this.
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
1. The default value of the user's balance is 0.0 in the users model. To properly test the POST request that involves deducting the balance, you need to ensure that the user's balance is updated accordingly, either by modifying it in the admin panel or by creating users with different balances programmatically.

2. The route for the POST request to place an order is  `/api/orders/place_order`.

3. The tests for the code are written in the orders app, not the users app. You can run these tests by using the following command:terminal:
```
python manage.py test orders
``` 
This command will run the tests located within the `tests.py` file of the `orders` app and provide you with feedback on whether the code is functioning correctly.


