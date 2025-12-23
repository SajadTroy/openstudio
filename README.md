# OpenStudio

**Your Personal Broadcast Tower for OpenStream.**

OpenStudio is a lightweight, self-hosted streaming server. It allows you to broadcast from OBS Studio directly to your VPS. It now features **Dynamic Security Keys** to prevent unauthorized access.

## How to Use

1.  **Run the Server:**
    ```bash
    python3 studio.py
    ```

2.  **Get Your Key:**
    The script will generate a new, random security key every time it starts. Look at the console output:

    ```text
    ============================================================
    🔐 SECURITY ENABLED: New Session Started
    👉 STREAM KEY: a1b2c3d4e5f67890
    🔴 Configure OBS Server: rtmp://<YOUR_VPS_IP>:1935
    🔴 Configure OBS Key:    a1b2c3d4e5f67890
    ============================================================
    ```

3.  **Configure OBS:**
    * **Service:** Custom
    * **Server:** `rtmp://<YOUR_VPS_IP>:1935`
    * **Stream Key:** Copy the `STREAM KEY` from the console.

4.  **Start Streaming:**
    Once connected, your public HLS link remains the same:
    ```
    http://<YOUR_VPS_IP>:8888/hls/index.m3u8
    ```
    *(You can share this public link with OpenStream; it doesn't change even if your security key does).*