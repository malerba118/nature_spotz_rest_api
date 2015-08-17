# nature_spotz_rest_api

A rest api for a nature service that will allow people to create
postings for spots in nature that they feel are worth visiting.

The api has been implemented with the django rest framework and I chose to use a
postgres database with postgis extensions because postgres is well-designed for
geospatial queries.

I plan to implement an android app and angular web service on top of this api.

You may log in with the following credentials:
    username: user1
    password: password
    
Login link: [http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/auth/login/?next=/api/v1/spots/](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/auth/login/?next=/api/v1/spots/)

Documentation:
[http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/docs/](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/docs/)


Here is some of the planning/preliminary documentation I did:
[https://docs.google.com/document/d/1Z6MHEu-rkFO6cNhaoxhaM4CXyqBe9jJ8hmXgzGO7wI4/edit?usp=sharing](https://docs.google.com/document/d/1Z6MHEu-rkFO6cNhaoxhaM4CXyqBe9jJ8hmXgzGO7wI4/edit?usp=sharing)


When retrieving spots (and other resources) there are many options to fitler by.

A "fields" query parameter can be used on any GET request and will return only the specified fields:
[http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?fields=title,description,location](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?fields=title,description,location)

"page" and "page_size" query parameters allow the user to specify the size of a result set and which page of results to view.
[http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?page=1&page_size=1](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?page=1&page_size=1)

"curr_loc" and "radius" query parameters allow the user to search for spots within a given radius(miles):
[http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?curr_loc=42,-74&radius=15](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?curr_loc=42,-74&radius=15)

"feature_type" and "activity_type" query parameters can be used multiple times in a url and return all spots matching any of the types listed:
[http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?activity_type=7&feature_type=11&feature_type=10](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/spots/?activity_type=7&feature_type=11&feature_type=10)

See [documentation](http://ec2-52-11-184-39.us-west-2.compute.amazonaws.com/api/v1/docs/) for more details.


