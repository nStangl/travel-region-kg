# tum-ba-thesis-code

## GraphDB Client
The client Jupyter Notebook uses a python library ([graphdb-python-api](https://github.com/patzomir/graphdb-python-api)).
Note that you have to generate the actual usable (client) library yourself with the codegen tool [swagger.io](https://swagger.io).
The generated library can be found in this repo under `python-client/`.
Note that you can use swagger to create the client library for a wide choice of languages. Though it wouldn't be difficult to do it yourself.

### Generate client library
Take the swagger file [rdf4j.swagger](https://github.com/patzomir/graphdb-python-api/blob/main/rdf4j.swagger) from the git repo and copy it into [swagger.io](https://swagger.io), select Client>Python and download the resulting library.
Then import the required modules.
