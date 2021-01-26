FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN useradd -m -s /bin/bash bash3
RUN echo bash3:bash3pass | chpasswd
RUN apt update && apt install locate sudo

WORKDIR /home/bash3

COPY bashrc /home/bash3/.bashrc
COPY flag /home/bash3/flag
COPY motd.tail /
COPY flag_a /usr/share/bash-completion/flag

USER root
ADD /sudoers.tx /etc/sudoers
RUN chmod 440 /etc/sudoers
CMD ["login", "-f", "bash3"]
