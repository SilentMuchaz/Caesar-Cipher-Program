"""Educational Caesar cipher with predictable ASCII letter handling.

This is a classical substitution cipher, not secure modern encryption.
"""


def caesar_shift(message: str, shift: int, mode: str) -> str:
    """Encrypt or decrypt ASCII letters, preserving case and other characters.

    Args:
        message: Text to transform.
        shift: Any integer rotation, including negative values.
        mode: Either 'encrypt' or 'decrypt' (case-insensitive).

    Returns:
        The transformed text.

    Raises:
        TypeError: If message is not a string or shift is not an integer.
        ValueError: If mode is not encrypt or decrypt.
    """
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    if type(shift) is not int:
        raise TypeError("shift must be an integer")
    if not isinstance(mode, str) or mode.lower() not in {"encrypt", "decrypt"}:
        raise ValueError("mode must be 'encrypt' or 'decrypt'")

    offset = shift % 26
    if mode.lower() == "decrypt":
        offset = -offset

    output = []
    for char in message:
        if "A" <= char <= "Z":
            output.append(chr((ord(char) - ord("A") + offset) % 26 + ord("A")))
        elif "a" <= char <= "z":
            output.append(chr((ord(char) - ord("a") + offset) % 26 + ord("a")))
        else:
            output.append(char)
    return "".join(output)


def prompt_shift() -> int:
    """Ask again when a shift key is not a valid integer."""
    while True:
        raw = input("Shift key (integer): ")
        try:
            return int(raw)
        except ValueError:
            print("Invalid shift key. Enter a whole number, such as 3 or -3.")


def prompt_mode() -> str:
    """Ask again until a supported operation is chosen."""
    while True:
        mode = input("Mode (encrypt/decrypt): ").strip().lower()
        if mode in {"encrypt", "decrypt"}:
            return mode
        print("Invalid mode. Enter 'encrypt' or 'decrypt'.")


def main() -> None:
    print("=== CAESAR CIPHER ===")
    message = input("Message: ")
    shift = prompt_shift()
    mode = prompt_mode()
    result = caesar_shift(message, shift, mode)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
