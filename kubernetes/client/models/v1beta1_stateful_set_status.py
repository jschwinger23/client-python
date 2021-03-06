# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1StatefulSetStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, observed_generation=None, replicas=None):
        """
        V1beta1StatefulSetStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_generation': 'int',
            'replicas': 'int'
        }

        self.attribute_map = {
            'observed_generation': 'observedGeneration',
            'replicas': 'replicas'
        }

        self._observed_generation = observed_generation
        self._replicas = replicas

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1beta1StatefulSetStatus.
        most recent generation observed by this StatefulSet.

        :return: The observed_generation of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1beta1StatefulSetStatus.
        most recent generation observed by this StatefulSet.

        :param observed_generation: The observed_generation of this V1beta1StatefulSetStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def replicas(self):
        """
        Gets the replicas of this V1beta1StatefulSetStatus.
        Replicas is the number of actual replicas.

        :return: The replicas of this V1beta1StatefulSetStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1beta1StatefulSetStatus.
        Replicas is the number of actual replicas.

        :param replicas: The replicas of this V1beta1StatefulSetStatus.
        :type: int
        """
        if replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")

        self._replicas = replicas

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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1StatefulSetStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
