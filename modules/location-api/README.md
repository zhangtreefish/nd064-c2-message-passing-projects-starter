## How to run
### First set up a virtual environment:
conda --version 
conda env remove -n ENV_NAME
conda create --name udaconnect_env python=3.8
conda info --envs
conda activate udaconnect_env
### inside the virtual environment:
pip3 install grpcio-tools
conda list
#### Generating gRPC files
`pip install grpcio-tools grpcio`
`pip freeze > requirements.txt`
`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto`
`python3 main.py`

## Referencesgrpc vs REST:
gRPC vs REST: https://blog.dreamfactory.com/grpc-vs-rest-how-does-grpc-compare-with-traditional-rest-apis/
example gRPC uptaking image and sending to REST: https://doordash.engineering/2020/10/16/building-an-image-upload-endpoint-in-a-grpc-and-kotlin/
https://stackoverflow.com/questions/18351516/comparison-between-http-and-rpc
https://developers.google.com/protocol-buffers/docs/proto3
what is rpc in .proto?
is message and service required in .proto?
https://grpc.io/docs/languages/python/quickstart/
https://visualstudiomagazine.com/articles/2020/01/16/grpc-well-known-types.aspx
""grpc_message":"Exception calling application: created_at","grpc_status":2" ?
https://stackoverflow.com/questions/62315295/convert-datetime-to-protobuf-timestamp-in-python
https://www.programiz.com/python-programming/datetime/strftime
https://strftime.org/
https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import
https://github.com/protocolbuffers/protobuf/issues/3986
https://stackoverflow.com/questions/35407560/attributeerror-dict-object-has-no-attribute-predictors

:"Exception calling application: Invalid payload: {'creation_time': ['Not a valid datetime"...: it required a strfdatetime, not datetime.
:"	status = StatusCode.UNKNOWN
	details = "Exception calling application: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/."
https://realpython.com/python-microservices-grpc/
So I added the "with" block as per https://flask.palletsprojects.com/en/2.0.x/appcontext/, but got '...NameError: name 'init_db' is not defined"'. How is init_db imported? If I use db.init_app(app) instead, then upon running writer.py I got "status = StatusCode.UNAVAILABLE details = "failed to connect to all addresses" grpc_status":14}
https://stackoverflow.com/questions/419163/what-does-if-name-main-do

If moving writer.py to outside app/: get import error on location+pb2_grpc: Why?
https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters

__all__:https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
downgrade to python 3.7.5 to overcome psycopg2 intall problem on my Big Sur Mac: https://stackoverflow.com/questions/62898911/how-to-downgrade-python-version-from-3-8-to-3-7-mac
and https://github.com/pyenv/pyenv/issues/849#issuecomment-863456765 does not work in conda env; 
change python version in conda: https://chris35wills.github.io/conda_python_version/

removed `export PATH="/Users/mommy/Library/Python/3.9/bin:$PATH"` from .zshrc; added per https://github.com/pyenv/pyenv/issues/849
had to run `pyenv install 3.7.0` not  `pyenv install 3.7`//error:

(udaconnect_env) mommy@Mommys-iMac location-api % pip install -r requirements.txt
(udaconnect_env) mommy@Mommys-iMac location-api % python3 app/grpc_server.py
`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto`
in Location Schema, why validate for id in create?
https://stackoverflow.com/questions/35282222/in-python-how-do-i-cast-a-class-object-to-a-dict/35282286

## Local developement
`vagrant up`
At modules/location-api, after inside venv or a conda env: `pip install -r requirements.txt`, then:
terminal one: `kubectl port-forward svc/postgres 5432:5432`
terminal two: `python3 app/grpc_server.py`
termnal three: `python3 app/writer.py` or `python3 app/reader.py` 