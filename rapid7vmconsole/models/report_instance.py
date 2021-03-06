# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.report_size import ReportSize  # noqa: F401,E501


class ReportInstance(object):
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
        'generated': 'str',
        'id': 'int',
        'links': 'list[Link]',
        'size': 'ReportSize',
        'status': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'generated': 'generated',
        'id': 'id',
        'links': 'links',
        'size': 'size',
        'status': 'status',
        'uri': 'uri'
    }

    def __init__(self, generated=None, id=None, links=None, size=None, status=None, uri=None):  # noqa: E501
        """ReportInstance - a model defined in Swagger"""  # noqa: E501

        self._generated = None
        self._id = None
        self._links = None
        self._size = None
        self._status = None
        self._uri = None
        self.discriminator = None

        if generated is not None:
            self.generated = generated
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if uri is not None:
            self.uri = uri

    @property
    def generated(self):
        """Gets the generated of this ReportInstance.  # noqa: E501

        The date the report finished generation.  # noqa: E501

        :return: The generated of this ReportInstance.  # noqa: E501
        :rtype: str
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this ReportInstance.

        The date the report finished generation.  # noqa: E501

        :param generated: The generated of this ReportInstance.  # noqa: E501
        :type: str
        """

        self._generated = generated

    @property
    def id(self):
        """Gets the id of this ReportInstance.  # noqa: E501

        The identifier of the report instance.  # noqa: E501

        :return: The id of this ReportInstance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportInstance.

        The identifier of the report instance.  # noqa: E501

        :param id: The id of this ReportInstance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this ReportInstance.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this ReportInstance.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ReportInstance.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this ReportInstance.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def size(self):
        """Gets the size of this ReportInstance.  # noqa: E501

        The size of the report, uncompressed.  # noqa: E501

        :return: The size of this ReportInstance.  # noqa: E501
        :rtype: ReportSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ReportInstance.

        The size of the report, uncompressed.  # noqa: E501

        :param size: The size of this ReportInstance.  # noqa: E501
        :type: ReportSize
        """

        self._size = size

    @property
    def status(self):
        """Gets the status of this ReportInstance.  # noqa: E501

        The status of the report generation process.  # noqa: E501

        :return: The status of this ReportInstance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportInstance.

        The status of the report generation process.  # noqa: E501

        :param status: The status of this ReportInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["aborted", "failed", "complete", "running", "unknown"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uri(self):
        """Gets the uri of this ReportInstance.  # noqa: E501

        The URI of the report accessible through the web console. Refer to the `Download` relation hyperlink for a download URI.  # noqa: E501

        :return: The uri of this ReportInstance.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ReportInstance.

        The URI of the report accessible through the web console. Refer to the `Download` relation hyperlink for a download URI.  # noqa: E501

        :param uri: The uri of this ReportInstance.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(ReportInstance, dict):
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
        if not isinstance(other, ReportInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
