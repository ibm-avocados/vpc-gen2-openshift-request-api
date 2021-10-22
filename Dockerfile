FROM fedora:latest
RUN dnf upgrade -y
RUN dnf install -y \
    python3-pip \
    wget \
    unzip 

RUN curl -fsSL https://clis.cloud.ibm.com/install/linux | sh && \
ibmcloud config --check-version=false

COPY app.py /srv/
COPY requirements.txt /srv/
WORKDIR /srv

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD ["python3", "app.py"]