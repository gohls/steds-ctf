FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/rbash bash1
RUN echo bash1:bash1pass | chpasswd
RUN mkdir /home/bash1/.programs/
RUN echo "PATH=/home/bash1/.programs/" >> /home/bash1/.bashrc && echo "export PATH" >> /home/bash1/.bashrc
RUN ln -s /bin/ls /home/bash1/.programs/ls
RUN ln -s /bin/cat /home/bash1/.programs/cat
RUN ln -s /usr/bin/clear /home/bash1/.programs/clear
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

WORKDIR /home/bash1

COPY ./- /home/bash1/-flag
COPY bashrc /home/bash1/.bashrc
COPY motd.tail /

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
