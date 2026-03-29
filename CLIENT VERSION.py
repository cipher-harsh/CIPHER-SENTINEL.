import psutil, os, threading, time, socket, requests, sys
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
from cryptography.fernet import Fernet

# ====== 🔐 MASTER CONFIG & ENCRYPTION ======
cipher_suite = Fernet(b'8_W1Yv4X7M9-L8Zp2_kR5T7v9X0J2m1n3B5v6C7D8E9=')
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
LOG_FILE = os.path.join(DESKTOP_PATH, "sentinel_core.dat") 
SUSPICIOUS_NAMES = ["keylogger", "trojan", "miner", "rat", "hacktool", "malware", "ransomware"]

# UI Themes
NEON_GREEN, CYAN, DARK_BG = "#00FF41", "#00D1FF", "#020202"
F_CODE, F_STATS = ("Courier New", 10, "bold"), ("Consolas", 9)

# Global Variables
text_box = None
btn_scan = None
stats_label = None
root = None

# ====== 🛠️ SYSTEM TERMINATE LOGIC (VS Code Fix) ======
def terminate_everything():
    """Kills all threads and closes the VS Code terminal immediately"""
    if root:
        root.destroy()
    # Forces the Python interpreter to exit, freeing the terminal
    os._exit(0)

# ====== 🛠️ CORE UTILITIES ======
def log(message, color=NEON_GREEN):
    if text_box:
        ts = datetime.now().strftime('%H:%M:%S')
        text_box.insert(tk.END, f"[{ts}] {message}\n", ("color", color))
        text_box.tag_config("color", foreground=color)
        text_box.see(tk.END)
    try:
        encrypted = cipher_suite.encrypt(f"[{datetime.now()}] {message}".encode())
        with open(LOG_FILE, "ab") as f: f.write(encrypted + b"\n")
    except: pass

def update_stats():
    """Real-time CPU/RAM/IP tracking"""
    try: pub_ip = requests.get('https://api.ipify.org', timeout=5).text
    except: pub_ip = "Offline"
    while True:
        try:
            cpu, ram = psutil.cpu_percent(), psutil.virtual_memory().percent
            local_ip = socket.gethostbyname(socket.gethostname())
            if stats_label:
                stats_label.config(text=f"CPU: {cpu}% | RAM: {ram}%\nL-IP: {local_ip}\nP-IP: {pub_ip}")
        except: break
        time.sleep(3)

def run_scan():
    """Deep heuristic process scanning"""
    def task():
        btn_scan.config(state="disabled")
        log(">>> INITIATING DEEP HEURISTIC SCAN...", CYAN)
        found = 0
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                name = (proc.info['name'] or "").lower()
                if any(bad in name for bad in SUSPICIOUS_NAMES):
                    log(f"[ALERT] MALWARE SIGNATURE: {name} (PID: {proc.info['pid']})", "#FF3131")
                    found += 1
            except: continue
        log(f">>> SCAN FINISHED. {found} THREATS IDENTIFIED.")
        btn_scan.config(state="normal")
    threading.Thread(target=task, daemon=True).start()

def kill_proc():
    pid = simpledialog.askinteger("Admin", "Enter PID to Terminate:")
    if pid:
        try:
            psutil.Process(pid).terminate()
            log(f">>> PROCESS {pid} KILLED SUCCESSFULLY.", CYAN)
        except Exception as e:
            log(f">>> ERROR: {e}", "#FF3131")

# ====== 🖥️ MAIN INTERFACE ======
def init_gui():
    global text_box, btn_scan, stats_label, root
    root = tk.Tk()
    root.title("CIPHER-SENTINEL | Cyber Security Core")
    root.geometry("1100x750")
    root.configure(bg=DARK_BG)

    # CRITICAL: Red Close Button (X) triggers full exit, no more hiding
    root.protocol('WM_DELETE_WINDOW', terminate_everything)

    # Sidebar UI
    side = tk.Frame(root, bg="#050505", width=260, highlightthickness=1, highlightbackground="#1A1A1A")
    side.pack(side="left", fill="y", padx=5, pady=5)

    tk.Label(side, text="CIPHER-SENTINEL", bg="#050505", fg=NEON_GREEN, font=("Impact", 24)).pack(pady=25)
    
    stats_label = tk.Label(side, text="BOOTING...", bg="#0A0A0A", fg=CYAN, font=F_STATS, pady=15, width=30)
    stats_label.pack(pady=10, padx=10)

    btn_opt = {"font": F_CODE, "bg": "#0A0A0A", "relief": "flat", "width": 22, "pady": 10}
    
    btn_scan = tk.Button(side, text="DEEP SCAN", fg=NEON_GREEN, command=run_scan, **btn_opt)
    btn_scan.pack(pady=5)
    
    tk.Button(side, text="KILL PROCESS", fg=CYAN, command=lambda: threading.Thread(target=kill_proc).start(), **btn_opt).pack(pady=5)
    
    # "Hide to Tray" button has been removed as per your request.

    tk.Button(side, text="SHUTDOWN CORE", fg="#FF3131", command=terminate_everything, **btn_opt).pack(side="bottom", pady=30)

    # Console Terminal UI
    term = tk.Frame(root, bg="#000")
    term.pack(side="right", expand=True, fill="both", padx=5, pady=5)
    text_box = ScrolledText(term, bg="#000", fg=NEON_GREEN, font=F_CODE, borderwidth=0, insertbackground=NEON_GREEN)
    text_box.pack(expand=True, fill="both", padx=10, pady=10)

    # Background threads
    threading.Thread(target=update_stats, daemon=True).start()
    
    log(">>> CIPHER-SENTINEL CORE v1.0 ONLINE.")
    log(">>> ALL DEFENSIVE MODULES ARMED.")
    
    root.mainloop()

if __name__ == "__main__":
    init_gui()