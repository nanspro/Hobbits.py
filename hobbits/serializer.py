''' Defining methods to encode and decode messages '''
from hobbits.message import Request


def parse(msg):
    ''' Decodes the wire protocol message '''

    result = msg.split("\n", 1)
    cmd_string = result[0]
    payload = result[1]

    # if payload has a new line(both headers and body are present) then split
    if "\n" in payload:
        tmp = payload.split("\n", 1)
        payload = tmp[0] + tmp[1]

    cmd = cmd_string.split(" ", 5)
    protocol = cmd[0]
    version = cmd[1]
    call = cmd[2]
    headers_len = int(cmd[3])
    body_len = int(cmd[4])
    headers = payload[0: headers_len]
    body = payload[headers_len: body_len + headers_len]

    request = Request(protocol, call, version, headers, body)
    return request.__dict__


def marshall(msg):
    ''' Encodes the parsed message to a wire protocol message '''

    if isinstance(msg, dict):
        protocol = msg.get("protocol")
        call = msg.get("call")
        version = msg.get("version")
        headers = msg.get("headers")
        body = msg.get("body")

        # If both headers and body are present then return by inserting \
        #  a new line between them
        l_1 = len(headers)
        l_2 = len(body)
        extra_line = "\n" if (l_1 != 0 and l_2 != 0) else ""
        message = "{} {} {} {} {}\n{}" +  \
            extra_line + "{}"
        return message.format(protocol, version, call, len(headers),
                              len(body), headers, body)
    return ''
