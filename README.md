# 🛡️ CIPHER-SENTINEL

**CIPHER-SENTINEL** is a high-performance, Python-based cybersecurity utility designed for real-time system monitoring, heuristic threat detection, and secure activity logging.

---

## 🚀 Key Features

* **Heuristic Process Scanning:** Real-time identification of suspicious process signatures and potential malware activity.
* **Live System Metrics:** Continuous tracking of CPU usage, RAM utilization, and Network IP (Local & Public) status.
* **Encrypted Logging:** Activity logs are automatically generated and stored in a secure `.dat` format using Fernet (AES-128) encryption.
* **Admin-Grade Security:** Logs are tamper-proof and remain inaccessible without the specialized Master Admin Decryptor.
* **Terminal Integration:** Optimized for clean execution within VS Code and standalone environments.

## 📂 Project Structure

| File Name | Description |
| :--- | :--- |
| `CLIENT VERSION.py` | Original Python source code including the GUI and Core logic. |
| `CLIENT VERSION.exe` | Standalone Windows executable (No Python installation required). |
| `sentinel_core.dat` | Encrypted log file generated on the User's Desktop. |

## 🛠️ Installation & Usage

1.  **Download:** Clone this repository or download the `CLIENT VERSION.exe` from the releases.
2.  **Execute:** Run the application. Ensure you have administrative privileges for accurate process scanning.
3.  **Monitor:** Use the dashboard to track system health and initiate a **Deep Scan**.
4.  **Log Generation:** Upon execution, the tool will create `sentinel_core.dat` on your Desktop to record all security events.

## 🔐 Log Decryption (OMEGA-SHIELD)

To maintain the integrity of security data, all generated logs are encrypted. 

> [!CAUTION]
> **Logs are not readable in standard text editors.** Accessing the readable `.txt` format requires the **OMEGA-SHIELD Master Admin Tool** and the private decryption key.

## 📧 Contact & Support

For access to the **Master Admin Tool**, private security keys, or professional collaboration, please reach out via the following channels:

* **Developer:** Harsh Patel
* **GitHub:** [@cipher-harsh](https://github.com/cipher-harsh)
* **Email:** harshcipher@gmail.com

---
*Disclaimer: This tool is intended for educational and ethical system monitoring purposes only.*
