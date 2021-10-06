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

class CreateOrdersModel(object):
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
        'request_data': 'list[str]'
    }

    attribute_map = {
        'request_data': 'request_data'
    }

    def __init__(self, request_data=None):  # noqa: E501
        """CreateOrdersModel - a model defined in Swagger"""  # noqa: E501
        self._request_data = None
        self.discriminator = None
        if request_data is not None:
            self.request_data = request_data

    @property
    def request_data(self):
        """Gets the request_data of this CreateOrdersModel.  # noqa: E501

        Request data  # noqa: E501

        :return: The request_data of this CreateOrdersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this CreateOrdersModel.

        Request data  # noqa: E501

        :param request_data: The request_data of this CreateOrdersModel.  # noqa: E501
        :type: list[str]
        """

        self._request_data = request_data

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
        if issubclass(CreateOrdersModel, dict):
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
        if not isinstance(other, CreateOrdersModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
