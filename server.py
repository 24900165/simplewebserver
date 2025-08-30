from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table</title>
    <h1 align="center">WEB DEVELOPMENT</h1>
</head>
<body bgcolor="lightblue">
    <table border="1" align="center" bgcolor="pink" cellpadding="10">
        <th><S class="No"></S></th>
        <th>Name of the layer</th>
        <th>Name of the protocol</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Application layer</td>
        <td>HTTP,FTP,DNS,Telnet,RDP</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Transport Layer</td>
        <td>TCP,UDP</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Internet layer</td>
        <td>ICMP,IGMP,ARP,IPV4/IPV6</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Network access layer</td>
        <td>Ethernet,FDDI,X.25,Frame Relay,Token Ring</td>
    </tr>
    
    </table>

</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()