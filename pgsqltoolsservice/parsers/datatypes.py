# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

''' Pg data types. We need to make sure all the data types are defined with name starting with DATATYPE_ as we
pull them into the array of system datatypes '''

''' null Type '''
DATATYPE_NULL = 'NULL'


''' Numeric Types '''
DATATYPE_SMALLINT = 'int2'
DATATYPE_INTEGER = 'int4'
DATATYPE_BIGINT = 'int8'
DATATYPE_NUMERIC = 'numeric'
DATATYPE_REAL = 'float4'
DATATYPE_DOUBLE = 'float8'

''' Monetary Types '''
DATATYPE_MONEY = 'money'

''' Character Types '''
DATATYPE_CHAR = 'char'
DATATYPE_VARCHAR = 'varchar'
DATATYPE_BPCHAR = 'bpchar'
DATATYPE_TEXT = 'text'


''' Binary Data Types '''
DATATYPE_BYTEA = 'bytea'

''' Date/Time Types '''
DATATYPE_TIMESTAMP = 'timestamp'
DATATYPE_TIMESTAMP_WITH_TIMEZONE = 'timestamptz'
DATATYPE_DATE = 'date'
DATATYPE_TIME = 'time'
DATATYPE_TIME_WITH_TIMEZONE = 'timetz'
DATATYPE_INTERVAL = 'interval'

''' Boolean Type '''
DATATYPE_BOOL = 'bool'

''' Geometric Types '''
DATATYPE_POINT = 'point'
DATATYPE_LINE = 'line'
DATATYPE_LSEG = 'lseg'
DATATYPE_BOX = 'box'
DATATYPE_PATH = 'path'
DATATYPE_POLYGON = 'polygon'
DATATYPE_CIRCLE = 'circle'

''' Network Address Types '''
DATATYPE_CIDR = 'cidr'
DATATYPE_INET = 'inet'
DATATYPE_MACADDR = 'macaddr'

''' Bit String Types '''
DATATYPE_BIT = 'bit'
DATATYPE_BIT_VARYING = 'varbit'

''' Text Search Types '''
DATATYPE_TSVECTOR = 'tsvector'
DATATYPE_TSQUERY = 'tsquery'

''' UUID Type '''
DATATYPE_UUID = 'uuid'

''' XML Type '''
DATATYPE_XML = 'xml'

''' JSON Types '''
DATATYPE_JSON = 'json'


''' Range Types '''
DATATYPE_INT4RANGE = 'int4range'
DATATYPE_INT8RANGE = 'int8range'
DATATYPE_NUMRANGE = 'numrange'
DATATYPE_TSRANGE = 'tsrange'
DATATYPE_TSTZRANGE = 'tstzrange'
DATATYPE_DATERANGE = 'daterange'

''' Object Identifier Types '''
DATATYPE_OID = 'oid'
DATATYPE_REGPROC = 'regproc'
DATATYPE_REGPROCEDURE = 'regprocedure'
DATATYPE_REGOPER = 'regoper'
DATATYPE_REGOPERATOR = 'regoperator'
DATATYPE_REGCLASS = 'regclass'
DATATYPE_REGTYPE = 'regtype'
DATATYPE_REGROLE = 'regrole'
DATATYPE_REGNAMESPACE = 'regnamespace'
DATATYPE_REGCONFIG = 'regconfig'
DATATYPE_REGDICTIONARY = 'regdictionary'

''' pg_lsn Type '''
DATATYPE_PG_LSN = 'pg_lsn'


''' Arrays '''
DATATYPE_SMALLINT_ARRAY = '_int2'
DATATYPE_INTEGER_ARRAY = '_int4'
DATATYPE_BIGINT_ARRAY = '_int8'
DATATYPE_NUMERIC_ARRAY = '_numeric'
DATATYPE_REAL_ARRAY = '_float4'
DATATYPE_DOUBLE_ARRAY = '_float8'
DATATYPE_MONEY_ARRAY = '_money'
DATATYPE_VARCHAR_ARRAY = '_varchar'
DATATYPE_CHAR_ARRAY = '_bpchar'
DATATYPE_TEXT_ARRAY = '_text'

DATATYPE_BYTEA_ARRAY = '_bytea'
DATATYPE_TIMESTAMP_ARRAY = '_timestamp'
DATATYPE_TIMESTAMP_WITH_TIMEZONE_ARRAY = '_timestamptz'
DATATYPE_DATE_ARRAY = '_date'
DATATYPE_TIME_ARRAY = '_time'
DATATYPE_TIME_WITH_TIMEZONE_ARRAY = '_timetz'
DATATYPE_INTERVAL_ARRAY = '_interval'

DATATYPE_BIT_ARRAY = '_bit'
DATATYPE_BIT_VARYING_ARRAY = '_varbit'
DATATYPE_TSVECTOR_ARRAY = '_tsvector'
DATATYPE_TSQUERY_ARRAY = '_tsquery'
DATATYPE_UUID_ARRAY = '_uuid'
DATATYPE_XML_ARRAY = '_xml'
DATATYPE_JSON_ARRAY = '_json'
