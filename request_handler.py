from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views import get_all_posts
from views import get_all_users
from views import get_all_tags, create_new_tag
from views import create_user, get_all_users, get_single_user, login_user
from views import get_all_subscriptions_by_user, create_subscription, delete_subscription
from views import get_all_categories, create_new_category
from views import create_post, get_posts_by_user_id
from views import get_single_post
from views import edit_post
from views import delete_post
from views import get_posts_by_title


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return (resource, key, value)

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        response = {}  # Default response
        # Set the response code to 'Ok'
        self._set_headers(200)

        # Parse the URL and capture the tuple that is returned
        # OG code -->(resource, id) = self.parse_url(self.path)

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed

            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            elif resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"
            # elif resource == "subscriptions":
            #     if id is not None:
            #         response = f"{get_all_subscriptions_by_user(id)}"
                # else:
                    # response = f"{get_all_users()}"

                    # add in an elif statement for if resource == "tags"
                    # to get_all_tags()

            # if resource == "moods":
            #     response = f"{get_all_moods()}"

            if resource == "tags":
                response = f"{get_all_tags()}"

            if resource == "categories":
                response = f"{get_all_categories()}"

        elif len(parsed) == 3:
            (resource, key, value) = parsed
            if key == "follower" and resource == "subscriptions":
                response = get_all_subscriptions_by_user(value)
            if key == "user_id" and resource == "posts":
                response = get_posts_by_user_id(value)
            if key == "title" and resource == "posts":
                response = get_posts_by_title(value)
        #     if key == "q" and resource == "entries":
        #         response = get_entry_by_search(value)

# f string needed because previous response is not a string.
        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        elif resource == 'register':
            response = create_user(post_body)
        elif resource == 'tags':
            response = create_new_tag(post_body)
        elif resource == 'subscriptions':
            response = create_subscription(post_body)
        elif resource == 'categories':
            response = create_new_category(post_body)
        elif resource == 'posts':
            response = create_post(post_body)
            # write a new if statement for if resource = "tags"
            # new_tag = create_new_tag(post_body)

        self.wfile.write(f"{response}".encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "posts":
            success = edit_post(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "subscriptions":
            if id is not None:
                delete_subscription(id)
        if resource == 'posts':
            if id is not None:
                delete_post(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
