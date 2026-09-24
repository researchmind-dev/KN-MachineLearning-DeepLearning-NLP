## flask app for hello world

from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

"""
Setting `host="0.0.0.0"` tells the Flask server to bind to **all available network interfaces** on the machine, 
rather than just the default loopback interface (`127.0.0.1` / `localhost`).

---

**Key Advantages**

* **Local Network Access:** Other devices (laptops, phones, testing rigs) on the same Wi-Fi or LAN can access your Flask
application using your machine's private IP address (e.g., `[http://192.168.1.15:5000](http://192.168.1.15:5000)`).

* **Container & Virtualization Friendly:** When running inside Docker containers or VMs, 
using `127.0.0.1` restricts access strictly inside the container filesystem. Binding to `0.0.0.0` 
allows Docker port-mapping (`-p 5000:5000`) to route external traffic into the container.

* **Multi-Interface Listening:** If your server has multiple Network Interface Cards (NICs) 
or multiple IPs (Ethernet, Wi-Fi, VPN), `0.0.0.0` listens on all of them simultaneously 
without needing separate configurations.

---

**Comparison**

| Host Setting | What It Binds To | Accessible From |
| --- | --- | --- |
| `127.0.0.1` *(Default)* | Loopback only | Only the local machine running the code |
| `0.0.0.0` | All network adapters | Local machine + LAN devices + Docker host |

---

**Security Note**

> `0.0.0.0` exposes your app to your entire local network. If your machine is connected to a public network or lacks 
a firewall, anyone on that network can send requests to your server.

> For production environments, do not rely on `app.run()`; instead, bind a WSGI server 
like **Gunicorn** or **uWSGI** to `0.0.0.0` behind a reverse proxy like Nginx.
"""