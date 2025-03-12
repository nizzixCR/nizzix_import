#Copyright (c) 2012-2024 Scott Chacon and others

#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
An import for an EasyLife 

\ngithub : https://github.com/nizzixCR/nizzix_import
\ncreator : nizzix_cr
'''

from disc import vp_discord
from disc import tool_discord
from temp_mail import temp_1secmail
from install_py import python_install
from anti_debug import AntiDbg
from temp_org import TempMail
from aimlapi import talk_ai

def clear():
    import os
    '''clear the terminal'''
    os.system("cls")

def command(command):
    import os 
    '''execute an commande in the terminal'''
    os.system(command)

def getuser():
    import os
    '''For have the name of the user'''
    return os.getlogin()

def getpcname():
    import socket
    '''For have the name of the PC'''
    return socket.gethostname()

def sizecmd():
    import os
    '''For have the Terminal Size'''
    return os.get_terminal_size()

def startpath(path):
    import os
    '''For launch an Path'''
    return os.startfile(path)

def current_path():
    import os
    '''For obtain the current directiory'''
    return os.path.dirname(os.path.abspath(__file__))

def current_path_file():
    import os
    '''For obtain the current file'''
    return os.path.abspath(__file__)

def open_a_path(path):
    import subprocess
    '''Open a PATH in a new Window'''
    return subprocess.Popen(path)

def delete(path):
    import os
    '''For Delete an path'''
    return os.remove(path)

def errormsg(error_text):
    import ctypes
    '''For display an Error messagebox'''
    return ctypes.windll.user32.MessageBoxW(0, f"{error_text}", "Error", 1)

def msgbox(text, title):
    import ctypes
    '''For display an personalized MsgBox With title and texte personalize'''
    return ctypes.windll.user32.MessageBoxW(0, f"{text}", f"{title}", 1)

def warningmsg(Warning_texte):
    import ctypes
    '''For display an warning MsgBox'''
    return ctypes.windll.user32.MessageBoxW(0, f"{Warning_texte}", "Warning", 0)

def open_link(link):
    import webbrowser
    '''For open an link in a browser'''
    return webbrowser.open(link)

def get_external_ipv4():
    import requests
    '''For obtain the external IPv4'''
    response = requests.get('https://api.ipify.org').text
    return response

def get_uuid():
    import uuid
    from uuid import uuid4
    '''Obtain the UUID'''
    return uuid.uuid4()

def getallmac():
    import subprocess
    '''Get all mac adress'''
    result = subprocess.check_output(['getmac']).decode('cp1252')
    return result 

def resize_grid(cols,lines):
    import os 
    '''Resize the terminal'''
    os.system(f"mode con: cols={cols} lines={lines}")

def check_hwid():
    import subprocess

    def run_command(command):
        """Exécute une commande et retourne la sortie sous forme de chaîne."""
        try:
            result = subprocess.check_output(command, shell=True, universal_newlines=True)
            return result.strip()
        except subprocess.CalledProcessError:
            return "N/A"

    hwid_info = {
        "Disk Drive Model and Serial Number": run_command('wmic diskdrive get model, serialnumber'),
        "Disk Drive Serial Number": run_command('wmic diskdrive get serialnumber'),
        "CPU Processor ID": run_command('wmic cpu get processorid'),
        "BIOS Serial Number": run_command('wmic bios get serialnumber'),
        "Motherboard Serial Number": run_command('wmic baseboard get serialnumber'),
        "SMBIOS UUID": run_command('wmic csproduct get uuid'),
        "MAC Address": run_command('getmac'),
    }

    return hwid_info

def antivm():
    import os
    import platform
    import uuid
    import psutil 
    import subprocess
    
    def check_files_on_desktop(file_names):
        desktop_path = os.path.expanduser("~/Desktop")
        for file_name in file_names:
            file_path = os.path.join(desktop_path, file_name)
            if os.path.exists(file_path):
                return True
        return False

    def check_windows_mode():
        return platform.system() == "MS-DOS"

    def is_allowed_user():
        allowed_names = ["george", "abby", "WDAGUtilityAccount", "A1vHxfPNYE", "dburns", "a6VtQdc"]
        return os.getlogin().lower() in (name.lower() for name in allowed_names)

    def has_invalid_uuid():
        uuid_value = uuid.uuid4()
        return str(uuid_value) == '00000000-0000-0000-0000-000000000000'

    def check_low_memory():
        total_memory = psutil.virtual_memory().total
        return total_memory < 2 * 1024 * 1024 * 1024

    def check_suspicious_processes():
        suspicious_processes = [
            "vboxservice.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe",
            "vmwareuser.exe", "qemu-ga.exe", "xenservice.exe"
        ]
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() in suspicious_processes:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False

    def check_suspicious_drivers():
        suspicious_drivers = ["VBoxGuest", "VBoxSF", "VBoxVideo", "vmhgfs", "vmmemctl"]
        try:
            output = subprocess.check_output("driverquery", shell=True, text=True)
            for driver in suspicious_drivers:
                if driver.lower() in output.lower():
                    return True
        except Exception:
            pass
        return False

    def check_vm_filesystems():
        vm_filesystems = ["vbox", "vmware", "qemu", "xen"]
        try:
            for part in psutil.disk_partitions():
                if any(fs in part.device.lower() for fs in vm_filesystems):
                    return True
        except Exception:
            pass
        return False

    def check_cpu_count():
        cpu_count = os.cpu_count()
        return cpu_count is not None and cpu_count <= 2

    def check_network_adapter():
        vm_mac_prefixes = [
            "00:05:69", "00:0C:29", "00:1C:14", "00:50:56", 
            "08:00:27", 
            "52:54:00"  
        ]
        try:
            for interface, addrs in psutil.net_if_addrs().items():
                for addr in addrs:
                    if addr.family == psutil.AF_LINK:
                        mac = addr.address.lower()
                        if any(mac.startswith(prefix) for prefix in vm_mac_prefixes):
                            return True
        except Exception:
            pass
        return False

    files_to_check = [
        "report.doc", "keys.txt", "invoice.doc", "report",
        "Financial_Report.ppt", "account.xlsx", "passwords.txt"
    ]

    if (
        check_files_on_desktop(files_to_check) or
        check_windows_mode() or
        is_allowed_user() or
        has_invalid_uuid() or
        check_low_memory() or
        check_suspicious_processes() or
        check_suspicious_drivers() or
        check_vm_filesystems() or
        check_cpu_count() or
        check_network_adapter()
    ):
        return True
    return False  

def get_hardware_info():
    import subprocess
    import wmi
    import platform

    '''Obtain your Hardware Information'''

    def get_windows_edition():
        try:
            command = 'wmic os get Caption /value'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            
            if output:
                windows_edition = output.decode('utf-8').strip().split('=')[1]
                return windows_edition
            else:
                return "Edition information not found"
        except Exception as e:
            return f"Error retrieving Windows edition: {str(e)}"

    def get_memory_info():
        try:
            command = 'wmic MEMORYCHIP get Capacity,Manufacturer,Speed /format:csv'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            memory_info = []
            
            if output:
                lines = output.decode('utf-8').strip().split('\n')[1:]  
                for line in lines:
                    if line:
                        parts = line.split(',')
                        memory_info.append({
                            'Manufacturer': parts[1],
                            'Capacity': int(parts[2]) // (1024**3),
                            'Speed': parts[3]
                        })
            return memory_info
        except Exception as e:
            return f"Error retrieving memory info: {str(e)}"

    def get_disk_info():
        try:
            command = 'wmic diskdrive get Model,Size /format:csv'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            disk_info = []
            
            if output:
                lines = output.decode('utf-8').strip().split('\n')[1:]
                for line in lines:
                    if line:
                        parts = line.split(',')
                        disk_info.append({
                            'Model': parts[1],
                            'Size (GB)': int(parts[2]) // (1024**3)
                        })
            return disk_info
        except Exception as e:
            return f"Error retrieving disk info: {str(e)}"

    c = wmi.WMI()

    gpu_info = []
    try:
        for gpu in c.Win32_VideoController():
            gpu_info.append({
                'Name': gpu.Name,
                'AdapterRAM': int(gpu.AdapterRAM) // (1024**2) if gpu.AdapterRAM else None, 
                'DriverVersion': gpu.DriverVersion
            })
    except Exception as e:
        gpu_info.append({'Error': str(e)})

    processor_info = []
    try:
        for processor in c.Win32_Processor():
            processor_info.append({
                'Name': processor.Name,
                'Cores': processor.NumberOfCores,
                'MaxClockSpeed (MHz)': processor.MaxClockSpeed,
                'Manufacturer': processor.Manufacturer
            })
    except Exception as e:
        processor_info.append({'Error': str(e)})

    os_info = {
        'System': platform.system(),
        'Node': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Architecture': platform.architecture()[0],
        'WindowsEdition': get_windows_edition()
    }

    hardware_info = {
        'OS Information': os_info,
        'Processor Information': processor_info,
        'Graphics Card Information': gpu_info,
        'Memory Information': get_memory_info(),
        'Disk Information': get_disk_info()
    }

    return hardware_info

def encrypt_64(text):
    import base64
    """Encode the bytes-like object s using Base64 and return a bytes object.

    Optional altchars should be a byte string of length 2 which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    """
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encrypted_text = encoded_bytes.decode('utf-8')
    return encrypted_text

def decrypt_64(encoded_text):
    import base64
    """Decode the Base64 encoded bytes-like object or ASCII string s.

    Optional altchars must be a bytes-like object or ASCII string of length 2
    which specifies the alternative alphabet used instead of the '+' and '/'
    characters.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded.

    If validate is False (the default), characters that are neither in the
    normal base-64 alphabet nor the alternative alphabet are discarded prior
    to the padding check.  If validate is True, these non-alphabet characters
    in the input result in a binascii.Error.
    For more information about the strict base64 check, see:

    https://docs.python.org/3.11/library/binascii.html#binascii.a2b_base64
    """
    decoded_bytes = base64.b64decode(encoded_text)
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

def encrypt_32(text):
    import base64
    """Encode the bytes-like object s using Base32 and return a bytes object.

    Optional altchars should be a byte string of length 2 which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    """
    encoded_bytes = base64.b32encode(text.encode())
    encoded_string = encoded_bytes.decode()
    return encoded_string

def decrypt_32(encoded_text):
    import base64
    """Decode the Base32 encoded bytes-like object or ASCII string s.

    Optional altchars must be a bytes-like object or ASCII string of length 2
    which specifies the alternative alphabet used instead of the '+' and '/'
    characters.

    The result is returned as a bytes object.  A binascii.Error is raised if
    s is incorrectly padded.

    If validate is False (the default), characters that are neither in the
    normal Base-32 alphabet nor the alternative alphabet are discarded prior
    to the padding check.  If validate is True, these non-alphabet characters
    in the input result in a binascii.Error.
    For more information about the strict base64 check, see:

    https://docs.python.org/3.11/library/binascii.html#binascii.a2b_base64
    """
    decoded_bytes = base64.b32decode(encoded_text)
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

def encrypt_caesar_shift(text, a_key):
    '''Encrypt using Caesar cipher-like shift'''
    encrypted_message = ""
    for char in text:
        encrypted_char = chr((ord(char) + a_key) % 256)
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_caesar_shift(text, a_key):
    '''Decrypt using Caesar cipher-like shift'''
    decrypted_message = ""
    for char in text:
        decrypted_char = chr((ord(char) - a_key) % 256)
        decrypted_message += decrypted_char
    return decrypted_message

def generate_random_password(numbers_characters):
    import string
    import random
    '''Generate an random password'''
    characters = string.ascii_letters + string.digits + '@'
    password = ''.join(random.choice(characters) for i in range(numbers_characters))
    return password

def ip2geo(ip_address, type=1, api='ip-api'):
    import requests
    '''For retrieving geolocation information of an IP address from multiple APIs.'''
    
    # Define available APIs and their URL formats
    apis = {
        'ip-api': f'http://ip-api.com/json/{ip_address}',
        'ipinfo': f'https://ipinfo.io/{ip_address}/json',
        'ipstack': f'http://api.ipstack.com/{ip_address}?access_key=YOUR_API_KEY',
        'geoip2': f'https://geoip.maxmind.com/geoip/v2.1/city/{ip_address}',
        'ip-geolocation': f'https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip_address}',
        'db-ip': f'https://api.db-ip.com/v2/free/{ip_address}'
    }
    
    if api not in apis:
        return {'error': 'Invalid API. Choose from: ip-api, ipinfo, ipstack, geoip2, ip-geolocation, db-ip.'}
    
    url = apis[api]
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if 'error' in data or ('status' in data and data['status'] == 'fail'):
            return {'error': 'Failed to retrieve geolocation information.'}
        
        if type == 1:
            return {'country': data.get('country', 'N/A')}
        elif type == 2:
            return {'country': data.get('country', 'N/A'), 'region': data.get('region', 'N/A')}
        elif type == 3:
            return {'country': data.get('country', 'N/A'), 'region': data.get('region', 'N/A'), 'city': data.get('city', 'N/A')}
        elif type == 4:
            return {'country': data.get('country', 'N/A'), 'region': data.get('region', 'N/A'), 'city': data.get('city', 'N/A'), 'zip': data.get('zip', 'N/A')}
        elif type == 5:
            return {'country': data.get('country', 'N/A'), 'region': data.get('region', 'N/A'), 'city': data.get('city', 'N/A'), 
                    'zip': data.get('zip', 'N/A'), 'latitude': data.get('latitude', 'N/A'), 'longitude': data.get('longitude', 'N/A')}
        elif type == 6:
            return {'country': data.get('country', 'N/A'), 'region': data.get('region', 'N/A'), 'city': data.get('city', 'N/A'), 
                    'zip': data.get('zip', 'N/A'), 'latitude': data.get('latitude', 'N/A'), 'longitude': data.get('longitude', 'N/A'), 
                    'isp': data.get('isp', 'N/A'), 'org': data.get('org', 'N/A')}
        else:
            return {'error': 'Invalid type parameter. Please choose between 1 and 6.'}
    else:
        return {'error': 'Failed to retrieve IP information.'}

def precise_date(type=1):
    import datetime
    '''For getting the precise date with different format types.'''
    
    date = datetime.datetime.now()

    if type == 1:
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S.%f")
    elif type == 2:
        formatted_date = date.strftime("%d/%m/%Y")  
    elif type == 3:
        formatted_date = date.strftime("%H:%M:%S")
    elif type == 4:
        formatted_date = date.strftime("%Y-%m-%d") 
    elif type == 5:
        formatted_date = date.strftime("%d-%m-%Y %H:%M") 
    else:
        return {'error': 'Invalid type. Choose from 1 to 5.'}
    
    return formatted_date, date

def proxies_scrape(type="http", limit=None):
    import requests
    '''For getting free proxies with an optional limit on the number of proxies returned'''
    
    proxy_urls = {
        "http": [
            "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/proxyscrape_premium_http_proxies.txt",
            "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/proxies.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/http.txt",
            "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
            "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt"
        ],
        "https": [
            "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/http_proxies.txt",
            "https://www.proxy-list.download/api/v1/get?type=https",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/https.txt",
            "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
            "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt"
        ],
        "socks4": [
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks4/socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/socks4.txt",
            "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
            "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
            "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/socks4_proxies.txt"
        ],
        "socks5": [
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks5/socks5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/socks5.txt",
            "https://raw.githubusercontent.com/themiralay/Proxy-List-World/refs/heads/master/data.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/Proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/xResults/old-data/Proxies.txt",
            "https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/refs/heads/main/proxies.txt",
            "https://raw.githubusercontent.com/yashing2/proxy/refs/heads/main/socks5_proxies.txt"
        ]
    }

    urls = proxy_urls.get(type, [])

    proxies = []

    for url in urls:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                rformat = r.text.strip()
                rformat = rformat.replace("\r", "")
                rlist = list(rformat.split("\n"))
                proxies.extend(rlist)
                
                if limit and len(proxies) >= limit:
                    proxies = proxies[:limit]
                    break
        except requests.exceptions.RequestException as e:
            pass

    if limit:
        proxies = proxies[:limit]

    return proxies

def check_proxy(proxy_ip_port, timeout=3, test_url="https://www.google.com"):
    import requests
    from requests.exceptions import Timeout, RequestException
    proxy_types = ["http", "https", "socks4", "socks5"]

    for proxy_type in proxy_types:
        proxy_url = f"{proxy_type}://{proxy_ip_port}"
        
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        try:
            response = requests.get(test_url, proxies=proxies, timeout=timeout)
            
            if response.status_code == 200:
                return True
        except (Timeout, RequestException) as e:
            pass

    return False 

def title(new_title):  
    import os
    '''For change the title of the page'''
    os.system(f"title {new_title}")

class Key:
    def __init__(self, key_value):
        self.key_value = key_value

    def check_key(self, keyauthapp):
        '''Checks if the provided key is valid. Returns True if valid, False otherwise.'''
        try:
            result = keyauthapp.license(self.key_value)
            return result == 'valid'
        except Exception as e:
            print(f"Error checking key: {e}")
            return False


def check_key(keyauthapp, key_value):
    '''Checks if the provided key is valid. Returns True if valid, False otherwise.'''
    try:
        result = keyauthapp.license(key_value)
        return result == 'valid' 
    except Exception as e:
        print(f"Error checking key: {e}")
        return False


def keyauth_connexion(Name, Ownerid, version="1.0"):
    import sys 
    import hashlib
    from .keyauth import api

    '''For creating a KeyAuth connection interface'''

    def getchecksum():
        md5_hash = hashlib.md5()
        with open(''.join(sys.argv), "rb") as file:
            md5_hash.update(file.read())
        digest = md5_hash.hexdigest()
        return digest

    return api(
        name=Name,
        ownerid=Ownerid,
        version=version,
        hash_to_check=getchecksum()
    )

def scan_url(api_key, url_to_scan):
    import requests
    
    '''This is for scanning a URL with VirusTotal but you need a VirusTotal API Key.
       Usage:
       scan_url('your_api_key', 'url_to_scan')
    '''
    def scan(url):
        url_scan = 'https://www.virustotal.com/vtapi/v2/url/scan'
        params = {'apikey': api_key, 'url': url}
        response_scan = requests.post(url_scan, data=params)
        scan_id = response_scan.json()['scan_id']
        return scan_id

    def report(scan_id):
        url_report = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': api_key, 'resource': scan_id}
        response_report = requests.get(url_report, params=params)
        return response_report.json()

    def main():
        scan_id = scan(url_to_scan)
        report_results = report(scan_id)

        result = {}

        result["scan_id"] = scan_id
        result["scan_date"] = report_results.get('scan_date')
        result["positives"] = report_results.get('positives')

        most_detected_virus = max(report_results.get('scans'), key=lambda x: report_results.get('scans')[x].get('detected', 0))
        most_detected_virus_name = most_detected_virus
        most_detected_antivirus = report_results.get('scans')[most_detected_virus]['result']

        ignore_results = ['clean site', 'unrated site']

        if most_detected_antivirus.lower() not in ignore_results:
            result["most_detected_virus"] = most_detected_antivirus
            result["most_detected_antivirus"] = most_detected_virus_name

        all_detected_viruses = []
        for engine, result_item in report_results.get('scans').items():
            if result_item.get('result').lower() not in ignore_results:
                all_detected_viruses.append({
                    "virus": result_item.get('result'),
                    "antivirus": engine
                })

        result["all_detected_viruses"] = all_detected_viruses

        if report_results.get('positives') > 5:
            result["url_scan_status"] = "high"
        elif report_results.get('positives') > 0:
            result["url_scan_status"] = "medium"
        else:
            result["url_scan_status"] = "clean"

        result["url"] = report_results.get('url')
        result["verbose_msg"] = report_results.get('verbose_msg')

        return result

    return main()

def scan_file(api_key, file_path):
    import requests
    
    '''This is for scanning a file with VirusTotal but you need a VirusTotal API Key
       Usage:
       scan_file('your_api_key', 'file_path_to_scan')
    '''
    def scan_file(file_path):
        url_scan = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': api_key}
        files = {'file': (file_path, open(file_path, 'rb'))}
        response_scan = requests.post(url_scan, files=files, params=params)
        scan_id = response_scan.json()['scan_id']
        return scan_id

    def report_file(scan_id):
        url_report = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': api_key, 'resource': scan_id}
        response_report = requests.get(url_report, params=params)
        return response_report.json()

    def main():
        scan_id = scan_file(file_path)
        report_results = report_file(scan_id)

        result = {
            "scan_id": scan_id,
            "scan_date": report_results.get('scan_date'),
            "positives": report_results.get('positives')
        }

        most_detected_virus = max(report_results.get('scans'), key=lambda x: report_results.get('scans')[x].get('detected', 0))
        most_detected_virus_name = most_detected_virus
        most_detected_antivirus = report_results.get('scans')[most_detected_virus]['result']

        ignore_results = ['clean site', 'unrated site']

        if most_detected_antivirus.lower() not in ignore_results:
            result["most_detected_virus"] = most_detected_antivirus
            result["most_detected_antivirus"] = most_detected_virus_name

        all_detected_viruses = []
        for engine, result_item in report_results.get('scans').items():
            if result_item.get('result').lower() not in ignore_results:
                all_detected_viruses.append({
                    "virus": result_item.get('result'),
                    "antivirus": engine
                })

        result["all_detected_viruses"] = all_detected_viruses

        if report_results.get('positives') > 5:
            result["file_scan_status"] = "dangerous"
        elif report_results.get('positives') > 0:
            result["file_scan_status"] = "not dangerous"
        else:
            result["file_scan_status"] = "safe"

        result["file_path"] = file_path
        result["verbose_msg"] = report_results.get('verbose_msg')

        return result

    return main()

def search_virustotal(api_key, resource_type, entry):
    import requests
    
    '''This is for searching on VirusTotal using the search API
       Usage:
       search_virustotal(api_key, resource_type='url', entry='example.com')
       search_virustotal(api_key, 'ip_address', '192.168.1.1')
       search_virustotal(api_key, 'domain', 'example.com')
       search_virustotal(api_key, 'hash', 'abcdef1234567890')
    '''
    def search(resource_type, entry):
        url_search = 'https://www.virustotal.com/vtapi/v2/search'
        params = {'apikey': api_key, 'query': entry, 'resource': resource_type}
        response_search = requests.get(url_search, params=params)
        return response_search.json()

    def main():
        search_results = search(resource_type, entry)

        result = {}

        if search_results.get('response_code') == 1:
            result["search_results"] = []
            for result_item in search_results.get('results'):
                result["search_results"].append({
                    "type": result_item.get('type'),
                    "resource": result_item.get('id'),
                    "score": result_item.get('reputation'),
                    "last_analysis_date": result_item.get('last_analysis_date')
                })
        else:
            result["error"] = f"No results found for: {entry}"

        return result

    return main()

def change_paper(image_path):
    import ctypes
    '''Change your wallpaper with an image path'''
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        return 'Wallpaper changed successfully!'
    except Exception as e:
        return str(e)
    
def check_file(file_path):
    '''Check if a file exists with the given path'''
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False

def speech(text):
    import pyttsx3
    '''Speech a text'''
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def active_windows():
    import os
    
    kms_key_mapping = {
        "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
        "3KHY7-WNT83-DGQKR-F7HPR-844BM": "3KHY7-WNT83-DGQKR-F7HPR-844BM",
        "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
        "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR": "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR",
        "W269N-WFGWX-YVC9B-4J6C9-T83GX": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
        "MH37W-N47XK-V7XM9-C7227-GCQG9": "MH37W-N47XK-V7XM9-C7227-GCQG9",
        "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
        "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
        "NPPR9-FWDCX-D2C8J-H872K-2YT43": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
        "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4" 
    }

    current_version = os.popen("slmgr /dli").read()

    if current_version.strip() in kms_key_mapping:
        os.system(f"slmgr /ipk {kms_key_mapping[current_version.strip()]}")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

def restart(time):
    import os 
    '''Permet you to restart pc '''
    os.system(f"shutdown /r /t {time}")

def shutdown(time):
    import os
    '''Permet you to shutdown pc'''
    os.system(f"shutdown /s /t {time}")

def cpu_core():
    import os
    return os.cpu_count()

def close(file_path):
    import os
    file_descriptor = os.open(file_path, os.O_RDWR)

    os.close(file_descriptor)

def kill(pid):
    import os
    import signal
    os.kill(pid, signal.SIGKILL)