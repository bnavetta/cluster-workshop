FROM serrep3.services.brown.edu:5000/tensorflow

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /srv/my-task
WORKDIR /srv/my-task

CMD ["./task.py"]
