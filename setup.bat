cd ./tests/keys
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -config localhost.cnf
cd ../../..