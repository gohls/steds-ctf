FROM ubuntu:latest
RUN apt-get update && apt-get -y install socat
EXPOSE 6001
CMD socat TCP-LISTEN:6001,reuseaddr,fork EXEC:"echo 'username: net1\npassword: donkeykongmemes\nport: 6002'"
