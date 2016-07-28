~/Downloads/protoc-3.0.0-beta-4-osx-x86_64/bin/protoc -I protos --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` protos/search_and_index.proto
