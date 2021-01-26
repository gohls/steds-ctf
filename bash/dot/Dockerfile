FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN useradd -m -s /bin/rbash dot
RUN echo dot:bash0pass | chpasswd
RUN mkdir /home/dot/.programs/
RUN ln -s /bin/ls /home/dot/.programs/ls
RUN ln -s /bin/cat /home/dot/.programs/cat
RUN ln -s /usr/bin/clear /home/dot/.programs/clear
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY dot-flag /home/dot/.flag
COPY bashrc /home/dot/.bashrc
COPY motd.tail /

WORKDIR /home/dot

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
