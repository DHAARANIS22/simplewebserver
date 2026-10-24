from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Device details</title>
        <body align="center"bgcolor="lavender">
            
            <h2>Dhaarani-26019313</h2>
            <h3>My laptop configurations</h3>
            <table border="2" align="center" cellspacing="2 cellpadding=2">
                <tr align="center">
                    <th>S.no</td>
                    <th>Device type</td>
                    <th>Device info</td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Device name</td>
                    <td>TL15-53M-G2</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Processor</td>
                    <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Installed RAM</td>
                    <td>16.0 GB (15.7 GB usable)</td>

                </tr>
                <tr>
                    <td>4</td>
                    <td>Graphics card</td>
                    <td>16.0 GB (15.7 GB usable)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Storage</td>
                    <td>109 GB of 477 GB used</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Device Id</td>
                    <td>D80ABB6F-8E77-4AF7-A42A-8A9FAFC276E3</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Product Id</td>
                    <td>00342-42954-11727-AAOEM</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>System type</td>
                    <td>64-bit operating system, x64-based processor</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>Pen and touch</td>
                    <td>No pen or touch input is available for this display</td>
                </tr>

            </table>
        </body>
    </head>
        
</html>
        

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()