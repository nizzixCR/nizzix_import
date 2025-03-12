import platform
import win32security
import os
import subprocess

class others:
    import platform
    import win32security
    import os
    import subprocess
    
    @staticmethod
    def get_hwid():
        if platform.system() == "Linux":
            with open("/etc/machine-id") as f:
                hwid = f.read()
                return hwid
        elif platform.system() == 'Windows':
            winuser = os.getlogin()
            sid = win32security.LookupAccountName(None, winuser)[0]
            hwid = win32security.ConvertSidToStringSid(sid)
            return hwid
            '''
            cmd = subprocess.Popen(
                "wmic useraccount where name='%username%' get sid",
                stdout=subprocess.PIPE,
                shell=True,
            )
                        
            (suppost_sid, error) = cmd.communicate()
                        
            suppost_sid = suppost_sid.split(b"\n")[1].strip()
                                
            return suppost_sid.decode()
                            
            ^^ HOW TO DO IT USING WMIC
            '''
        elif platform.system() == 'Darwin':
            output = subprocess.Popen("ioreg -l | grep IOPlatformSerialNumber", stdout=subprocess.PIPE, shell=True).communicate()[0]
            serial = output.decode().split('=', 1)[1].replace(' ', '')
            hwid = serial[1:-2]
            return hwid