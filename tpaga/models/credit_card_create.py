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


class CreditCardCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreditCardCreate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'primary_account_number': 'str',
            'expiration_month': 'str',
            'expiration_year': 'str',
            'card_verification_code': 'str',
            'card_holder_name': 'str',
            'billing_address': 'BillingAddress'
        }

        self.attribute_map = {
            'primary_account_number': 'primaryAccountNumber',
            'expiration_month': 'expirationMonth',
            'expiration_year': 'expirationYear',
            'card_verification_code': 'cardVerificationCode',
            'card_holder_name': 'cardHolderName',
            'billing_address': 'billingAddress'
        }

        self._primary_account_number = None
        self._expiration_month = None
        self._expiration_year = None
        self._card_verification_code = None
        self._card_holder_name = None
        self._billing_address = None

    @property
    def primary_account_number(self):
        """
        Gets the primary_account_number of this CreditCardCreate.


        :return: The primary_account_number of this CreditCardCreate.
        :rtype: str
        """
        return self._primary_account_number

    @primary_account_number.setter
    def primary_account_number(self, primary_account_number):
        """
        Sets the primary_account_number of this CreditCardCreate.


        :param primary_account_number: The primary_account_number of this CreditCardCreate.
        :type: str
        """
        self._primary_account_number = primary_account_number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this CreditCardCreate.


        :return: The expiration_month of this CreditCardCreate.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this CreditCardCreate.


        :param expiration_month: The expiration_month of this CreditCardCreate.
        :type: str
        """
        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this CreditCardCreate.


        :return: The expiration_year of this CreditCardCreate.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this CreditCardCreate.


        :param expiration_year: The expiration_year of this CreditCardCreate.
        :type: str
        """
        self._expiration_year = expiration_year

    @property
    def card_verification_code(self):
        """
        Gets the card_verification_code of this CreditCardCreate.


        :return: The card_verification_code of this CreditCardCreate.
        :rtype: str
        """
        return self._card_verification_code

    @card_verification_code.setter
    def card_verification_code(self, card_verification_code):
        """
        Sets the card_verification_code of this CreditCardCreate.


        :param card_verification_code: The card_verification_code of this CreditCardCreate.
        :type: str
        """
        self._card_verification_code = card_verification_code

    @property
    def card_holder_name(self):
        """
        Gets the card_holder_name of this CreditCardCreate.


        :return: The card_holder_name of this CreditCardCreate.
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """
        Sets the card_holder_name of this CreditCardCreate.


        :param card_holder_name: The card_holder_name of this CreditCardCreate.
        :type: str
        """
        self._card_holder_name = card_holder_name

    @property
    def billing_address(self):
        """
        Gets the billing_address of this CreditCardCreate.


        :return: The billing_address of this CreditCardCreate.
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this CreditCardCreate.


        :param billing_address: The billing_address of this CreditCardCreate.
        :type: BillingAddress
        """
        self._billing_address = billing_address

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
