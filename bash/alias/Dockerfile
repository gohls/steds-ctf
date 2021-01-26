FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN useradd -m -s /bin/rbash bash2
RUN echo bash2:bash2pass | chpasswd
RUN mkdir /home/bash2/.programs/
RUN echo "PATH=/home/bash2/.programs/" >> /home/bash2/.bashrc && echo "export PATH" >> /home/bash2/.bashrc
RUN ln -s /bin/ls /home/bash2/.programs/ls
RUN ln -s /bin/cat /home/bash2/.programs/cat
RUN ln -s /usr/bin/clear /home/bash2/.programs/clear
RUN ln -s /usr/bin/tput /home/bash2/.programs/tput

WORKDIR /home/bash2

COPY ./flag /home/bash2
COPY bashrc /home/bash2/.bashrc
COPY motd.tail /

CMD ["login", "-f", "bash2"]

