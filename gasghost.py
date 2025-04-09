import requests
import time
from config import ETHERSCAN_API_KEY, GAS_THRESHOLD_GWEI, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def get_gas_price():
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    return int(response['result']['ProposeGasPrice'])

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def main():
    print("🟢 GasWatchdog запущен...")
    while True:
        try:
            gas_price = get_gas_price()
            print(f"⛽️ Текущий газ: {gas_price} Gwei")
            if gas_price >= GAS_THRESHOLD_GWEI:
                send_telegram_alert(f"⚠️ Высокий GAS: {gas_price} Gwei! Проверь сеть.")
        except Exception as e:
            print("❌ Ошибка:", e)
        time.sleep(30)  # каждые 30 секунд

if __name__ == "__main__":
    main()
