FROM jenkins/jenkins:lts

USER root

# Встановлюємо системні залежності для Python і Tkinter
RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 \
       python3 \
       python3-pip \
       python3-tk \
       tcl-dev \
       tk-dev \
       build-essential

# Оновлюємо pip
RUN python3 -m pip install --upgrade pip

# Установка Docker CLI (необхідно, якщо вам це потрібно)
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli

USER jenkins
RUN jenkins-plugin-cli
