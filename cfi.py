import requests

import datetime
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)


def print_welcome_message():
    print(r"""
          
█     █ █  █ ▄▄▄▄▄ █  █ ▄▄▄▄▄
█ ▀ ▀ █ █  █ █ ▄▄█ █  █ █▄▄▄█
█  ▀  █ █▄▄█ █  ▄  █▄▄█ █
          """)
    print(Fore.GREEN + Style.BRIGHT + "Cyberfinance BOT")
    print(Fore.GREEN + Style.BRIGHT + "Update Link: https://github.com/frisca30/")
    print(Fore.YELLOW + Style.BRIGHT + "Free Konsultasi Join Discord: https://discord.gg/ikuzodao")
    print(Fore.BLUE + Style.BRIGHT + "Belikan saya kopi :) 0881 0260 1020 05 DANA")
    print(Fore.RED + Style.BRIGHT + "gausah mbok jual ! Ngotak dikit bos. Ngoding susah2 kau tinggal rename :)\n\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def read_tokens():
    with open('tokens.txt', 'r') as file:
        return [line.strip() for line in file if line.strip()]

def info_balance(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    crack_time = data['message']['miningData']['crackTime']
    now = datetime.datetime.now().timestamp()
    countdown = crack_time - now
    hours, remainder = divmod(countdown, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{Fore.BLUE+Style.BRIGHT}[Balance]:", f"{Fore.BLUE+Style.BRIGHT}{data['message']['userData']['balance']} |", f"{Fore.BLUE+Style.BRIGHT}{int(hours):02} Jam {int(minutes):02} Menit", f"{Fore.BLUE+Style.BRIGHT}lagi untuk claim")

def claim_mining(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/claim"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(f"{Fore.YELLOW+Style.BRIGHT}[Claim]: {data['message']}")

def auto_upgrade_hammer(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"HAMMER"}'
    while True:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            sys.stdout.write(f"{Fore.RED+Style.BRIGHT}[Saldo Tidak Cukup]\n")
            break
        response_data = response.json()
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[Sukses Upgrade] Hammer Level: {response_data['message']['boostData']['hammerLevel']}")

def auto_upgrade_egg(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"EGG"}'
    while True:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            sys.stdout.write(f"{Fore.RED+Style.BRIGHT}[Saldo Tidak Cukup]\n")
            break
        response_data = response.json()
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[Sukses Upgrade] Egg Level: {response_data['message']['boostData']['eggLevel']}")

def fetch_uuids(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/gametask/all"
    headers = {
        'Authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tasks = response.json()['message']
        return [task['uuid'] for task in tasks if not task['isCompleted']]
    else:
        print("Failed to fetch tasks")
        return []

def complete_tasks(uuids, ini_token):
    base_url = "https://api.cyberfin.xyz/api/v1/gametask/complete/"
    headers = {
        'Authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'Content-Type': 'application/json'
    }
    for uuid in uuids:
        response = requests.patch(f"{base_url}{uuid}", headers=headers)
        response_data = response.json()
        if response.status_code == 200:    
            print(f"{Fore.GREEN+Style.BRIGHT}[Sukses] | {uuid} completed successfully.")
        else:
            print(f"{Fore.RED+Style.BRIGHT}[Gagal] | {uuid} | {response_data['message']}")

def user_level(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/info"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  # Menggunakan token yang dibaca
        'dnt': '1',
        'if-none-match': 'W/"a4-LZ8zXP3aEql/rLf1iujkfLlL6Tk"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['message']
        print(f"{Fore.BLUE+Style.BRIGHT}[Egg Level]: {data['eggLevel']}")
        print(f"{Fore.BLUE+Style.BRIGHT}[Hammer Level]: {data['hammerLevel']}")
    else:
        print(f"{Fore.RED+Style.BRIGHT}[Gagal mendapatkan informasi level pengguna]")

def main():
    print_welcome_message()
    user_input_task = input("Auto cleartask ? (y / n) : ")
    user_input_hammer = input("Auto upgrade hammer ( Cracking Power ) ? (y / n) : ")
    user_input_egg = input("Auto upgrade egg ( Jam per Claim ) ? (y / n) : ")
    clear_console()
    while True:
        print_welcome_message()
        tokens = read_tokens()  # Membaca semua token dari file
        for index, ini_token in enumerate(tokens):
            # Proses setiap token
            #print(f"Memproses akun ke {index + 1}: {ini_token}")  # Menampilkan nomor akun berdasarkan urutan di tokens.txt
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Akun ke-{index + 1} ] ==============")  # Mencetak nama
            if user_input_task.lower() == 'y':
                uuids = fetch_uuids(ini_token)
                complete_tasks(uuids, ini_token)
            if user_input_hammer.lower() == 'y':
                auto_upgrade_hammer(ini_token)
            if user_input_egg.lower() == 'y':
                auto_upgrade_egg(ini_token)
            user_level(ini_token)
            info_balance(ini_token)
            claim_mining(ini_token)
        for i in range(3600, 0, -1):
            sys.stdout.write(f"\r{Fore.CYAN+Style.BRIGHT}============ Selesai, tunggu {i} detik.. ============")
            sys.stdout.flush()
            time.sleep(1)
        print()  # Cetak baris baru setelah hitungan mundur selesai

        # Membersihkan konsol setelah hitungan mundur
        clear_console()
        time.sleep(5)  # Delay 5 detik sebelum memulai lagi

if __name__ == "__main__":
    main()
