"""Tests for the improved educational Caesar cipher implementation."""

import unittest
from caesar_cipher import caesar_shift


class CaesarCipherTests(unittest.TestCase):
    def test_encrypt_basic(self):
        self.assertEqual(caesar_shift("HELLO", 3, "encrypt"), "KHOOR")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_shift("KHOOR", 3, "decrypt"), "HELLO")

    def test_preserves_mixed_case(self):
        self.assertEqual(caesar_shift("Attack at Dawn!", 5, "encrypt"), "Fyyfhp fy Ifbs!")

    def test_preserves_punctuation_and_digits(self):
        self.assertEqual(caesar_shift("Hello, World! 123", 3, "encrypt"), "Khoor, Zruog! 123")

    def test_wraps_alphabet(self):
        self.assertEqual(caesar_shift("XYZ xyz", 3, "encrypt"), "ABC abc")

    def test_shift_above_26(self):
        self.assertEqual(caesar_shift("HELLO", 29, "encrypt"), "KHOOR")

    def test_negative_shift(self):
        self.assertEqual(caesar_shift("HELLO", -3, "encrypt"), "EBIIL")

    def test_zero_shift(self):
        self.assertEqual(caesar_shift("Hello!", 0, "encrypt"), "Hello!")

    def test_round_trip(self):
        text = "Network Security: VLAN-10 / Port 22"
        encrypted = caesar_shift(text, 17, "encrypt")
        self.assertEqual(caesar_shift(encrypted, 17, "decrypt"), text)

    def test_non_ascii_characters_unchanged(self):
        self.assertEqual(caesar_shift("Café", 3, "encrypt"), "Fdié")

    def test_rejects_invalid_mode(self):
        with self.assertRaises(ValueError):
            caesar_shift("HELLO", 3, "reverse")

    def test_rejects_non_integer_shift(self):
        with self.assertRaises(TypeError):
            caesar_shift("HELLO", "three", "encrypt")

    def test_rejects_non_string_message(self):
        with self.assertRaises(TypeError):
            caesar_shift(None, 3, "encrypt")

    def test_mode_case_insensitive(self):
        self.assertEqual(caesar_shift("HELLO", 3, "ENCRYPT"), "KHOOR")


if __name__ == "__main__":
    unittest.main()
