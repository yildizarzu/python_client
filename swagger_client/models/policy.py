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


class Policy(object):
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
        'ratio': 'str',
        'days_remaining': 'int'
    }

    attribute_map = {
        'ratio': 'ratio',
        'days_remaining': 'days_remaining'
    }

    def __init__(self, ratio=None, days_remaining=None):
        """
        Policy - a model defined in Swagger
        """

        self._ratio = None
        self._days_remaining = None

        if ratio is not None:
          self.ratio = ratio
        if days_remaining is not None:
          self.days_remaining = days_remaining

    @property
    def ratio(self):
        """
        Gets the ratio of this Policy.

        :return: The ratio of this Policy.
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """
        Sets the ratio of this Policy.

        :param ratio: The ratio of this Policy.
        :type: str
        """

        self._ratio = ratio

    @property
    def days_remaining(self):
        """
        Gets the days_remaining of this Policy.

        :return: The days_remaining of this Policy.
        :rtype: int
        """
        return self._days_remaining

    @days_remaining.setter
    def days_remaining(self, days_remaining):
        """
        Sets the days_remaining of this Policy.

        :param days_remaining: The days_remaining of this Policy.
        :type: int
        """

        self._days_remaining = days_remaining

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
