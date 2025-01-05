import os

"""
This script is designed to install and configure Cloudflared on a Linux system and run a Flask application.

Functions:
    install_cloudflared() -> str:
        Downloads and installs the Cloudflared binary for Linux.
        Returns the name of the installed binary.

    configure_tunnel(token: str, binary_name: str):
        Configures the Cloudflared tunnel using the provided token and binary name.

Main Execution:
    If the script is run as the main module, it attempts to load environment variables,
    retrieve the Cloudflared token, install Cloudflared, and configure the tunnel.
    If the platform is not Linux or the token is not found, it runs the Flask application.
"""

# import platform

# from dotenv import load_dotenv

# import subprocess
# def install_cloudflared() -> str:

#     os_name = platform.system().lower()
#     print("Detectado Linux.")
#     url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb"
#     install_command = "apt install ./cloudflared-linux-amd64.deb"
#     binary_name = "cloudflared"

#     print(f"Baixando o Cloudflared para {os_name}...")
#     subprocess.run(["curl", "-L", url, "-o", "cloudflared-linux-amd64.deb"])

#     print(f"Instalando o Cloudflared para {os_name}...")
#     subprocess.run(install_command, shell=True)

#     print("Cloudflared instalado com sucesso.")
#     return binary_name


# def configure_tunnel(token: str, binary_name: str):

#     print("Configurando o Cloudflared Tunnel...")

#     try:
#         subprocess.run([f"{binary_name}", "service", "uninstall"])
#     except Exception as e:
#         raise e

#     subprocess.run([f"{binary_name}", "service", "install", token])


if __name__ == "__main__":

    # if platform.system() == "Linux":
    #     load_dotenv()
    #     token: str = os.getenv("CLOUDFLARED_TOKEN")

    #     if token:
    #         configure_tunnel(token, install_cloudflared())

    #     else:
    #         print(
    #             "Token não encontrado. Verifique se o arquivo .env está configurado corretamente."
    #         )

    from app import app

    debug = os.getenv("DEBUG", "False").lower() in ("true", "1", "t", "y", "yes")

    app.run(6003, debug)
