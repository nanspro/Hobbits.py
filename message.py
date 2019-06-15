''' Message parsed from wire protocol's request message '''
class Request:

    def __init__(self, protocol, call, version, headers, body):
        self.protocol = protocol # EWP
        self.call = call # RPC or Gossip
        self.version = version
        self.headers = headers
        self.body = body