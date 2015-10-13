# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_line1': 'str',
            'address_line2': 'str',
            'postal_code': 'str',
            'city': 'City'
        }

        self.attribute_map = {
            'address_line1': 'addressLine1',
            'address_line2': 'addressLine2',
            'postal_code': 'postalCode',
            'city': 'city'
        }

        self._address_line1 = None
        self._address_line2 = None
        self._postal_code = None
        self._city = None

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this Address.


        :return: The address_line1 of this Address.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this Address.


        :param address_line1: The address_line1 of this Address.
        :type: str
        """
        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this Address.


        :return: The address_line2 of this Address.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this Address.


        :param address_line2: The address_line2 of this Address.
        :type: str
        """
        self._address_line2 = address_line2

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Address.


        :return: The postal_code of this Address.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Address.


        :param postal_code: The postal_code of this Address.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def city(self):
        """
        Gets the city of this Address.


        :return: The city of this Address.
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Address.


        :param city: The city of this Address.
        :type: City
        """
        self._city = city

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
