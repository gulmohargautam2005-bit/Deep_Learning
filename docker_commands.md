# Docker Container & Image Management Reference

This document serves as a quick reference guide for managing Docker containers, images, and troubleshooting deployments on the EC2 self-hosted runner.

---

## 1. Inspecting Containers

### List Running Containers
```bash
docker ps
```

### List All Containers (Running and Stopped)
```bash
docker ps -a
```

### Check Current Directory inside a Running Container
```bash
docker exec -it cnncls pwd
```

### List Files inside a Running Container
```bash
docker exec -it cnncls ls -la
```

---

## 2. Inspecting Logs

### Check Container Output Logs (Troubleshooting Startup Crashes)
```bash
docker logs cnncls
```
*Use this command if the container exits immediately after running to view the Python/Flask error stack trace.*

---

## 3. Cleaning Up Containers & Images

### Stop All Containers
```bash
docker stop $(docker ps -a -q)
```

### Delete All Containers
```bash
docker rm $(docker ps -a -q)
```

### List All Installed Images
```bash
docker images
```

### Delete All Installed Images
```bash
docker rmi $(docker images -q) -f
```

### Deep Clean (Remove All Stopped Containers, Unused Images, and Build Cache)
```bash
docker system prune -a -f
```
