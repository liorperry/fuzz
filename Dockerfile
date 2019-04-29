FROM python:latest
RUN  apt-get update -y  &&  apt-get install -y	\
	autoconf \
	autoconf-archive \
	build-essential \
	curl \
	libpqxx-dev \
    	libboost-regex-dev \
	gcc \
	gcovr \
	gdb \
	git \
	htop \
	procps \
	vim \
	wget \
	dos2unix \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get autoremove
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN adduser --disabled-password --gecos "" sanin

USER sanin
WORKDIR /home/sanin
COPY . /home/sanin/fuzz
WORKDIR /home/sanin/fuzz

#RUN dos2unix app.py && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

CMD ["python app.py -o http://elasticsearch:9200 -i logs_index"]