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
