# Docker Fundamentals & Workflow Guide

This document summarizes the core Docker concepts we discussed, tailored specifically to running Docker on Windows and optimizing python-based machine learning pipelines.

---

## 1. What is Docker? (Windows vs. Linux)

Docker allows you to package your application and all of its system dependencies (Python versions, packages, environment variables, system tools) into a self-contained unit called a **Container**.

Even though you are running Windows, Docker Desktop allows you to build and run Linux containers. It does this using **WSL 2** (Windows Subsystem for Linux), a lightweight virtualized Linux kernel built into Windows. 
When you run a container, your Windows machine runs it inside this virtualized Linux layer.

---

## 2. Key Terms: Images, Containers, and Docker Hub

* **Image**: A read-only template containing the operating system, file system, installed software, and configurations. Think of it as a **blueprint** or an installer file.
* **Container**: A running, active instance of an image. If the image is a blueprint, the container is the actual house built from that blueprint.
* **Docker Hub** (hub.docker.com): An online public repository (like GitHub is for code, Docker Hub is for container images) where developers can upload and download pre-built images.

---

## 3. Detailed Dockerfile Walkthrough

Here is the line-by-line explanation of your `dockerfile` configuration:

```dockerfile
# 1. Start from an official base image
FROM python:3.10

# 2. Update Linux packages and install the AWS CLI
RUN apt update && apt install awscli -y

# 3. Set the active directory inside the container
WORKDIR /app   

# 4. Copy the requirements file from your local disk into the container
COPY requirements.txt /app/requirements.txt

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the local source code into the container
COPY . /app

# 7. Specify the default command to execute on startup
CMD ["python", "main.py"]
```

### Explanation of Commands:

* **`FROM python:3.10`**: Tells Docker to pull the official Python 3.10 Linux image from Docker Hub to act as the base layer.
* **`RUN apt update && apt install awscli -y`**: Runs Linux commands inside the container during build time to install the AWS CLI (commonly used to download datasets or sync models to AWS S3).
* **`WORKDIR /app`**: Creates and switches to `/app` inside the container. All subsequent commands will execute inside this directory.
* **`COPY requirements.txt /app/requirements.txt`**: Copies the requirements file from Windows into the container's `/app` folder.
* **`RUN pip install --no-cache-dir -r requirements.txt`**: Installs your python packages. The `--no-cache-dir` flag prevents caching download files inside the image, saving VRAM and disk space.
* **`COPY . /app`**: Copies your entire local source code (e.g. `main.py`, `src/`, `config/`) into the container.
* **`CMD ["python", "main.py"]`**: Defines the command that executes when the container starts.

---

## 4. The Docker Cache Optimization Pattern

In the Dockerfile, we copy files in two separate steps:

1. Copy `requirements.txt` $\to$ run `pip install`.
2. Copy the rest of the source code (`COPY . /app`).

### Why do this?
Installing Python dependencies is a slow process (often taking several minutes). Docker builds images in layers and **caches** each layer.
* If we copied the entire folder (`COPY . /app`) **before** running `pip install`, any small code edit on Windows would invalidate the cache. Docker would be forced to download and reinstall all libraries on every single build.
* By copying `requirements.txt` first, Docker checks if it has changed. If not, it skips the `pip install` step entirely and uses the cached layer. When you edit code, Docker only re-executes the fast `COPY . /app` layer, completing your builds in **under a second**.
