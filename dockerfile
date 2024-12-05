
FROM python:3.14.0a1-slim-bookworm


COPY . .

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]