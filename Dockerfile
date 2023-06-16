FROM python:3.9-slim
RUN apt install libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python -m bot test
CMD [ "python", "-m", "bot", "register", "run" ]