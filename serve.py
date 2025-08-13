#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌐 VK Lucky Bistro website is now running!")
        print(f"📍 Open in browser: http://localhost:{PORT}")
        print(f"🤖 The AI chatbot should appear in the bottom-right corner")
        print(f"⚡ Press Ctrl+C to stop the server")
        
        # Try to open browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except:
            pass
            
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
