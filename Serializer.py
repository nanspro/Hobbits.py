from message import Request

''' Decodes the wire protocol message '''
def parse(msg):
    result = msg.split("\n", 1)
    cmd_string = result[0]
    payload = result[1]

    # if payload has a new line(only when both headers and body are present) then split
    if "\n" in payload:
        tmp = payload.split("\n", 1)
        payload = tmp[0] + tmp[1]

    cmd = cmd_string.split(" ", 5)
    protocol = cmd[0]
    version = cmd[1]
    call = cmd[2]
    headersLen = int(cmd[3])
    bodyLen = int(cmd[4])
    headers = payload[0 : headersLen]
    body = payload[headersLen : bodyLen + headersLen]

    request = Request(protocol, call, version, headers, body)
    return request.__dict__

''' Encodes the parsed message to a wire protocol message '''
def marshall(msg):
    if isinstance(msg, dict):
        protocol = msg.get("protocol")
        call = msg.get("call")
        version = msg.get("version")
        headers = msg.get("headers")
        body = msg.get("body")

        # If both headers and body are present then return by inserting a new line between them
        extra_line = "\n" if (len(headers) != 0 and len(body) != 0) else ""
        message = "{} {} {} {} {}\n{}" + extra_line + "{}"
        return message.format(protocol, version, call, len(headers), len(body), headers, body)




