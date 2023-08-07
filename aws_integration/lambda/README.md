# CREATE A RESTFUL API GATEWAY ENDPINT THAT INVOKES A LAMBDA FUNCTION

## There is a default event input you get when you set up a rest endpoint and invoke a lambda function through an api gateway. This event is then passed as an imput into the lambda function and you can use it as args in your function body.

## STEPS
1. Create a lambda function; code up the function to take in event input (Varies for different inputs)
2. Set up a transanctions resource and set up a get method api -> it forwards requests to the lambda function. 
3. The lamda function returns a hardcoded response; you can do something else like call a database
4. Invoke the endpoint from the browser or using curl

## CREATING A LAMBDA FUNCTION
creating a function requires you to understand the trigger; trigger could be:
- API Gateway
- Http 
- Cloud Storage

Once you understand the trigger, you can then go ahead to define the event type, in some cases, functions can be triggered without requirung any form of event input. In some other cases, you need to be able to pass in event inputs: IN AWS, FOR API Gateway triggered events; the inputs can be passed in using event['queryStringParameters']

## DEPLOYING A LAMBDA FUNCTION

Your function might need additional dependencies to run; in this case you must add the modules/libraries to the same path as your function which is the root directory. You can pip install these libraries using `pip install pandas -t .` . This command will not add the module to your path nor virtual environment, but rather download them to the current path. Once they have been downloaded, you can then zip all required files and your main function file.

You must also change the Handler namwe to: name_of_python_file:function_name. The Handler info can be found under Runtime Settings.