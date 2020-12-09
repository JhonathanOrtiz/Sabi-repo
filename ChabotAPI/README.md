# Chatbot API with Dialogflow and FastAPI


# Prerequesites

* Python >= 3.6

* virtualenv <= 16.7.10


# Overview

The following API was built with Python as programming language "Dialogflow" as chatbot interface and FastAPI as server builder. 

**IMPORTANT**

* Dialogflow webhook API works only with HTTPS protocol.
* For request to API use a POST to server URL


  ``` request POST (url, query) ```

* Your request body must be a json object with a unique attribute "text" (e.g {text: "your query"})
  
  ``` user_input = {"text": "user query"} ```

* Response is a json object with the following attributes:



  ``` 
  {
        "text": string,
        "intent": string,
        "all_parameters": bool,
        "search": bool,
        "query": dict 
    }
    
  ```

*WHERE*...

**text**: Chatbot response.

**intent**: Intent detected 

**search**: if conditions for searching are complete is true, otherwise false

**all_parameters**: If user input has all parameters required for detected intent is True otherwise False

**query**: Is a dict with two parameters product which is a list if products required, and cants which is the cants for each product. the n-th is for n-product

# API ARCHITECTURE

[main.py](https://github.com/AllAmigo/chatbot_api/blob/master/chatbot_api/main.py) File recives a post request with a text input from user, and then call "get_response" method.

[models.py](https://github.com/AllAmigo/chatbot_api/blob/master/chatbot_api/app/models.py) file create the object for query user format.

[send_message.py](https://github.com/AllAmigo/chatbot_api/blob/master/chatbot_api/app/send_message.py) file, contains "get_response methods" and several methods for normalize input from user before call Dialogflow API and return a QueryResult Object. 

[parsing_response](https://github.com/AllAmigo/chatbot_api/blob/master/chatbot_api/app/parsing_response.py) file, cotains "parse response" method and since we can't return a QueryResult object here we parse the QueryResult Object and return a json object with important information from Dialogflow API response.


# Start using API


``` $ cd chatbot_api ```

``` $ pip3 install -r requirements.txt ```

For use just FastAPI run the following command

``` $ uvicorn main:app --host 0.0.0.0 --port 80 ```

NOTE: you should before install requirements.txt

Uvicorn packege should be installed by running requirements.txt, otherwise you can install it via pip

``` $ pip install uvicorn ```


This API was created for ALL Enterprise SABI app 

Backend team - Machine Learning

by Jhonathan Ortiz