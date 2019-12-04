#!/usr/bin/python

import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8000

build_data = {
    "id": "env_appname_modulename:12.1",
    "envName": "env",
    "appName": "appname",
    "moduleName": "modulename",
    "parentImage": "192.168.1.2:5000/weblogc.12.1",
    "context": "xxx",
    "mountnfs": [
        {
            "srcDir": "172.10.1.100:/share",
            "destDir": "/share"
        }
    ],
    "datasource": [
        {
            "dsdriver": "abc",
            "dsjndiname": "jdbc/dafdasf",
            "dsname": "xxx",
            "dsurl": "jdbc:oracle:thin:@(dsagasgagasg)",
            "dsusername": "hello",
            "dspassword": "world",
            "globalTransactionProtocol": "OnePhaseCommit"
        }
    ],
    "java_options": "-Dfile.encoding=utf-8",
    "charset": "UTF-8",
    "topic": {
        "access": "env-appname-modulename-access",
        "server": "env-appname-modulename-server"
    }
}

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(build_data))
        return


try:
    server = HTTPServer(("", PORT_NUMBER), myHandler)
    print("Started httpserver on port", PORT_NUMBER)
    server.serve_forever()

except KeyboardInterrupt:
    print("Ctrl C received, shutting down the web server")
    server.socket.close()