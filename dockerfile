FROM python:3.11-slim

WORKDIR /Structured_enquiry

COPY . .

RUN pip install pytest

CMD ["python", "student.py"]
