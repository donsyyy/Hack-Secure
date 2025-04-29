from cryptography.fernet import Fernet
import os

def generate_key():
    #Generate and save a secret key
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the secret key from file"""
    return open("secret.key", "rb").read()

def encrypt_file(input_filename, key, output_filename=None):
    """Encrypt a file with option to specify output filename"""
    fernet = Fernet(key)
    
    with open(input_filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output filename
    if not output_filename:
        output_filename = input_filename + ".enc"
    
    with open(output_filename, "wb") as file:
        file.write(encrypted_data)
    
    print(f"File encrypted successfully. Encrypted file: {output_filename}")
    return output_filename

def decrypt_file(input_filename, key, output_filename=None):
    """Decrypt a file with option to specify output filename"""
    fernet = Fernet(key)
    
    with open(input_filename, "rb") as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except:
        print("Invalid key or corrupted file")
        return None
    
    # Determine output filename
    if not output_filename:
        if input_filename.endswith('.enc'):
            output_filename = input_filename[:-4]  # Remove .enc extension
        else:
            output_filename = input_filename + ".dec"
    
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File decrypted successfully. Decrypted file: {output_filename}")
    return output_filename

def main():
    print("File Encryption/Decryption Tool")
    print("-------------------------------")
    
    # Check if key exists, otherwise generate one
    if not os.path.exists("secret.key"):
        print("Generating new secret key...")
        key = generate_key()
    else:
        key = load_key()
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            input_filename = input("Enter the file to encrypt: ").strip()
            if not os.path.exists(input_filename):
                print("File not found!")
                continue
                
            output_option = input("Save as new file? (y/n): ").lower()
            if output_option == 'y':
                output_filename = input("Enter output filename: ").strip()
                encrypt_file(input_filename, key, output_filename)
            else:
                encrypt_file(input_filename, key)
        
        elif choice == "2":
            input_filename = input("Enter the file to decrypt: ").strip()
            if not os.path.exists(input_filename):
                print("File not found!")
                continue
                
            output_option = input("Save as new file? (y/n): ").lower()
            if output_option == 'y':
                output_filename = input("Enter output filename: ").strip()
                decrypt_file(input_filename, key, output_filename)
            else:
                decrypt_file(input_filename, key)
        
        elif choice == "3":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
