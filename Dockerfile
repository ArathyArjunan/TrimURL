FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collect static at build time
RUN python manage.py collectstatic --noinput

# expose is optional on Render, but fine
EXPOSE 8000

# migrate at start and bind to $PORT that Render provides
CMD ["sh","-c","python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --noinput || true && gunicorn shorturl.wsgi:application --bind  0.0.0.0:$PORT"]
