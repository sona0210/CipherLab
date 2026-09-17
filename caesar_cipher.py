# CipherLab - Caesar Cipher Encryption Tool


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            shifted_char = chr(
                (ord(char) - start + shift) % 26 + start
            )

            result += shifted_char

        else:
            result += char

    return result


print("=" * 50)
print("             🔐 CIPHERLAB")
print("=" * 50)
print("Caesar Cipher Encryption Tool")
print("-" * 50)

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\nChoose an operation:")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    result = caesar_cipher(message, shift)
    operation = "Encryption"

elif choice == "2":
    result = caesar_cipher(message, -shift)
    operation = "Decryption"

else:
    print("\nInvalid choice. Please select 1 or 2.")
    exit()


print("\n--- Result ---")
print("Original Message :", message)
print(f"{operation} Result  :", result)

print("\n" + "=" * 50)
print(f"          {operation.upper()} COMPLETED")
print("=" * 50)