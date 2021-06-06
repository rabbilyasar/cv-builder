FROM python:3.9.5-alpine

LABEL maintainer="rabbil"

ENV PYTHONBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/api

RUN apk add --no-cache \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev git
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/api
RUN pip install -r requirements.txt

COPY .env .env




EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]