FROM ubuntu:latest
RUN apt-get update && apt-get -y install socat
EXPOSE 1234
CMD socat TCP-LISTEN:1234,reuseaddr,fork EXEC:"echo ZmxhZ3t0ZXN0aW5nMTIzfQo="
