# store-manager-api-v2
#### Continous Integration badges
[![Build Status](https://travis-ci.com/calebrotich10/store-manager-api-v2.svg?branch=develop)](https://travis-ci.com/calebrotich10/store-manager-api-v2)  [![Coverage Status](https://coveralls.io/repos/github/calebrotich10/store-manager-api-v2/badge.svg?branch=develop)](https://coveralls.io/github/calebrotich10/store-manager-api-v2?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/94613d7438838aeb23d5/maintainability)](https://codeclimate.com/github/calebrotich10/store-manager-api-v2/maintainability)

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. This repository contains the API endpoints for the application and has data persisted using Postgres database

#### Functionality
1. The application allows the admin to register a new store attendant
2. The application enables the store attendant to create sales
3. The admin can add products and categories

#### Endpoints
<table>
  <tr>
    <th>Http Method</th>
    <th>Endpoint</th>
    <th>Functionality</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v2/auth/signup</td>
    <td>Creates a new user account</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v2/products</td>
    <td>Used by the admin to add a new product</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v2/saleorder</td>
    <td>Used by the sale attendant to add a new sale order</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/auth/signin</td>
    <td>Authenticates and creates a token for the users</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/products/&ltproduct_id&gt</td>
    <td>Enables a user to fetch a specific product</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/saleorder/&ltsale_order_id&gt</td>
    <td>Enables a user to fetch a specific sale order</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/products</td>
    <td>Enables a user to fetch all products</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/saleorder</td>
    <td>Enables a user to fetch all sale orders</td>
  </tr>
   <tr>
    <td>POST</td>
    <td>api/v2/category</td>
    <td>Enables a user to create a category</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v2/category</td>
    <td>Enables a user to fetch all categories</td>
  </tr>
   <tr>
    <td>PUT</td>
    <td>api/v2/category/<id:category_id></td>
    <td>Enables a user to update a category</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>api/v2/category<int:category_id></td>
    <td>Enables a user to delete a category</td>
  </tr>
   <tr>
    <td>POST</td>
    <td>api/v2/auth/logout</td>
    <td>Logs out a user and blacklists the token</td>
  </tr>
</table>

#### Installing the application
1. Open a command terminal in your preferred folder
2. Run command `git clone https://github.com/calebrotich10/store-manager-api-v2.git` to have a copy locally
3. `cd store-manager-api-v2`
4. Create a virtual environment for the application `virtualenv venv`
5. Install dependencies from the `requirements.txt` file `pip3 install -r requirements.txt`
6. Export environment variables to your environment ```export JWT_SECRET_KEY=your-secret-key```, ```export FLASK_APP="run.py"```,```export FLASK_ENV="development"```
6. Run the application using flask command `flask run` or using python3 `python3 run.py`

#### Running tests
Inside the virtual environment created above, run command:
`export FLASK_ENV='testing'`
`coverage run --source=app.api.v1 -m pytest app/tests/v1 -v -W error::UserWarning && coverage report`

#### Technologies used
1. `JWT` for authentication
2. `pytest` for running tests
3. Python based framework `flask`
4. Flask packages

#### Deployment
[Heroku](https://store-manager-api-v2.herokuapp.com/)

#### Author
[Caleb Rotich](https://github.com/calebrotich10)

#### Credits
This application was build as part of the [Andela](https://andela.com/) NBO 33 challenge. #TIA
