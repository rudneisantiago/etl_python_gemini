import os
import requests
import pandas as pd

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_URL = os.getenv("API_URL")
FILE_NAME = "users.csv"
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)


def get_user_ids():
    df = pd.read_csv(FILE_NAME)
    return df["UserId"].tolist()


def get_user(id):
    respose = requests.get(f"{API_URL}/users/{id}")
    return respose.json() if respose.status_code == 200 else None


def update_user(user):
    response = requests.put(f"{API_URL}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


def generate_ai_news(user):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Você é um especialista em marketing bancário"
        ),
        contents=f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres e apenas 1 opção)",
    )
    return response.text


def send_news_to_users():
    users = [user for id in get_user_ids() if (user := get_user(id)) is not None]

    for user in users:
        news = generate_ai_news(user)
        user.setdefault("news", []).append(
            {"description": news, "icon": f"{user['name']}.svg"}
        )
        success = update_user(user=user)
        print(
            f"Usuário {user['name']} {'atualizado com sucesso!' if success else 'não atualizado'}"
        )


def main():
    print(
        """
            #########################################
            ### Iniciando transmissão de notícias ###
            #########################################
        """
    )

    send_news_to_users()

    print(
        """
            #########################################
            ########### Fim da transmissão ##########
            #########################################
        """
    )


main()
