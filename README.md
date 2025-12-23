# OpenStudio

<p align="center">
  <img src="files/openstudio.jpg" width="100%" alt="OpenStudio Banner">
</p>

**Your Personal Broadcast Tower for OpenStream.**

OpenStudio is a lightweight, self-hosted streaming server. It allows you to broadcast from OBS Studio directly to your VPS.

## How to Use

1.  **Run the Server:**
    ```bash
    python3 main.py
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

3.  **Configure Streamin Software:**
    * **Service:** Custom
    * **Server:** `rtmp://<YOUR_VPS_IP>:1935`
    * **Stream Key:** Copy the `STREAM KEY` from the console.

4.  **Start Streaming:**
    Once connected, your public HLS link remains the same:
    ```
    http://<YOUR_VPS_IP>:8888/hls/index.m3u8
    ```
    *(You can share this public link with OpenStream; it doesn't change even if your security key does).*

## ✅ Add to OpenStream

Now that your station is live, add it to the global OpenStream playlist so others can watch it!

1.  **Verify your link:** Open `http://<YOUR_VPS_IP>:8888/hls/index.m3u8` in VLC Player to make sure it works.
2.  **Go to the OpenStream Repository:** [SajadTroy/openstream](https://github.com/SajadTroy/openstream)
3.  **Fork** the repository and browse to the `streams/` folder.
4.  **Edit** the `community.m3u` file.
5.  **Append your channel** to the bottom of the file using this format:

    ```text
    #EXTINF:-1 group-title="Your Category" tvg-logo="[https://example.com/logo.png](https://example.com/logo.png)", Your Channel Name
    http://<YOUR_VPS_IP>:8888/hls/index.m3u8
    ```

6.  **Submit a Pull Request (PR).**
    * Once merged, the OpenStream bot will test your link.
    * If it is accessible, it will appear in the main playlist within 24 hours.

> **Note:** Ensure your VPS firewall allows traffic on port **8888** so the OpenStream validator can check your link.