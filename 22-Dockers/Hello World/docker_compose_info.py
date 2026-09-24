"""
Docker Compose allows you to define and run multi-container setups using a single `docker-compose.yml` file. 
Docker automatically creates a shared network where containers can reach each other using their service names 
as hostnames.

---

**1. Project Structure**

```text
my-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

```

---

**2. Update Files**

**`requirements.txt`**

```text
flask
redis
psycopg2-binary

```

**`app.py`**
Use the service names (`redis`, `db`) as the connection hosts instead of `localhost`:

```python
import os
import psycopg2
import redis
from flask import Flask

app = Flask(__name__)

# Connect using service names defined in docker-compose.yml
r = redis.Redis(host='redis', port=6379)

def get_db_connection():
    return psycopg2.connect(
        host='db',
        database=os.environ.get('POSTGRES_DB', 'flaskdb'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'secret123')
    )

@app.route('/')
def index():
    # Increment Redis visitor count
    visits = r.incr('visitor_count')
    return f"Hello World! Page visits tracked by Redis: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

**`Dockerfile`**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]

```

---

**3. Define `docker-compose.yml**`

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - POSTGRES_DB=flaskdb
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret123
    depends_on:
      - redis
      - db

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: flaskdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret123
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:

```

---

**4. Running and Managing the App**

* **Start all services in background:**
```bash
docker compose up -d --build

```


* **View running services:**
```bash
docker compose ps

```


* **Inspect logs:**
```bash
docker compose logs -f web

```


* **Stop and tear down all containers:**
```bash
docker compose down

```


*(Add `-v` to also delete persistent database volumes: `docker compose down -v`)*
"""


"""
* **`version: '3.8'`**
* Specifies the Docker Compose file format version and feature set.


* **`services:`**
* Defines all individual containers that make up the application stack (`web`, `redis`, `db`).



---

**`web` Service (Flask App)**

* **`build: .`**
* Builds a custom Docker image using the `Dockerfile` located in the current directory (`.`).


* **`ports: ["5000:5000"]`**
* Maps port `5000` on your host machine to port `5000` inside the container (`host:container`).


* **`environment:`**
* Injects environment variables inside the container so Flask can read the DB credentials at runtime.


* **`depends_on:`**
* Ensures `redis` and `db` containers start before the `web` container is launched.



---

**`redis` Service (Cache / Store)**

* **`image: redis:alpine`**
* Pulls the official, lightweight Redis image directly from Docker Hub.


* **`ports: ["6379:6379"]`**
* Exposes Redis port `6379` to the host machine for local debugging or external tools.



---

**`db` Service (PostgreSQL)**

* **`image: postgres:15-alpine`**
* Pulls the official lightweight PostgreSQL 15 image from Docker Hub.


* **`environment:`**
* Sets required initialization credentials (`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`) 
to automatically create the database on first boot.


* **`volumes: [postgres_data:/var/lib/postgresql/data]`**
* Mounts the named volume to PostgreSQL’s data directory to persist database data across container restarts.


* **`ports: ["5432:5432"]`**
* Exposes the Postgres port to your host machine for connecting via GUI tools (e.g., DBeaver, pgAdmin).



---

**Top-Level `volumes:**`

* **`postgres_data:`**
* Declares a Docker-managed persistent volume on your host drive so data isn't lost when containers are stopped 
or removed.
"""