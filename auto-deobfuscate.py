import base64

def deobfuscate_string(obfuscated_string):
    # Example base64 decode
    try:
        decoded_bytes = base64.b64decode(obfuscated_string)
        decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
        return decoded_string
    except Exception as e:
        return f"Error during deobfuscation: {str(e)}"

obfuscated = "ZGVjb2RlX21l"
deobfuscated = deobfuscate_string(obfuscated)

print(f"Deobfuscated String: {deobfuscated}")
