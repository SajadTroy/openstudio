import os
import subprocess
import threading
import socketserver
import http.server
import shutil
import time
import sys
import secrets

RTMP_PORT = 1935
HTTP_PORT = 8888
HLS_DIR = "hls"

STREAM_KEY = secrets.token_hex(8)


def cleanup_hls():
    """Cleans up old HLS segments to start fresh."""
    if os.path.exists(HLS_DIR):
        shutil.rmtree(HLS_DIR)
    os.makedirs(HLS_DIR)


def start_http_server():
    """Starts a simple web server to serve the HLS files."""

    class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            super().end_headers()

    os.chdir(".")

    handler = CORSRequestHandler
    with socketserver.TCPServer(("", HTTP_PORT), handler) as httpd:
        print(f"📡 Broadcast Tower Active: http://0.0.0.0:{HTTP_PORT}")
        httpd.serve_forever()


def start_ffmpeg_listener():
    """Starts FFmpeg in 'Listen Mode' to accept RTMP from OBS."""

    listen_url = f"rtmp://0.0.0.0:{RTMP_PORT}/{STREAM_KEY}"

    cmd = [
        "ffmpeg",
        "-listen",
        "1",
        "-i",
        listen_url,
        "-c",
        "copy",
        "-f",
        "hls",
        "-hls_time",
        "4",
        "-hls_list_size",
        "5",
        "-hls_flags",
        "delete_segments",
        f"{HLS_DIR}/index.m3u8",
    ]

    while True:
        try:
            print("\n" + "=" * 60)
            print(f"🔐 SECURITY ENABLED: New Session Started")
            print(f"👉 STREAM KEY: {STREAM_KEY}")
            print(f"🔴 Configure OBS Server: rtmp://<YOUR_VPS_IP>:{RTMP_PORT}")
            print(f"🔴 Configure OBS Key:    {STREAM_KEY}")
            print("=" * 60 + "\n")

            print("⏳ Waiting for stream connection...")
            subprocess.run(cmd)
            print("⚠️ Stream disconnected. Resetting...")
            time.sleep(2)
        except KeyboardInterrupt:
            break


def main():
    print("🎬 OpenStudio (Python Edition) Starting...")

    cleanup_hls()

    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    try:
        start_ffmpeg_listener()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down OpenStudio.")
        sys.exit(0)


if __name__ == "__main__":
    main()
