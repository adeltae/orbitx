# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

import time
import os

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

start = time.monotonic()
heartbeat_file = open(str(os.getpid()), 'w')

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    global start
    with grpc.insecure_channel('corn-syrup.uwaterloo.ca:28430') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    assert 42 == response.entities[0].data[0]
    print(int(time.monotonic() - start), file = heartbeat_file, flush=True)
    start = time.monotonic()


if __name__ == '__main__':
    while True:
        time.sleep(1)
        run()