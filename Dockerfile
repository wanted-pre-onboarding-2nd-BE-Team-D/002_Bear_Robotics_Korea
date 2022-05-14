FROM python:3.10.4-slim-bullseye

#
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
#pip 버전 체크 방지
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
#.pyc 파일 생성방지
ENV PYTHONDONTWRITEBYTECODE 1
#파이썬 로그 출력 버퍼 제거
ENV PYTHONBUFFERED 1

WORKDIR /app

#local 현재 디렉토리의 requirements를 도커의 현재 디렉토리로 카피
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get -y install vim

#local => 도커 전체 옮기기
COPY . . 

## 포트 지정
EXPOSE 8000


