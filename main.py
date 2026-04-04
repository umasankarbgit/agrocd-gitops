from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        message = os.getenv(
            "MESSAGE",
            "Hello from ArgoCD running on Kubernetes 🚀"
        )

        return f"""
        <html>
            <head><title>Secure Python App</title></head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1 style="color: black;">{message}</h1>
            </body>
        </html>
        """

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
