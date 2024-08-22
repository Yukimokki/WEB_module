from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Why there is no ___init__?"""

    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
  <div class="container">
    <div class="row mt-5">
        <div class="col-6">
            <div class="card bg-primary">
                <div class="card-body text-white">
                    <h3 class="class-title">Contact information</h3>
                    <div class="row">
                    <div class="col-6">Moscow</div>
                    <div class="col-6">+7 777 777 7777</div>
                    <div class="col-6">St.Petersburg</div>
                    <div class="col-6">+8 888 888 8888</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-6">
            <div class="card">
                <div class="card-body">
                    <h3 class="class-title">Leave your message</h3>
                    <form>
                        <div class="mb-3">

                            <input name = "name" type="text" class="form-control" id="exampleInputEmail1" placeholder="Name"
                                   aria-describedby="emailHelp">

                        </div>
                        <div class="mb-3">

                            <input name = "email" type="email" class="form-control" id="exampleInputEmail1" placeholder="email"
                                    aria-describedby="emailHelp">
                        </div>
                            <div class="mb-3">

                                <textarea name = "message" class="form-control" placeholder="Your message" id="exampleFormControlTextarea1" rows="3"></textarea>

                            </div>
                        <button type="submit" class="btn btn-primary form-control">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
  </div>
  </body>
    </html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s,%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
