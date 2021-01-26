FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN useradd -m -s /bin/rbash net1
RUN echo net1:donkeykongmemes | chpasswd
RUN mkdir /home/net1/.programs/
RUN echo "PATH=/home/net1/.programs/" >> /home/net1/.bashrc && echo "export PATH" >> /home/net1/.bashrc
RUN ln -s /bin/ls /home/net1/.programs/ls
RUN ln -s /bin/cat /home/net1/.programs/cat
RUN ln -s /usr/bin/clear /home/net1/.programs/clear
RUN ln -s /usr/bin/clear_console /home/net1/.programs/clear_console
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

WORKDIR /home/net1

RUN echo "clear" >> .bashrc
RUN echo "echo 'stedsCTF #1'" >> .bashrc
RUN echo "echo 'You are in a restricted bash shell, feel free to explore!'" >> .bashrc
COPY flag.txt /home/net1

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"] 
