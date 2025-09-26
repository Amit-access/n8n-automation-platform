# Use official n8n image as the base
# (you can pin a specific version, e.g. n8nio/n8n:1.64.0 for stability)
FROM n8nio/n8n:latest

# Optional: set a default timezone (override via env in compose)
ENV GENERIC_TIMEZONE=Asia/Kolkata

# If later you add custom nodes and need build tools, you can enable:
# USER root
# RUN apk add --no-cache python3 make g++
# USER node

# n8n uses /home/node/.n8n as data dir by default.
# We won't copy anything here; workflows & data will be mounted as a volume.
WORKDIR /home/node/.n8n

# CMD comes from the base image; nothing else required here.

