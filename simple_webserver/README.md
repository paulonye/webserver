# Simple Webserver

## STEPS

### Define the App

To get started with your web app, you can get started using a web framework, we will be using fastapi.

fastapi is a modern web framework for building web applications

- Install necessary libraries - fastapi and uvicorn (for running the web application)
- Import the fastpi module
- Instantiate your fastapi instance
- Define your method, and resource name
- Define your function
- Your function might need to take in Query Parameters; in this case you would need to specify the type of input as a function argument


### Building the API
You would need to instantiate a fastapi instance, after which you then specify a method, a resource name, along with a function.

When defining responses, by default fast api handles serialization such that if your function is supposed to end up getting a list/array, you don't need to serialize your data before sending across the internet, fastapi handles that for you.

When wrirting (post); you need to model how that the data will look

### Start the Webserver
To start the webserver, you need to start the use uvicorn

`uvicorn main:app --port 8080 --reload`

`main`: This is the name of the script, and `app` is the name of the fastapi instance defined.

You can also define the app with an host, this is important if you want to expose the application to external users.

`uvicorn main:app --host 0.0.0.0 --port 8080`

### Testing the API with curl
For testing the download API
`curl -X POST -F "file=@random.png" http://localhost:8080/upload`

For testing the Get transactions API
`curl -X GET http://localhost:8080/transactions?rows=3`

