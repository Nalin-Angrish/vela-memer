FROM python:3.9-slim
RUN pip install --upgrade pip && apt update && apt install build-essential python3-dev libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python -m bot test
CMD [ "python", "-m", "bot", "register", "run" ]