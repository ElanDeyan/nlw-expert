from src.main.server.server import app as Server

if __name__ == "__main__":
    Server.run(host="0.0.0.0", port=3000, debug=True)
