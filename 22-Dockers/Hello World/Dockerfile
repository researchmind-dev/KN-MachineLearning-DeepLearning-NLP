FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]

"""
* **`FROM python:3.7`**
* Sets the base image containing Debian OS with Python 3.7 pre-installed.
* Every Dockerfile must start with a `FROM` instruction.


* **`COPY . /app`**
* Copies all files and folders from your current local directory (`.`) into the `/app` folder inside the container.


* **`WORKDIR /app`**
* Sets `/app` as the active working directory for all following commands (`RUN`, `CMD`, etc.).
* Automatically creates the folder if it doesn't exist.


* **`RUN pip install -r requirements.txt`**
* Runs during the image **build** process.
* Installs all listed Python dependencies (like Flask, NumPy, Pandas) inside the image.


* **`CMD ["python", "app.py"]`**
* Specifies the default command executed when the container **starts**.
* Launches your Flask application.



---

> **Pro-Tip for Docker Caching:** Swap the order to avoid reinstalling dependencies every time you edit your code:
> ```dockerfile
> WORKDIR /app
> COPY requirements.txt .
> RUN pip install -r requirements.txt
> COPY . .
> CMD ["python", "app.py"]
> 
> ```
> 
>


To build and run your Flask container from the terminal, follow these steps:

---

**1. Build the Docker Image**

Run this command in the folder containing your `Dockerfile`, `app.py`, and `requirements.txt`:

```bash
docker build -t my-flask-app .

```

* `-t my-flask-app`: Tags (names) your image `my-flask-app`.
* `.`: Specifies the current directory as the build context.

---

**2. Run the Container**

Start a container from the image and map the network port:

```bash
docker run -d -p 5000:5000 --name flask-container my-flask-app

```

* `-d`: Runs the container in the background (detached mode).
* `-p 5000:5000`: Maps port `5000` of your local host machine to port `5000` inside the container (`host_port:container_port`).
* `--name flask-container`: Assigns a name to your running container instance.

---

**3. Test the App**

Open your browser or run curl:

```bash
curl http://localhost:5000

```

It should return: `Hello World`.

---

**Useful Management Commands**

* **View running containers:** `docker ps`
* **Check logs (useful for debugging errors):** `docker logs flask-container`
* **Stop the container:** `docker stop flask-container`
* **Remove the container:** `docker rm flask-container`
"""