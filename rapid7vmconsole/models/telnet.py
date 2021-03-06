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


class Telnet(object):
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
        'character_set': 'str',
        'failed_login_regex': 'str',
        'links': 'list[Link]',
        'login_regex': 'str',
        'password_prompt_regex': 'str',
        'questionable_login_regex': 'str'
    }

    attribute_map = {
        'character_set': 'characterSet',
        'failed_login_regex': 'failedLoginRegex',
        'links': 'links',
        'login_regex': 'loginRegex',
        'password_prompt_regex': 'passwordPromptRegex',
        'questionable_login_regex': 'questionableLoginRegex'
    }

    def __init__(self, character_set=None, failed_login_regex=None, links=None, login_regex=None, password_prompt_regex=None, questionable_login_regex=None):  # noqa: E501
        """Telnet - a model defined in Swagger"""  # noqa: E501

        self._character_set = None
        self._failed_login_regex = None
        self._links = None
        self._login_regex = None
        self._password_prompt_regex = None
        self._questionable_login_regex = None
        self.discriminator = None

        if character_set is not None:
            self.character_set = character_set
        if failed_login_regex is not None:
            self.failed_login_regex = failed_login_regex
        if links is not None:
            self.links = links
        if login_regex is not None:
            self.login_regex = login_regex
        if password_prompt_regex is not None:
            self.password_prompt_regex = password_prompt_regex
        if questionable_login_regex is not None:
            self.questionable_login_regex = questionable_login_regex

    @property
    def character_set(self):
        """Gets the character_set of this Telnet.  # noqa: E501

        The character set to use.  # noqa: E501

        :return: The character_set of this Telnet.  # noqa: E501
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this Telnet.

        The character set to use.  # noqa: E501

        :param character_set: The character_set of this Telnet.  # noqa: E501
        :type: str
        """

        self._character_set = character_set

    @property
    def failed_login_regex(self):
        """Gets the failed_login_regex of this Telnet.  # noqa: E501

        Regular expression to match a failed login response.  # noqa: E501

        :return: The failed_login_regex of this Telnet.  # noqa: E501
        :rtype: str
        """
        return self._failed_login_regex

    @failed_login_regex.setter
    def failed_login_regex(self, failed_login_regex):
        """Sets the failed_login_regex of this Telnet.

        Regular expression to match a failed login response.  # noqa: E501

        :param failed_login_regex: The failed_login_regex of this Telnet.  # noqa: E501
        :type: str
        """

        self._failed_login_regex = failed_login_regex

    @property
    def links(self):
        """Gets the links of this Telnet.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Telnet.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Telnet.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Telnet.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def login_regex(self):
        """Gets the login_regex of this Telnet.  # noqa: E501

        Regular expression to match a login response.  # noqa: E501

        :return: The login_regex of this Telnet.  # noqa: E501
        :rtype: str
        """
        return self._login_regex

    @login_regex.setter
    def login_regex(self, login_regex):
        """Sets the login_regex of this Telnet.

        Regular expression to match a login response.  # noqa: E501

        :param login_regex: The login_regex of this Telnet.  # noqa: E501
        :type: str
        """

        self._login_regex = login_regex

    @property
    def password_prompt_regex(self):
        """Gets the password_prompt_regex of this Telnet.  # noqa: E501

        Regular expression to match a password prompt.  # noqa: E501

        :return: The password_prompt_regex of this Telnet.  # noqa: E501
        :rtype: str
        """
        return self._password_prompt_regex

    @password_prompt_regex.setter
    def password_prompt_regex(self, password_prompt_regex):
        """Sets the password_prompt_regex of this Telnet.

        Regular expression to match a password prompt.  # noqa: E501

        :param password_prompt_regex: The password_prompt_regex of this Telnet.  # noqa: E501
        :type: str
        """

        self._password_prompt_regex = password_prompt_regex

    @property
    def questionable_login_regex(self):
        """Gets the questionable_login_regex of this Telnet.  # noqa: E501

        Regular expression to match a potential false negative login response.  # noqa: E501

        :return: The questionable_login_regex of this Telnet.  # noqa: E501
        :rtype: str
        """
        return self._questionable_login_regex

    @questionable_login_regex.setter
    def questionable_login_regex(self, questionable_login_regex):
        """Sets the questionable_login_regex of this Telnet.

        Regular expression to match a potential false negative login response.  # noqa: E501

        :param questionable_login_regex: The questionable_login_regex of this Telnet.  # noqa: E501
        :type: str
        """

        self._questionable_login_regex = questionable_login_regex

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
        if issubclass(Telnet, dict):
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
        if not isinstance(other, Telnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
