''' Structure of Message parsed from wire protocol's request message '''


class Request:
    ''' Structure of Message parsed from wire protocol's request message '''
    def __init__(self, protocol, call, version, headers, body):
        self.protocol = protocol  # EWP
        self.call = call  # RPC or Gossip
        self.version = version
        self.headers = headers
        self.body = body

    def get_headers(self):
        ''' Get headers of a request'''
        return self.headers

    def get_body(self):
        ''' Get body of a request'''
        return self.body
