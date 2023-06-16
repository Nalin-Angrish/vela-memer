FROM python:3.9-slim
RUN apt update && apt install libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python -m bot test
CMD [ "python", "-m", "bot", "register", "run" ]