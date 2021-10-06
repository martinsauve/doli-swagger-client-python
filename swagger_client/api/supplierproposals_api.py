# coding: utf-8

"""
    Restler API Explorer

    Live API Documentation  # noqa: E501

    OpenAPI spec version: 1
    Contact: arul@luracast.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SupplierproposalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_supplierproposals(self, **kwargs):  # noqa: E501
        """List supplier proposals 🔐  # noqa: E501

        Get a list of supplier proposals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_supplierproposals(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sortfield: Sort field
        :param str sortorder: Sort order
        :param int limit: Limit for list
        :param int page: Page number
        :param str thirdparty_ids: Thirdparty ids to filter supplier proposals (example '1' or '1,2,3')
        :param str sqlfilters: Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\"
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_supplierproposals_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_supplierproposals_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_supplierproposals_with_http_info(self, **kwargs):  # noqa: E501
        """List supplier proposals 🔐  # noqa: E501

        Get a list of supplier proposals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_supplierproposals_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sortfield: Sort field
        :param str sortorder: Sort order
        :param int limit: Limit for list
        :param int page: Page number
        :param str thirdparty_ids: Thirdparty ids to filter supplier proposals (example '1' or '1,2,3')
        :param str sqlfilters: Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.datec:<:'20160101')\"
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sortfield', 'sortorder', 'limit', 'page', 'thirdparty_ids', 'sqlfilters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_supplierproposals" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sortfield' in params:
            query_params.append(('sortfield', params['sortfield']))  # noqa: E501
        if 'sortorder' in params:
            query_params.append(('sortorder', params['sortorder']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'thirdparty_ids' in params:
            query_params.append(('thirdparty_ids', params['thirdparty_ids']))  # noqa: E501
        if 'sqlfilters' in params:
            query_params.append(('sqlfilters', params['sqlfilters']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/supplierproposals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_supplierproposals(self, id, **kwargs):  # noqa: E501
        """Get properties of a supplier proposal (price request) object 🔐  # noqa: E501

        Return an array with supplier proposal informations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_supplierproposals(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of supplier proposal (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_supplierproposals_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_supplierproposals_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def retrieve_supplierproposals_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get properties of a supplier proposal (price request) object 🔐  # noqa: E501

        Return an array with supplier proposal informations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_supplierproposals_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of supplier proposal (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_supplierproposals" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve_supplierproposals`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/supplierproposals/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
