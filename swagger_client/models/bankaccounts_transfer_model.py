# coding: utf-8

"""
    Restler API Explorer

    Live API Documentation  # noqa: E501

    OpenAPI spec version: 1
    Contact: arul@luracast.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BankaccountsTransferModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'bankaccount_from_id': 'int',
        'bankaccount_to_id': 'int',
        '_date': 'str',
        'description': 'str',
        'amount': 'float',
        'amount_to': 'float'
    }

    attribute_map = {
        'bankaccount_from_id': 'bankaccount_from_id',
        'bankaccount_to_id': 'bankaccount_to_id',
        '_date': 'date',
        'description': 'description',
        'amount': 'amount',
        'amount_to': 'amount_to'
    }

    def __init__(self, bankaccount_from_id=None, bankaccount_to_id=None, _date=None, description=None, amount=None, amount_to=None):  # noqa: E501
        """BankaccountsTransferModel - a model defined in Swagger"""  # noqa: E501
        self._bankaccount_from_id = None
        self._bankaccount_to_id = None
        self.__date = None
        self._description = None
        self._amount = None
        self._amount_to = None
        self.discriminator = None
        self.bankaccount_from_id = bankaccount_from_id
        self.bankaccount_to_id = bankaccount_to_id
        self._date = _date
        self.description = description
        self.amount = amount
        if amount_to is not None:
            self.amount_to = amount_to

    @property
    def bankaccount_from_id(self):
        """Gets the bankaccount_from_id of this BankaccountsTransferModel.  # noqa: E501

        BankAccount ID to use as the source of the internal wire transfer  # noqa: E501

        :return: The bankaccount_from_id of this BankaccountsTransferModel.  # noqa: E501
        :rtype: int
        """
        return self._bankaccount_from_id

    @bankaccount_from_id.setter
    def bankaccount_from_id(self, bankaccount_from_id):
        """Sets the bankaccount_from_id of this BankaccountsTransferModel.

        BankAccount ID to use as the source of the internal wire transfer  # noqa: E501

        :param bankaccount_from_id: The bankaccount_from_id of this BankaccountsTransferModel.  # noqa: E501
        :type: int
        """
        if bankaccount_from_id is None:
            raise ValueError("Invalid value for `bankaccount_from_id`, must not be `None`")  # noqa: E501

        self._bankaccount_from_id = bankaccount_from_id

    @property
    def bankaccount_to_id(self):
        """Gets the bankaccount_to_id of this BankaccountsTransferModel.  # noqa: E501

        BankAccount ID to use as the destination of the internal wire transfer  # noqa: E501

        :return: The bankaccount_to_id of this BankaccountsTransferModel.  # noqa: E501
        :rtype: int
        """
        return self._bankaccount_to_id

    @bankaccount_to_id.setter
    def bankaccount_to_id(self, bankaccount_to_id):
        """Sets the bankaccount_to_id of this BankaccountsTransferModel.

        BankAccount ID to use as the destination of the internal wire transfer  # noqa: E501

        :param bankaccount_to_id: The bankaccount_to_id of this BankaccountsTransferModel.  # noqa: E501
        :type: int
        """
        if bankaccount_to_id is None:
            raise ValueError("Invalid value for `bankaccount_to_id`, must not be `None`")  # noqa: E501

        self._bankaccount_to_id = bankaccount_to_id

    @property
    def _date(self):
        """Gets the _date of this BankaccountsTransferModel.  # noqa: E501

        Date of the internal wire transfer (UNIX timestamp)  # noqa: E501

        :return: The _date of this BankaccountsTransferModel.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BankaccountsTransferModel.

        Date of the internal wire transfer (UNIX timestamp)  # noqa: E501

        :param _date: The _date of this BankaccountsTransferModel.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this BankaccountsTransferModel.  # noqa: E501

        Description of the internal wire transfer  # noqa: E501

        :return: The description of this BankaccountsTransferModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankaccountsTransferModel.

        Description of the internal wire transfer  # noqa: E501

        :param description: The description of this BankaccountsTransferModel.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this BankaccountsTransferModel.  # noqa: E501

        Amount to transfer from the source to the destination BankAccount  # noqa: E501

        :return: The amount of this BankaccountsTransferModel.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BankaccountsTransferModel.

        Amount to transfer from the source to the destination BankAccount  # noqa: E501

        :param amount: The amount of this BankaccountsTransferModel.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def amount_to(self):
        """Gets the amount_to of this BankaccountsTransferModel.  # noqa: E501

        Amount to transfer to the destination BankAccount (only when accounts does not share the same currency)  # noqa: E501

        :return: The amount_to of this BankaccountsTransferModel.  # noqa: E501
        :rtype: float
        """
        return self._amount_to

    @amount_to.setter
    def amount_to(self, amount_to):
        """Sets the amount_to of this BankaccountsTransferModel.

        Amount to transfer to the destination BankAccount (only when accounts does not share the same currency)  # noqa: E501

        :param amount_to: The amount_to of this BankaccountsTransferModel.  # noqa: E501
        :type: float
        """

        self._amount_to = amount_to

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BankaccountsTransferModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BankaccountsTransferModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
