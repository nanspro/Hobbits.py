from __future__ import print_function
import sys, pytest

from Serializer import parse, marshall

def test_parsing():
    msg = 'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}'
    msg2 = 'EWP 0.2 RPC 0 27\n<27 bytes binary body data>'
    msg3 = 'EWP 0.2 GOSSIP 25 16\n25 bytes of binary header\n16 bytes of body'

    assert parse(msg) == {'protocol': 'EWP', 'call': 'RPC', 'version': '0.2', 'headers': '', 'body': '{"id":1,"method_id":0x00}'}
    assert parse(msg2) == {'protocol': 'EWP', 'call': 'RPC', 'version': '0.2', 'headers': '', 'body': '<27 bytes binary body data>'}
    assert parse(msg3) == {'protocol': 'EWP', 'call': 'GOSSIP', 'version': '0.2', 'headers': '25 bytes of binary header', 'body': '16 bytes of body'} 

def test_marshall():
    msg = {'protocol': 'EWP', 'call': 'RPC', 'version': '0.2', 'headers': '', 'body': '{"id":1,"method_id":0x00}'}
    msg2 = {'protocol': 'EWP', 'call': 'RPC', 'version': '0.2', 'headers': '', 'body': '<27 bytes binary body data>'}
    msg3 = {'protocol': 'EWP', 'call': 'GOSSIP', 'version': '0.2', 'headers': '25 bytes of binary header', 'body': '16 bytes of body'}

    assert marshall(msg) == 'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}'
    assert marshall(msg2) == 'EWP 0.2 RPC 0 27\n<27 bytes binary body data>'
    assert marshall(msg3) == 'EWP 0.2 GOSSIP 25 16\n25 bytes of binary header\n16 bytes of body'


# if __name__ == "__main__":
#     test_parsing()
#     test_marshall()
