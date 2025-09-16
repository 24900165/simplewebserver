# EX01 Developing a Simple Webserver
## Date:30-08-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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

 
```

## OUTPUT:
![alt text](<Screenshot 2025-08-30 094455.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
