import hashlib
import os


def calculate_sha256(file_path):
    """
    Calculate SHA256 hash of a file.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

    except Exception as e:
        print(f"[ERROR] {e}")
        return None


def verify_integrity(file_path, known_hash):
    """
    Compare current file hash against known hash.
    """

    current_hash = calculate_sha256(file_path)

    if current_hash is None:
        return

    print("\nCurrent SHA256 Hash:")
    print(current_hash)

    print("\nStored SHA256 Hash:")
    print(known_hash)

    if current_hash == known_hash:
        print("\n[PASS] File integrity verified.")
        print("The file has not changed.")
    else:
        print("\n[ALERT] Integrity check FAILED!")
        print("The file may have been modified.")


def main():

    print("=" * 60)
    print("File Integrity Checker (SHA256)")
    print("=" * 60)

    print("\nChoose an option:")
    print("1. Generate SHA256 hash")
    print("2. Verify file integrity")

    choice = input("\nSelection: ").strip()

    if choice == "1":

        file_path = input("\nEnter file path: ").strip()

        hash_value = calculate_sha256(file_path)

        if hash_value:
            print("\nGenerated SHA256 Hash:")
            print(hash_value)

    elif choice == "2":

        file_path = input("\nEnter file path: ").strip()

        known_hash = input(
            "\nEnter previously saved SHA256 hash: "
        ).strip()

        verify_integrity(file_path, known_hash)

    else:
        print("\nInvalid selection.")


if __name__ == "__main__":
    main()
