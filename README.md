
## Tasks Background

You are tasked to build a receipt generation API that allows only authenticated and authorized users to generate multiple (at least 10) receipts per request.


## API DOCUMENTATION

# NOTE
1. For the API to work, the user has to be authenticated 
2. The API uses JWT Bearer Token which is passed on the header
3. I have shared a postman collection : RECEIPT APP API.postman_collection.json



* User Registration

- registration url: https://receipts-api-app.herokuapp.com/auth/cashier/
- request type: POST

-  Payload Input:
```

{
    "password": "Password123",
    "username": "cashier",
    "first_name": "User1",
    "last_name": "Test",
    "email": "user@mail.com",
    "sex": "male",
    "date_of_birth": "2021-01-12",
    "phone": "0801111111"
}
```


- Payload Response:

    - status code : 201
    ``` 
    {
        "status": "Successful"
    }
   ```
 



* User Login
- login url: https://receipts-api-app.herokuapp.com/auth/login/
- request type: POST


- Payload Input:

```
{
    "email": "cashier@mail.com",
    "password": "Password123"
}
```


- Payload Response:

     - status code : 200

    ``` 
   
  {
    "email": "cashier@mail.com",
    "username": "cashier01",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2NTEyOTM0LCJqdGkiOiJkMjAwZWViMzhkYjI0NGNhYjQ3YzY1NWI3MjZkYWQ2NyIsInVzZXJfaWQiOjJ9.39NFqfdniNWq0ayKopjsGkfEJV5a5lZ5j2QaUk-juLI" } 
```
```





* API FOR CREATING RECEIPTS

 // To authenticate the API, set the header with the following:
- header 
 'Authorization' :  Bearer <access_token>
 'Content-Type': 'application/json'


-  url: https://receipts-api-app.herokuapp.com/app/create/receipt/
- request type: POST

- Payload Input:

```
[
  
    {
        "customer_name": "Sunday Ajayi",
        "customer_phone": "08067715394",
        "customer_address": "House 51,Road 311,Gowon Estate, Ipaja, Lagos,  Nigeria",
        "item": "Macbook Pro",
        "unit_price": 2900,
        "quantity": 2
    },
    {
        "customer_name": "Sunday Ajayi",
        "customer_phone": "08067715394",
        "customer_address": "House 51,Road 311,Gowon Estate, Ipaja, Lagos,  Nigeria",
        "item": "Macbook Pro",
        "unit_price": 1900,
        "quantity": 2
    },
    
]

```


- Payload Output:

    - 201 status code  ( for receipt data from 10 and above)
      ( returns the body of the created request)
    
    ```
    [
    {
        "customer_name": "Sunday Ajayi",
        "customer_phone": "08067715394",
        "customer_address": "House 51,Road 311,Gowon Estate, Ipaja, Lagos,  Nigeria",
        "item": "Macbook Pro",
        "unit_price": 2900,
        "quantity": 2,
        "description": null,
        "cashier_user": 2,
        "id": 57,
        "total": 5800
    },
        {
        "customer_name": "Sunday Ajayi",
        "customer_phone": "08067715394",
        "customer_address": "House 51,Road 311,Gowon Estate, Ipaja, Lagos,  Nigeria",
        "item": "Macbook Pro",
        "unit_price": 2900,
        "quantity": 2,
        "description": null,
        "cashier_user": 2,
        "id": 57,
        "total": 5800
    },
    ...
    ]
     ```
     


    - 400 status code 

     ```

    {
    "message": [
        "You are about creating less than 10 receipts " ]   
   }
```



     

