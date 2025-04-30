from sample_server import SampleServer
from drunkard import Drunkard


# Inherit all the functions from the pre-supplied sample server class.
class DrunkardServer(SampleServer):

    # This is a method from the 'grandparent' class, BaseHTTPRequestHandler, which we receive through SampleServer, and we know is called every time the server, which this handler will power, receives an HTTP POST request.
    def do_POST(self):
        # Use a method from our helper SampleServer class (parent) to extract the data we need once a post request is made.
        post_data = self.get_post_data()
        # Create an instance of the drunkard class in order to process the data we receive.
        # NB: Really we should only do this once per instance.
        drunkard = Drunkard()
        # Extract the supplied 2D space dimensions from the POST request.
        # This is our 'contract' with the client; the structure they have to use in order for us to be able to understand the request.
        sent_width = post_data['width']
        sent_height = post_data['height']
        # Send the drunkard home, supplying the extracted data, as we would normally.
        path = drunkard.go_home(sent_width, sent_height)
        # Again invoke an inherited method from the helper SampleServer class, in order to send a response to the POST request received, containing the path that the drunkard took.
        self.send_post_response(path)
