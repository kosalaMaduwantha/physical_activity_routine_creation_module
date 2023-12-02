# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PhysicalActResponseBody400(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, title: str=None, status: int=None, detail: str=None):  # noqa: E501
        """PhysicalActResponseBody400 - a model defined in Swagger

        :param type: The type of this PhysicalActResponseBody400.  # noqa: E501
        :type type: str
        :param title: The title of this PhysicalActResponseBody400.  # noqa: E501
        :type title: str
        :param status: The status of this PhysicalActResponseBody400.  # noqa: E501
        :type status: int
        :param detail: The detail of this PhysicalActResponseBody400.  # noqa: E501
        :type detail: str
        """
        self.swagger_types = {
            'type': str,
            'title': str,
            'status': int,
            'detail': str
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'status': 'status',
            'detail': 'detail'
        }
        self._type = type
        self._title = title
        self._status = status
        self._detail = detail

    @classmethod
    def from_dict(cls, dikt) -> 'PhysicalActResponseBody400':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The physical_act_response_body_400 of this PhysicalActResponseBody400.  # noqa: E501
        :rtype: PhysicalActResponseBody400
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this PhysicalActResponseBody400.

        type of the error  # noqa: E501

        :return: The type of this PhysicalActResponseBody400.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this PhysicalActResponseBody400.

        type of the error  # noqa: E501

        :param type: The type of this PhysicalActResponseBody400.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self) -> str:
        """Gets the title of this PhysicalActResponseBody400.

        title of the error  # noqa: E501

        :return: The title of this PhysicalActResponseBody400.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this PhysicalActResponseBody400.

        title of the error  # noqa: E501

        :param title: The title of this PhysicalActResponseBody400.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def status(self) -> int:
        """Gets the status of this PhysicalActResponseBody400.

        status of the error  # noqa: E501

        :return: The status of this PhysicalActResponseBody400.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this PhysicalActResponseBody400.

        status of the error  # noqa: E501

        :param status: The status of this PhysicalActResponseBody400.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def detail(self) -> str:
        """Gets the detail of this PhysicalActResponseBody400.

        detail of the error  # noqa: E501

        :return: The detail of this PhysicalActResponseBody400.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this PhysicalActResponseBody400.

        detail of the error  # noqa: E501

        :param detail: The detail of this PhysicalActResponseBody400.
        :type detail: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail