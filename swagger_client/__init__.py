# coding: utf-8

"""
    Hotelspro Api Client

    Hotelspro Api Client

    OpenAPI spec version: 2.0.0
    Contact: clientintegration@hotelspro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.availability_response import AvailabilityResponse
from .models.book_response import BookResponse
from .models.book_response_confirmation_numbers import BookResponseConfirmationNumbers
from .models.book_response_hotel_payment_info import BookResponseHotelPaymentInfo
from .models.book_response_rooms import BookResponseRooms
from .models.booking_list_response import BookingListResponse
from .models.cancel_response import CancelResponse
from .models.error import Error
from .models.error_details import ErrorDetails
from .models.hotel_availability_response import HotelAvailabilityResponse
from .models.pax import Pax
from .models.policy import Policy
from .models.product import Product
from .models.provision_response import ProvisionResponse
from .models.results import Results
from .models.room import Room
from .models.search_response import SearchResponse

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()