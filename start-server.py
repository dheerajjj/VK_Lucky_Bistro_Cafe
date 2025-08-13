#!/usr/bin/env python3
"""
Simple HTTP server for VK Lucky Bistro website
This resolves CORS issues when testing the chatbot widget
"""
import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow API calls
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-API-Key')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def start_server():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print("=" * 60)
        print("🍽️  VK LUCKY BISTRO - CHATBOT TEST SERVER")
        print("=" * 60)
        print(f"✅ Server running at: http://localhost:{PORT}")
        print(f"🤖 Test the chatbot at: http://localhost:{PORT}/index-with-inline-widget.html")
        print(f"🔧 Debug version at: http://localhost:{PORT}/widget-test.html")
        print("📱 The chatbot will work properly from these URLs!")
        print("\n🚀 Opening browser automatically...")
        print("⚡ Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Try to open browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}/index-with-inline-widget.html")
        except Exception as e:
            print(f"Could not auto-open browser: {e}")
            print(f"Please manually open: http://localhost:{PORT}/index-with-inline-widget.html")
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    # Check if we're in the right directory
    if not os.path.exists('index.html'):
        print("❌ Error: Please run this script from the VK Lucky Bistro directory")
        print("Current directory:", os.getcwd())
        sys.exit(1)
    
    start_server()
