🚀 Project Name : Maurya
===============

**Maurya: Virustotal Domain Analyzer for extracting sensitive info .**

📌 Overview


*_Maurya_*  is a security analysis tool in Python that interfaces with VirusTotal's API for domain reputation checking. It implements comprehensive error handling and JSON response parsing and created formatted output display for security analysis results including BitDefender findings and detected samples. In that JSON output you can get sensitive info like username , passwords etc.. 


### 🤔 Why This Name?


Just because I wanted to name it something cool yet classic, like 'Dynasty'.



### ⌚ Total Time taken to build & test

 Approx :20 min.

### 🙃 Why I Created This


You all know that bug hunters, especially those using CLI tools like Subfinder, Amass, Nuclei, Dirsearch, etc. Personally, I’ve been running into issues while bug hunting that I have to find the admin panel or subdomain for every domain using dorking, then set it up with the VirusTotal API. After that, I search for the URL like this: **https://[API_KEY].[domain or login panel]**, and then I have to sift through it using Ctrl + F to find any sensitive details.
This whole process is pretty lengthy, and I thought it would be way better if we could automate it with a CLI version. That’s why I decided to create this tool.

### 🔧 Requirements & Dependencies

*    Virus Total API 
*    Python ( latest version )

### 📥 Installation Guide & Usuage
<!-- --------------------- -->


 ```bash
git clone https://github.com/gigachad80/Maurya
cd Maurya
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 maurya.py
```
Step 1:  Now aftter running maurya.py , enter any domain and set your API key.

Step 2: That's it , just wait for 2-3 sec. and you'll get your output
                

### 📞 Contact


📧 Email: pookielinuxuser@tutamail.com


### 📄 License

Licensed under **MIT**


🕒 Last Updated: January 23, 2025








