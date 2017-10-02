# swagger-client
Hotelspro Api Client

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'
swagger_client.configuration.host = '' # test or production host should be set
# create an instance of the API class
api_instance = swagger_client.DefaultApi()
product_code = 'product_code_example' # str | product code that returned in Search(or Hotel Availability) Response

try:
    # Availability with Product Code
    api_response = api_instance.availability_product_code_get(product_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->availability_product_code_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**availability_product_code_get**](docs/DefaultApi.md#availability_product_code_get) | **GET** /availability/{product_code} | Availability with Product Code
*DefaultApi* | [**book_provision_code_post**](docs/DefaultApi.md#book_provision_code_post) | **POST** /book/{provision_code} | Book with Provision Code
*DefaultApi* | [**bookings_booking_code_get**](docs/DefaultApi.md#bookings_booking_code_get) | **GET** /bookings/{booking_code} | Get Booking Detail
*DefaultApi* | [**bookings_get**](docs/DefaultApi.md#bookings_get) | **GET** /bookings/ | Get Booking List
*DefaultApi* | [**cancel_booking_code_post**](docs/DefaultApi.md#cancel_booking_code_post) | **POST** /cancel/{booking_code} | Cancel Booking with Booking Code
*DefaultApi* | [**hotel_availability_get**](docs/DefaultApi.md#hotel_availability_get) | **GET** /hotel-availability/ | Hotel Availability with Hotel Code and Search Code
*DefaultApi* | [**provision_product_code_post**](docs/DefaultApi.md#provision_product_code_post) | **POST** /provision/{product_code} | Provision with Product Code
*DefaultApi* | [**search_post**](docs/DefaultApi.md#search_post) | **POST** /search/ | Search with Hotel Code(Hotel Code List) or Destination Code or Geolocation


## Documentation For Models

 - [AvailabilityResponse](docs/AvailabilityResponse.md)
 - [BookResponse](docs/BookResponse.md)
 - [BookResponseConfirmationNumbers](docs/BookResponseConfirmationNumbers.md)
 - [BookResponseHotelPaymentInfo](docs/BookResponseHotelPaymentInfo.md)
 - [BookResponseRooms](docs/BookResponseRooms.md)
 - [BookingListResponse](docs/BookingListResponse.md)
 - [CancelResponse](docs/CancelResponse.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [HotelAvailabilityResponse](docs/HotelAvailabilityResponse.md)
 - [Pax](docs/Pax.md)
 - [Policy](docs/Policy.md)
 - [Product](docs/Product.md)
 - [ProvisionResponse](docs/ProvisionResponse.md)
 - [Results](docs/Results.md)
 - [Room](docs/Room.md)
 - [SearchResponse](docs/SearchResponse.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

clientintegration@hotelspro.com

