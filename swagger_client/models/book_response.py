# coding: utf-8

"""
    Hotelspro Api Client

    Hotelspro Api Client

    OpenAPI spec version: 2.0.0
    Contact: clientintegration@hotelspro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BookResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'created_at': 'str',
        'checkin': 'str',
        'checkout': 'str',
        'hotel_code': 'str',
        'destination_code': 'str',
        'client_nationality': 'str',
        'pay_at_hotel': 'bool',
        'currency': 'str',
        'mealtype_code': 'str',
        'nonrefundable': 'str',
        'view': 'str',
        'price': 'str',
        'policies': 'list[Policy]',
        'rooms': 'list[Room]',
        'status': 'str',
        'confirmation_numbers': 'list[BookResponseConfirmationNumbers]',
        'hotel_payment_info': 'list[BookResponseHotelPaymentInfo]',
        'minimum_selling_price': 'str',
        'special_request': 'str'
    }

    attribute_map = {
        'code': 'code',
        'created_at': 'created_at',
        'checkin': 'checkin',
        'checkout': 'checkout',
        'hotel_code': 'hotel_code',
        'destination_code': 'destination_code',
        'client_nationality': 'client_nationality',
        'pay_at_hotel': 'pay_at_hotel',
        'currency': 'currency',
        'mealtype_code': 'mealtype_code',
        'nonrefundable': 'nonrefundable',
        'view': 'view',
        'price': 'price',
        'policies': 'policies',
        'rooms': 'rooms',
        'status': 'status',
        'confirmation_numbers': 'confirmation_numbers',
        'hotel_payment_info': 'hotel_payment_info',
        'minimum_selling_price': 'minimum_selling_price',
        'special_request': 'special_request'
    }

    def __init__(self, code=None, created_at=None, checkin=None, checkout=None, hotel_code=None, destination_code=None, client_nationality=None, pay_at_hotel=None, currency=None, mealtype_code=None, nonrefundable=None, view=None, price=None, policies=None, rooms=None, status=None, confirmation_numbers=None, hotel_payment_info=None, minimum_selling_price=None, special_request=None):
        """
        BookResponse - a model defined in Swagger
        """

        self._code = None
        self._created_at = None
        self._checkin = None
        self._checkout = None
        self._hotel_code = None
        self._destination_code = None
        self._client_nationality = None
        self._pay_at_hotel = None
        self._currency = None
        self._mealtype_code = None
        self._nonrefundable = None
        self._view = None
        self._price = None
        self._policies = None
        self._rooms = None
        self._status = None
        self._confirmation_numbers = None
        self._hotel_payment_info = None
        self._minimum_selling_price = None
        self._special_request = None

        self.code = code
        self.created_at = created_at
        self.checkin = checkin
        self.checkout = checkout
        self.hotel_code = hotel_code
        self.destination_code = destination_code
        self.client_nationality = client_nationality
        self.pay_at_hotel = pay_at_hotel
        self.currency = currency
        self.mealtype_code = mealtype_code
        self.nonrefundable = nonrefundable
        if view is not None:
          self.view = view
        self.price = price
        self.policies = policies
        self.rooms = rooms
        self.status = status
        self.confirmation_numbers = confirmation_numbers
        self.hotel_payment_info = hotel_payment_info
        if minimum_selling_price is not None:
          self.minimum_selling_price = minimum_selling_price
        if special_request is not None:
          self.special_request = special_request

    @property
    def code(self):
        """
        Gets the code of this BookResponse.

        :return: The code of this BookResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this BookResponse.

        :param code: The code of this BookResponse.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def created_at(self):
        """
        Gets the created_at of this BookResponse.

        :return: The created_at of this BookResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this BookResponse.

        :param created_at: The created_at of this BookResponse.
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def checkin(self):
        """
        Gets the checkin of this BookResponse.

        :return: The checkin of this BookResponse.
        :rtype: str
        """
        return self._checkin

    @checkin.setter
    def checkin(self, checkin):
        """
        Sets the checkin of this BookResponse.

        :param checkin: The checkin of this BookResponse.
        :type: str
        """
        if checkin is None:
            raise ValueError("Invalid value for `checkin`, must not be `None`")

        self._checkin = checkin

    @property
    def checkout(self):
        """
        Gets the checkout of this BookResponse.

        :return: The checkout of this BookResponse.
        :rtype: str
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """
        Sets the checkout of this BookResponse.

        :param checkout: The checkout of this BookResponse.
        :type: str
        """
        if checkout is None:
            raise ValueError("Invalid value for `checkout`, must not be `None`")

        self._checkout = checkout

    @property
    def hotel_code(self):
        """
        Gets the hotel_code of this BookResponse.

        :return: The hotel_code of this BookResponse.
        :rtype: str
        """
        return self._hotel_code

    @hotel_code.setter
    def hotel_code(self, hotel_code):
        """
        Sets the hotel_code of this BookResponse.

        :param hotel_code: The hotel_code of this BookResponse.
        :type: str
        """
        if hotel_code is None:
            raise ValueError("Invalid value for `hotel_code`, must not be `None`")

        self._hotel_code = hotel_code

    @property
    def destination_code(self):
        """
        Gets the destination_code of this BookResponse.

        :return: The destination_code of this BookResponse.
        :rtype: str
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """
        Sets the destination_code of this BookResponse.

        :param destination_code: The destination_code of this BookResponse.
        :type: str
        """
        if destination_code is None:
            raise ValueError("Invalid value for `destination_code`, must not be `None`")

        self._destination_code = destination_code

    @property
    def client_nationality(self):
        """
        Gets the client_nationality of this BookResponse.

        :return: The client_nationality of this BookResponse.
        :rtype: str
        """
        return self._client_nationality

    @client_nationality.setter
    def client_nationality(self, client_nationality):
        """
        Sets the client_nationality of this BookResponse.

        :param client_nationality: The client_nationality of this BookResponse.
        :type: str
        """
        if client_nationality is None:
            raise ValueError("Invalid value for `client_nationality`, must not be `None`")

        self._client_nationality = client_nationality

    @property
    def pay_at_hotel(self):
        """
        Gets the pay_at_hotel of this BookResponse.

        :return: The pay_at_hotel of this BookResponse.
        :rtype: bool
        """
        return self._pay_at_hotel

    @pay_at_hotel.setter
    def pay_at_hotel(self, pay_at_hotel):
        """
        Sets the pay_at_hotel of this BookResponse.

        :param pay_at_hotel: The pay_at_hotel of this BookResponse.
        :type: bool
        """
        if pay_at_hotel is None:
            raise ValueError("Invalid value for `pay_at_hotel`, must not be `None`")

        self._pay_at_hotel = pay_at_hotel

    @property
    def currency(self):
        """
        Gets the currency of this BookResponse.

        :return: The currency of this BookResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this BookResponse.

        :param currency: The currency of this BookResponse.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")
        allowed_values = ["USD", "EUR", "GBP", "TRY", "AED"]
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def mealtype_code(self):
        """
        Gets the mealtype_code of this BookResponse.

        :return: The mealtype_code of this BookResponse.
        :rtype: str
        """
        return self._mealtype_code

    @mealtype_code.setter
    def mealtype_code(self, mealtype_code):
        """
        Sets the mealtype_code of this BookResponse.

        :param mealtype_code: The mealtype_code of this BookResponse.
        :type: str
        """
        if mealtype_code is None:
            raise ValueError("Invalid value for `mealtype_code`, must not be `None`")

        self._mealtype_code = mealtype_code

    @property
    def nonrefundable(self):
        """
        Gets the nonrefundable of this BookResponse.

        :return: The nonrefundable of this BookResponse.
        :rtype: str
        """
        return self._nonrefundable

    @nonrefundable.setter
    def nonrefundable(self, nonrefundable):
        """
        Sets the nonrefundable of this BookResponse.

        :param nonrefundable: The nonrefundable of this BookResponse.
        :type: str
        """
        if nonrefundable is None:
            raise ValueError("Invalid value for `nonrefundable`, must not be `None`")

        self._nonrefundable = nonrefundable

    @property
    def view(self):
        """
        Gets the view of this BookResponse.

        :return: The view of this BookResponse.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this BookResponse.

        :param view: The view of this BookResponse.
        :type: str
        """

        self._view = view

    @property
    def price(self):
        """
        Gets the price of this BookResponse.

        :return: The price of this BookResponse.
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this BookResponse.

        :param price: The price of this BookResponse.
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def policies(self):
        """
        Gets the policies of this BookResponse.

        :return: The policies of this BookResponse.
        :rtype: list[Policy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this BookResponse.

        :param policies: The policies of this BookResponse.
        :type: list[Policy]
        """
        if policies is None:
            raise ValueError("Invalid value for `policies`, must not be `None`")

        self._policies = policies

    @property
    def rooms(self):
        """
        Gets the rooms of this BookResponse.

        :return: The rooms of this BookResponse.
        :rtype: list[Room]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """
        Sets the rooms of this BookResponse.

        :param rooms: The rooms of this BookResponse.
        :type: list[Room]
        """
        if rooms is None:
            raise ValueError("Invalid value for `rooms`, must not be `None`")

        self._rooms = rooms

    @property
    def status(self):
        """
        Gets the status of this BookResponse.

        :return: The status of this BookResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BookResponse.

        :param status: The status of this BookResponse.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def confirmation_numbers(self):
        """
        Gets the confirmation_numbers of this BookResponse.

        :return: The confirmation_numbers of this BookResponse.
        :rtype: list[BookResponseConfirmationNumbers]
        """
        return self._confirmation_numbers

    @confirmation_numbers.setter
    def confirmation_numbers(self, confirmation_numbers):
        """
        Sets the confirmation_numbers of this BookResponse.

        :param confirmation_numbers: The confirmation_numbers of this BookResponse.
        :type: list[BookResponseConfirmationNumbers]
        """
        if confirmation_numbers is None:
            raise ValueError("Invalid value for `confirmation_numbers`, must not be `None`")

        self._confirmation_numbers = confirmation_numbers

    @property
    def hotel_payment_info(self):
        """
        Gets the hotel_payment_info of this BookResponse.

        :return: The hotel_payment_info of this BookResponse.
        :rtype: list[BookResponseHotelPaymentInfo]
        """
        return self._hotel_payment_info

    @hotel_payment_info.setter
    def hotel_payment_info(self, hotel_payment_info):
        """
        Sets the hotel_payment_info of this BookResponse.

        :param hotel_payment_info: The hotel_payment_info of this BookResponse.
        :type: list[BookResponseHotelPaymentInfo]
        """
        if hotel_payment_info is None:
            raise ValueError("Invalid value for `hotel_payment_info`, must not be `None`")

        self._hotel_payment_info = hotel_payment_info

    @property
    def minimum_selling_price(self):
        """
        Gets the minimum_selling_price of this BookResponse.

        :return: The minimum_selling_price of this BookResponse.
        :rtype: str
        """
        return self._minimum_selling_price

    @minimum_selling_price.setter
    def minimum_selling_price(self, minimum_selling_price):
        """
        Sets the minimum_selling_price of this BookResponse.

        :param minimum_selling_price: The minimum_selling_price of this BookResponse.
        :type: str
        """

        self._minimum_selling_price = minimum_selling_price

    @property
    def special_request(self):
        """
        Gets the special_request of this BookResponse.

        :return: The special_request of this BookResponse.
        :rtype: str
        """
        return self._special_request

    @special_request.setter
    def special_request(self, special_request):
        """
        Sets the special_request of this BookResponse.

        :param special_request: The special_request of this BookResponse.
        :type: str
        """

        self._special_request = special_request

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other