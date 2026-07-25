FROM python:3.13-slim AS builder 
RUN mkdir /app
 
WORKDIR /app
 
# Disables the creation of .pyc files (compiled bytecode).
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1  
 
RUN pip install --upgrade pip 
 
COPY requirements.txt  /app/
 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/

# Multi-stage builds
FROM python:3.13-slim
 
RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
WORKDIR /app

# Copy Application Code with Permissions:
COPY --chown=appuser:appuser . .
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Switch to Non-Root User 
USER appuser

# Run collectstatic to compile static files for Whitenoise
RUN python manage.py collectstatic --noinput
 
EXPOSE 8000 
 
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "mysite.wsgi:application"]
