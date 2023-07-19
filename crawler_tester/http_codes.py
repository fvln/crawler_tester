CODES_SUCCESS = [
    200,  # OK
    201,  # Created
    202,  # Accepted
    203,  # Non-Authoritative Information
    204,  # No Content
    205,  # Reset Content
    206,  # Partial Content
    # Useless
    # 207,  # Multi-Status
    # 208,  # Already Reported
    # 210,  # Content Different
    # 226,  # IM Used
]

CODES_REDIRECT = [
    301,  # Moved Permanently
    302,  # Found
    303,  # See Other
    305,  # Use Proxy (depuis HTTP/1.1)
    307,  # Temporary Redirect
    308,  # Permanent Redirect
    # TODO ?
    # 300,  # Multiple Choices
    # 304,  # Not Modified
    # Useless
    # 306,  # inutilisé
    # 310,  # Too many Redirects
]

CODES_ERR_CLIENT = [
    400,  # Bad Request
    401,  # Unauthorized
    402,  # Payment Required
    403,  # Forbidden
    404,  # Not Found
    405,  # Method Not Allowed
    406,  # Not Acceptable
    407,  # Proxy Authentication Required
    408,  # Request Time-out
    409,  # Conflict
    410,  # Gone
    411,  # Length Required
    412,  # Precondition Failed
    413,  # Request Entity Too Large
    414,  # Request-URI Too Long
    415,  # Unsupported Media Type
    416,  # Requested range unsatisfiable
    417,  # Expectation failed
    418,  # I’m a teapot
    419,  # Page expired
    421,  # Bad mapping / Misdirected Request
    422,  # Unprocessable entity
    423,  # Locked
    424,  # Method failure
    425,  # Too Early
    426,  # Upgrade Required
    427,  # Invalid digital signature
    428,  # Precondition Required
    429,  # Too Many Requests
    431,  # Request Header Fields Too Large
    449,  # Retry With
    450,  # Blocked by Windows Parental Controls
    451,  # Unavailable For Legal Reasons
    456,  # Unrecoverable Error
]

CODES_ERR_SERVER = [
    500,  # Internal Server Error
    501,  # Not Implemented
    502,  # Bad Gateway ou Proxy Error
    503,  # Service Unavailable
    504,  # Gateway Time-out
    505,  # HTTP Version not supported
    506,  # Variant Also Negotiates
    507,  # Insufficient storage
    508,  # Loop detected
    509,  # Bandwidth Limit Exceeded
    510,  # Not extended
    511,  # Network authentication required
]
