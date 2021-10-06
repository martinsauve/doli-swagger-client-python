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


class ExpensereportsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_expensereports(self, **kwargs):  # noqa: E501
        """Create Expense Report object 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expensereports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateExpensereportsModel body: request_data  

        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_expensereports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_expensereports_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_expensereports_with_http_info(self, **kwargs):  # noqa: E501
        """Create Expense Report object 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expensereports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateExpensereportsModel body: request_data  

        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_expensereports" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'request_data' in params:
            form_params.append(('request_data', params['request_data']))  # noqa: E501
            collection_formats['request_data'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/expensereports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_expensereports(self, **kwargs):  # noqa: E501
        """Create Expense Report object 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expensereports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] request_data:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_expensereports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_expensereports_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_expensereports_with_http_info(self, **kwargs):  # noqa: E501
        """Create Expense Report object 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_expensereports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] request_data:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_expensereports" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'request_data' in params:
            form_params.append(('request_data', params['request_data']))  # noqa: E501
            collection_formats['request_data'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/expensereports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_expensereports(self, **kwargs):  # noqa: E501
        """List Expense Reports 🔐  # noqa: E501

        Get a list of Expense Reports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_expensereports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sortfield: Sort field
        :param str sortorder: Sort order
        :param int limit: Limit for list
        :param int page: Page number
        :param str user_ids: User ids filter field. Example: '1' or '1,2,3'
        :param str sqlfilters: Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\"
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_expensereports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_expensereports_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_expensereports_with_http_info(self, **kwargs):  # noqa: E501
        """List Expense Reports 🔐  # noqa: E501

        Get a list of Expense Reports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_expensereports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sortfield: Sort field
        :param str sortorder: Sort order
        :param int limit: Limit for list
        :param int page: Page number
        :param str user_ids: User ids filter field. Example: '1' or '1,2,3'
        :param str sqlfilters: Other criteria to filter answers separated by a comma. Syntax example \"(t.ref:like:'SO-%') and (t.date_creation:<:'20160101')\"
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sortfield', 'sortorder', 'limit', 'page', 'user_ids', 'sqlfilters']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_expensereports" % key
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
        if 'user_ids' in params:
            query_params.append(('user_ids', params['user_ids']))  # noqa: E501
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
            '/expensereports', 'GET',
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

    def remove_expensereports(self, id, **kwargs):  # noqa: E501
        """Delete Expense Report 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_expensereports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense Report ID (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_expensereports_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_expensereports_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_expensereports_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Expense Report 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_expensereports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Expense Report ID (required)
        :return: list[str]
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
                    " to method remove_expensereports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_expensereports`")  # noqa: E501

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
            '/expensereports/{id}', 'DELETE',
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

    def retrieve_expensereports(self, id, **kwargs):  # noqa: E501
        """Get properties of a Expense Report object 🔐  # noqa: E501

        Return an array with Expense Report informations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_expensereports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of Expense Report (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_expensereports_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_expensereports_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def retrieve_expensereports_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get properties of a Expense Report object 🔐  # noqa: E501

        Return an array with Expense Report informations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_expensereports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of Expense Report (required)
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
                    " to method retrieve_expensereports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve_expensereports`")  # noqa: E501

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
            '/expensereports/{id}', 'GET',
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

    def update_expensereports(self, id, **kwargs):  # noqa: E501
        """Update Expense Report general fields (won't touch lines of expensereport) 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_expensereports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of Expense Report to update (required)
        :param UpdateExpensereportsModel body: request_data  

        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_expensereports_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_expensereports_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_expensereports_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Expense Report general fields (won't touch lines of expensereport) 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_expensereports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of Expense Report to update (required)
        :param UpdateExpensereportsModel body: request_data  

        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_expensereports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_expensereports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'request_data' in params:
            form_params.append(('request_data', params['request_data']))  # noqa: E501
            collection_formats['request_data'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/expensereports/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_expensereports(self, id, **kwargs):  # noqa: E501
        """Update Expense Report general fields (won't touch lines of expensereport) 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_expensereports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of Expense Report to update (required)
        :param list[str] request_data:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_expensereports_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_expensereports_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_expensereports_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Expense Report general fields (won't touch lines of expensereport) 🔐  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_expensereports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of Expense Report to update (required)
        :param list[str] request_data:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_expensereports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_expensereports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'request_data' in params:
            form_params.append(('request_data', params['request_data']))  # noqa: E501
            collection_formats['request_data'] = 'multi'  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/expensereports/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
