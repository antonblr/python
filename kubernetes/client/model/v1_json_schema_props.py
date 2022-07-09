"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kubernetes.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from kubernetes.client.exceptions import ApiAttributeError


def lazy_import():
    from kubernetes.client.model.v1_external_documentation import V1ExternalDocumentation
    from kubernetes.client.model.v1_validation_rule import V1ValidationRule
    globals()['V1ExternalDocumentation'] = V1ExternalDocumentation
    globals()['V1ValidationRule'] = V1ValidationRule


class V1JSONSchemaProps(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'ref': (str,),  # noqa: E501
            'schema': (str,),  # noqa: E501
            'additional_items': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'additional_properties': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'all_of': ([V1JSONSchemaProps],),  # noqa: E501
            'any_of': ([V1JSONSchemaProps],),  # noqa: E501
            'default': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'definitions': ({str: (V1JSONSchemaProps,)},),  # noqa: E501
            'dependencies': ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)},),  # noqa: E501
            'description': (str,),  # noqa: E501
            'enum': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'example': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'exclusive_maximum': (bool,),  # noqa: E501
            'exclusive_minimum': (bool,),  # noqa: E501
            'external_docs': (V1ExternalDocumentation,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'items': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'max_items': (int,),  # noqa: E501
            'max_length': (int,),  # noqa: E501
            'max_properties': (int,),  # noqa: E501
            'maximum': (float,),  # noqa: E501
            'min_items': (int,),  # noqa: E501
            'min_length': (int,),  # noqa: E501
            'min_properties': (int,),  # noqa: E501
            'minimum': (float,),  # noqa: E501
            'multiple_of': (float,),  # noqa: E501
            '_not': (V1JSONSchemaProps,),  # noqa: E501
            'nullable': (bool,),  # noqa: E501
            'one_of': ([V1JSONSchemaProps],),  # noqa: E501
            'pattern': (str,),  # noqa: E501
            'pattern_properties': ({str: (V1JSONSchemaProps,)},),  # noqa: E501
            'properties': ({str: (V1JSONSchemaProps,)},),  # noqa: E501
            'required': ([str],),  # noqa: E501
            'title': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'unique_items': (bool,),  # noqa: E501
            'x_kubernetes_embedded_resource': (bool,),  # noqa: E501
            'x_kubernetes_int_or_string': (bool,),  # noqa: E501
            'x_kubernetes_list_map_keys': ([str],),  # noqa: E501
            'x_kubernetes_list_type': (str,),  # noqa: E501
            'x_kubernetes_map_type': (str,),  # noqa: E501
            'x_kubernetes_preserve_unknown_fields': (bool,),  # noqa: E501
            'x_kubernetes_validations': ([V1ValidationRule],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ref': '$ref',  # noqa: E501
        'schema': '$schema',  # noqa: E501
        'additional_items': 'additionalItems',  # noqa: E501
        'additional_properties': 'additionalProperties',  # noqa: E501
        'all_of': 'allOf',  # noqa: E501
        'any_of': 'anyOf',  # noqa: E501
        'default': 'default',  # noqa: E501
        'definitions': 'definitions',  # noqa: E501
        'dependencies': 'dependencies',  # noqa: E501
        'description': 'description',  # noqa: E501
        'enum': 'enum',  # noqa: E501
        'example': 'example',  # noqa: E501
        'exclusive_maximum': 'exclusiveMaximum',  # noqa: E501
        'exclusive_minimum': 'exclusiveMinimum',  # noqa: E501
        'external_docs': 'externalDocs',  # noqa: E501
        'format': 'format',  # noqa: E501
        'id': 'id',  # noqa: E501
        'items': 'items',  # noqa: E501
        'max_items': 'maxItems',  # noqa: E501
        'max_length': 'maxLength',  # noqa: E501
        'max_properties': 'maxProperties',  # noqa: E501
        'maximum': 'maximum',  # noqa: E501
        'min_items': 'minItems',  # noqa: E501
        'min_length': 'minLength',  # noqa: E501
        'min_properties': 'minProperties',  # noqa: E501
        'minimum': 'minimum',  # noqa: E501
        'multiple_of': 'multipleOf',  # noqa: E501
        '_not': 'not',  # noqa: E501
        'nullable': 'nullable',  # noqa: E501
        'one_of': 'oneOf',  # noqa: E501
        'pattern': 'pattern',  # noqa: E501
        'pattern_properties': 'patternProperties',  # noqa: E501
        'properties': 'properties',  # noqa: E501
        'required': 'required',  # noqa: E501
        'title': 'title',  # noqa: E501
        'type': 'type',  # noqa: E501
        'unique_items': 'uniqueItems',  # noqa: E501
        'x_kubernetes_embedded_resource': 'x-kubernetes-embedded-resource',  # noqa: E501
        'x_kubernetes_int_or_string': 'x-kubernetes-int-or-string',  # noqa: E501
        'x_kubernetes_list_map_keys': 'x-kubernetes-list-map-keys',  # noqa: E501
        'x_kubernetes_list_type': 'x-kubernetes-list-type',  # noqa: E501
        'x_kubernetes_map_type': 'x-kubernetes-map-type',  # noqa: E501
        'x_kubernetes_preserve_unknown_fields': 'x-kubernetes-preserve-unknown-fields',  # noqa: E501
        'x_kubernetes_validations': 'x-kubernetes-validations',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V1JSONSchemaProps - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ref (str): [optional]  # noqa: E501
            schema (str): [optional]  # noqa: E501
            additional_items (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.. [optional]  # noqa: E501
            additional_properties (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.. [optional]  # noqa: E501
            all_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            any_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            default (bool, date, datetime, dict, float, int, list, str, none_type): default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false.. [optional]  # noqa: E501
            definitions ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            dependencies ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            enum ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            example (bool, date, datetime, dict, float, int, list, str, none_type): JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.. [optional]  # noqa: E501
            exclusive_maximum (bool): [optional]  # noqa: E501
            exclusive_minimum (bool): [optional]  # noqa: E501
            external_docs (V1ExternalDocumentation): [optional]  # noqa: E501
            format (str): format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like \"0321751043\" or \"978-0321751041\" - isbn10: an ISBN10 number string like \"0321751043\" - isbn13: an ISBN13 number string like \"978-0321751041\" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like \"#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like \"rgb(255,255,2559\" - byte: base64 encoded binary data - password: any kind of string - date: a date string like \"2006-01-02\" as defined by full-date in RFC3339 - duration: a duration string like \"22 ns\" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like \"2014-12-15T19:30:20.000Z\" as defined by date-time in RFC3339.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            items (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes.. [optional]  # noqa: E501
            max_items (int): [optional]  # noqa: E501
            max_length (int): [optional]  # noqa: E501
            max_properties (int): [optional]  # noqa: E501
            maximum (float): [optional]  # noqa: E501
            min_items (int): [optional]  # noqa: E501
            min_length (int): [optional]  # noqa: E501
            min_properties (int): [optional]  # noqa: E501
            minimum (float): [optional]  # noqa: E501
            multiple_of (float): [optional]  # noqa: E501
            _not (V1JSONSchemaProps): [optional]  # noqa: E501
            nullable (bool): [optional]  # noqa: E501
            one_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            pattern (str): [optional]  # noqa: E501
            pattern_properties ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            properties ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            required ([str]): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            unique_items (bool): [optional]  # noqa: E501
            x_kubernetes_embedded_resource (bool): x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata).. [optional]  # noqa: E501
            x_kubernetes_int_or_string (bool): x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf:    - type: integer    - type: string 2) allOf:    - anyOf:      - type: integer      - type: string    - ... zero or more. [optional]  # noqa: E501
            x_kubernetes_list_map_keys ([str]): x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the \"x-kubernetes-list-type\" extension set to \"map\". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items.. [optional]  # noqa: E501
            x_kubernetes_list_type (str): x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) `atomic`: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) `set`:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x-kubernetes-map-type `atomic` or an      array with x-kubernetes-list-type `atomic`. 3) `map`:      These lists are like maps in that their elements have a non-index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays.. [optional]  # noqa: E501
            x_kubernetes_map_type (str): x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) `granular`:      These maps are actual maps (key-value pairs) and each fields are independent      from each other (they can each be manipulated by separate actors). This is      the default behaviour for all maps. 2) `atomic`: the list is treated as a single entity, like a scalar.      Atomic maps will be entirely replaced when updated.. [optional]  # noqa: E501
            x_kubernetes_preserve_unknown_fields (bool): x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden.. [optional]  # noqa: E501
            x_kubernetes_validations ([V1ValidationRule]): x-kubernetes-validations describes a list of validation rules written in the CEL expression language. This field is an alpha-level. Using this field requires the feature gate `CustomResourceValidationExpressions` to be enabled.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V1JSONSchemaProps - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ref (str): [optional]  # noqa: E501
            schema (str): [optional]  # noqa: E501
            additional_items (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.. [optional]  # noqa: E501
            additional_properties (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property.. [optional]  # noqa: E501
            all_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            any_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            default (bool, date, datetime, dict, float, int, list, str, none_type): default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false.. [optional]  # noqa: E501
            definitions ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            dependencies ({str: (bool, date, datetime, dict, float, int, list, str, none_type,)}): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            enum ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional]  # noqa: E501
            example (bool, date, datetime, dict, float, int, list, str, none_type): JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil.. [optional]  # noqa: E501
            exclusive_maximum (bool): [optional]  # noqa: E501
            exclusive_minimum (bool): [optional]  # noqa: E501
            external_docs (V1ExternalDocumentation): [optional]  # noqa: E501
            format (str): format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like \"0321751043\" or \"978-0321751041\" - isbn10: an ISBN10 number string like \"0321751043\" - isbn13: an ISBN13 number string like \"978-0321751041\" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like \"#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like \"rgb(255,255,2559\" - byte: base64 encoded binary data - password: any kind of string - date: a date string like \"2006-01-02\" as defined by full-date in RFC3339 - duration: a duration string like \"22 ns\" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like \"2014-12-15T19:30:20.000Z\" as defined by date-time in RFC3339.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            items (bool, date, datetime, dict, float, int, list, str, none_type): JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes.. [optional]  # noqa: E501
            max_items (int): [optional]  # noqa: E501
            max_length (int): [optional]  # noqa: E501
            max_properties (int): [optional]  # noqa: E501
            maximum (float): [optional]  # noqa: E501
            min_items (int): [optional]  # noqa: E501
            min_length (int): [optional]  # noqa: E501
            min_properties (int): [optional]  # noqa: E501
            minimum (float): [optional]  # noqa: E501
            multiple_of (float): [optional]  # noqa: E501
            _not (V1JSONSchemaProps): [optional]  # noqa: E501
            nullable (bool): [optional]  # noqa: E501
            one_of ([V1JSONSchemaProps]): [optional]  # noqa: E501
            pattern (str): [optional]  # noqa: E501
            pattern_properties ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            properties ({str: (V1JSONSchemaProps,)}): [optional]  # noqa: E501
            required ([str]): [optional]  # noqa: E501
            title (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            unique_items (bool): [optional]  # noqa: E501
            x_kubernetes_embedded_resource (bool): x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata).. [optional]  # noqa: E501
            x_kubernetes_int_or_string (bool): x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf:    - type: integer    - type: string 2) allOf:    - anyOf:      - type: integer      - type: string    - ... zero or more. [optional]  # noqa: E501
            x_kubernetes_list_map_keys ([str]): x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the \"x-kubernetes-list-type\" extension set to \"map\". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items.. [optional]  # noqa: E501
            x_kubernetes_list_type (str): x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) `atomic`: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) `set`:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x-kubernetes-map-type `atomic` or an      array with x-kubernetes-list-type `atomic`. 3) `map`:      These lists are like maps in that their elements have a non-index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays.. [optional]  # noqa: E501
            x_kubernetes_map_type (str): x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) `granular`:      These maps are actual maps (key-value pairs) and each fields are independent      from each other (they can each be manipulated by separate actors). This is      the default behaviour for all maps. 2) `atomic`: the list is treated as a single entity, like a scalar.      Atomic maps will be entirely replaced when updated.. [optional]  # noqa: E501
            x_kubernetes_preserve_unknown_fields (bool): x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden.. [optional]  # noqa: E501
            x_kubernetes_validations ([V1ValidationRule]): x-kubernetes-validations describes a list of validation rules written in the CEL expression language. This field is an alpha-level. Using this field requires the feature gate `CustomResourceValidationExpressions` to be enabled.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
