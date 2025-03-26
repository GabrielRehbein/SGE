import requests
from decouple import config


class CallMeBotService:
    def __init__(self):
        self.__api_url = "https://api.callmebot.com/whatsapp.php"
        self.__api_key = config('CALL_ME_BOT_API_KEY')
        self.__phone = "+555190083958"

    def send_message(self, text):
        try:
            full_url = f"{self.__api_url}?phone={self.__phone}&text={text}&apikey={self.__api_key}"
            print(f"URL gerada: {full_url}")
            response = requests.get(full_url)
            print(response.content)
            if response.status_code == 200:
                return True, "Mensagem enviada com sucesso!"
            else:
                return False, f"Erro ao enviar a mensagem: {response.text}"
        except requests.exceptions.RequestException as e:
            return False, f"Erro na requisição: {str(e)}"

        
if __name__ == '__main__':
    print("API Key:", config('CALL_ME_BOT_API_KEY'))
    c = CallMeBotService()
    c.send_message('fad')