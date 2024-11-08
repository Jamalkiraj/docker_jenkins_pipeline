FROM python:3.9-slim
WORKDIR /usr/src/app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
