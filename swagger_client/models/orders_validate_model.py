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

class OrdersValidateModel(object):
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
        'idwarehouse': 'int',
        'notrigger': 'int'
    }

    attribute_map = {
        'idwarehouse': 'idwarehouse',
        'notrigger': 'notrigger'
    }

    def __init__(self, idwarehouse=None, notrigger=None):  # noqa: E501
        """OrdersValidateModel - a model defined in Swagger"""  # noqa: E501
        self._idwarehouse = None
        self._notrigger = None
        self.discriminator = None
        if idwarehouse is not None:
            self.idwarehouse = idwarehouse
        if notrigger is not None:
            self.notrigger = notrigger

    @property
    def idwarehouse(self):
        """Gets the idwarehouse of this OrdersValidateModel.  # noqa: E501

        Warehouse ID  # noqa: E501

        :return: The idwarehouse of this OrdersValidateModel.  # noqa: E501
        :rtype: int
        """
        return self._idwarehouse

    @idwarehouse.setter
    def idwarehouse(self, idwarehouse):
        """Sets the idwarehouse of this OrdersValidateModel.

        Warehouse ID  # noqa: E501

        :param idwarehouse: The idwarehouse of this OrdersValidateModel.  # noqa: E501
        :type: int
        """

        self._idwarehouse = idwarehouse

    @property
    def notrigger(self):
        """Gets the notrigger of this OrdersValidateModel.  # noqa: E501

        1=Does not execute triggers, 0= execute triggers  # noqa: E501

        :return: The notrigger of this OrdersValidateModel.  # noqa: E501
        :rtype: int
        """
        return self._notrigger

    @notrigger.setter
    def notrigger(self, notrigger):
        """Sets the notrigger of this OrdersValidateModel.

        1=Does not execute triggers, 0= execute triggers  # noqa: E501

        :param notrigger: The notrigger of this OrdersValidateModel.  # noqa: E501
        :type: int
        """

        self._notrigger = notrigger

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
        if issubclass(OrdersValidateModel, dict):
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
        if not isinstance(other, OrdersValidateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
