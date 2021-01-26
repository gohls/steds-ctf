FROM ubuntu:latest
RUN apt-get update && apt-get -y install socat
EXPOSE 7001
CMD socat TCP-LISTEN:7001,reuseaddr,fork EXEC:"echo 'all hail the nmap king\nstedsCTF{nmap1sl0venmap1sl1fe}'"
