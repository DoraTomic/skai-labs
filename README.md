TASK 1
Task was made in VisualStudio Code.
First, 'index.html' and 'main.js' are taken from Openlayers library for display of Simple Map.
Then Vite('vite-project') and Openlayers ('my-app') were installed.
In 'my-app' in 'main.js' file, data was loaded first. It imports polygon data from a JSON file named 'polygon.json'. The data is loaded as JSON object into a variable named 'users'. Then, the coordinates of the polygon are extracted and an OpenLayers 'Feature' object is created that represents the polygon geometry. The coordinates are transformed to EPSG:projection. Also, the centroid of the polygon is calculated.
Vector layer is added in creating map. It represents the polygon geometry using 'Vector' with 'Polygon' feature and is custom styled. The view is set to the center of the polygon and is zoomed.
Application starts from the terminal by positioning in the 'my-app' file with the 'npm start' command and then clicking on the host link.

TASK 2
In 'main.py' a simple Flask application was defined with a single endpoint '/saledetector' which is implemented using Flask-RESTful.
First, instances of the Flask application and Flask-RESTful API are created.
Then three request parsers are defined: 
-'root_parser' is used to parse the root-level JSON object in the request body. It expexts two required keys: 'productionListings' and 'salesTransactions', both of wich are dictionaties.
-'message_parser1' is used to parse the 'productListings' object. It expects two required keys: 'productID' and 'authorizedSellerID'.
-'message_parser2' is used to parse the 'saleTransactions' object. It expects two required keys: 'productID' and 'sellerID'.
Resaource Class inherits from 'Resource' and it defines method 'post()' which handles POST requests to the '/saledetector' endpoint. Inside the 'post()' method arguments are parsed using the defined parsers. It checks if the 'productID' from 'productListings' matches the 'productID' from 'salesTransactions'. If it matches, it further checks if the 'authorizedSellerID' from 'productListings' is different from the 'sellerID' from 'salesTransactions'. Depending on the conditions, it constructs a response JSON object 
indicating unauthorized sales or no unauthorized sales. The respose is returned with an appropriate HTTP status code.
'test.py' is a script that makes an HTTP POST request with JSON object.
Flask application is started by running 'main.py' in command prompt and requests are sent by running 'test.py' in another command prompt.

TASK 3
'main.py' defines a Flask application with a single endpoint '/interviewsscheduler' implemented using Flask-RESTful.
Instances of the Flask application and the Flask-RESTful API are created.
Then a request parser named 'arg_parser' is created using' reqparse.RequestParser()'. Two arguments are added to the parser: 'start_times' and 'end_times'. Both are expected to be lists of integers and are required.
Resource Class 'InterviewScheduler' defines method 'post()', which handles POST requests to created endpoint. Inside the method 'post()', request arguments are parsed using the 'arg_parser'. The 'start_times' and 'end_times' lists are retrieved from the parsed arguments. If lenghts of these lists are not same, it returns a response with an error message. Then, it calls method 'calculate_max_interviews', which takes those two lists that represent the start and end times of interview intervals.
Method iterates through the intervals and keeps track of the maximum number of interviews that can be conducted concurrently. Then it returns that number. 
The result is then in method 'post()' returned in a JSON response with an appropriate HTTP status code.
Flask application is started by running 'main.py' in command prompt and requests are sent by running 'test.py' in another.
