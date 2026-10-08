import base64

def obfuscate_payload(payload, lang):
    if lang == "bash":
        return f"eval $(echo {base64.b64encode(payload.encode()).decode()} | base64 -d)"

    elif lang == "python":
        encoded = base64.b64encode(payload.encode()).decode()
        return f"import base64; exec(base64.b64decode('{encoded}'))"

    elif lang == "php":
        encoded = base64.b64encode(payload.encode()).decode()
        return f"<?php eval(base64_decode('{encoded}')); ?>"

    elif lang == "nc":
        return f"# Original: {payload}\n# Netcat payloads are usually simple and can't be fully obfuscated.\n# Consider using a wrapper script."

    elif lang == "powershell":
        encoded = base64.b64encode(payload.encode('utf-16le')).decode()
        return f"powershell -EncodedCommand {encoded}"

    else:
        return "[ERROR] Language not supported."

lang = input("Enter language (bash/python/php/nc/powershell): ").strip().lower()
payload = input("Enter your payload: ").strip()

obfuscated = obfuscate_payload(payload, lang)

print("\n[+] Obfuscated Payload:\n")
print(obfuscated)
