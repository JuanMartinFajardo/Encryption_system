## About this software

This is a encryption method that I created when I was 16 years old. It is not very efficient, but it was one of my first incursions into the programming world. So I leave it here. I called it 'WatCrypter'.


## How to use it
Execute main.py in the terminal. There is a text user interface that allows the user to navigate the different options:

<img width="513" height="194" alt="Captura de pantalla 2025-11-10 a las 13 46 00" src="https://github.com/user-attachments/assets/09a652d1-354a-49b6-ae88-a7f4020ba15e" />




# WatCrypter: A Positional Frequency-Map Encryption System

WatDcrypt is a probabilistic encryption algorithm. Unlike traditional ciphers that substitute characters (e.g., 'a' → 'X'), this system encrypts the **structural positions** of each character within the message.

The final ciphertext is not a string of text, but a **frequency map** (a histogram) that describes the randomly generated numbers used to "draw" the message's structure. Encrypting the same message twice will produce two different, valid ciphertexts.

---

## ⚠️ Security Warning & Honest Assessment

This project was created as a creative exploration of cryptographic concepts.

**This is an experimental and educational algorithm and should NOT be used to protect sensitive data.**

* **Vulnerability:** The core encryption logic (without the noise layer) is vulnerable to a structural frequency analysis. An attacker can find the "anchor pattern" (where an inner layer's frequency matches the marker's frequency) to reverse-engineer the message positions *without* the key.
* **The "Noise" Layer:** The optional security layer (`encriptadorV4.py`) significantly complicates this specific attack by introducing "false positive" patterns. This makes the real signal much harder to find, but it is a form of *obscurity*, not formal security.
* **Not Formally Secure:** This algorithm has not been subjected to a formal cryptographic review. Its security relies on its custom, obscure nature, not on proven mathematical hardness.
* **Efficiency:** The algorithm is computationally slow and produces a ciphertext that is significantly larger than the original plaintext.

This repository is best viewed as a "case study" in custom cipher design and a fun cryptographic puzzle.

---

## How it Works

### 1. The Key (The Map)

The **`key`** is a sorted list of 256 integers. This key a **map** that divides the number line into 256 "intervals" or "bins," one for each ASCII character.

* The number at `key[97]` (for 'a') might be **15**.
* The number at `key[98]` (for 'b') might be **23**.

This means:
* **Character 'a'** "owns" the number range `(previous_key_num, 15]`.
* **Character 'b'** "owns" the number range `(15, 23]`.

These key numbers (15, 23, etc.) are called **"markers."**

### 2. Encryption (The position encoder)

This is the core of the algorithm. Let's encrypt the message **"banana"**.

1.  **Find Positions:** The algorithm first finds all positions for a unique character.
    * **'a'** is at positions `[1, 3, 5]`.

2.  **Build Nested Layers:** It works backward from the highest position (5) to encode this structure.
    * **Layer 1 (for position 5):**
        * It picks **5** unique random numbers from 'a's range (e.g., 1-15).
        * *Result:* `[10, 12, 4, 7, 14]`
    * **Layer 2 (for position 3):**
        * It picks **3** unique random numbers *from the previous layer's* results.
        * *Result:* `[12, 7, 14]`
    * **Layer 3 (for position 1):**
        * It picks **1** unique random number *from the previous layer's* results.
        * *Result:* `[7]`

3.  **Add Markers:** All generated numbers are collected, and the 'a' marker (15) is added once for every 'a' in the message (3 times).
    * *Final list for 'a':* `[10, 12, 4, 7, 14, 12, 7, 14, 7, 15, 15, 15]`

This process is repeated for 'b' (positions `[4]`) and 'n' (positions `[0, 2]`).

### 3. The Ciphertext (`msn`)

All numbers generated for all characters are combined, sorted, and converted into a **frequency map**. The output `msn` is a list containing two lists: `msn[0]` (the numbers) and `msn[1]` (their counts).

The partial map for 'a' would look like this:
* `Numbers`: `[... 4, 7, 10, 12, 14, 15 ...]`
* `Counts`: `[... 1, 3, 1, 2, 2, 3 ...]`

This reveals the **"anchor pattern"**: the number from the innermost layer (`7`) and the marker (`15`) both have the highest frequency (3), which is the total count of the character 'a'.

### 4. Decryption (`decode`)

The decrypter reverses this logic **using the key**.

1.  **Find Marker:** It iterates through its `key`. It finds `15` and knows this is 'a'.
2.  **Check Frequency:** It looks up `15` in `msn` and sees its frequency is **3**. It now knows 'a' appeared 3 times.
3.  **Define Range:** It knows 'a's range is `(previous_key_num, 15]`.
4.  **Rebuild Layers (in reverse):**
    * It asks: "How many numbers in this range have a frequency of **3 or more**?"
        * *Answer:* `[7]` (and the marker 15). The list length is **1**. It places an 'a' at **position 1**.
    * It asks: "How many numbers in this range have a frequency of **2 or more**?"
        * *Answer:* `[7, 12, 14]`. The list length is **3**. It places an 'a' at **position 3**.
    * It asks: "How many numbers in this range have a frequency of **1 or more**?"
        * *Answer:* `[4, 7, 10, 12, 14]`. The list length is **5**. It places an 'a' at **position 5**.

The original positions `[1, 3, 5]` are recovered. The decrypter ignores all noise from the security layer because it falls outside the key-defined ranges it is looking for.

---

## Files in this Repository

* `encriptadorV4.py`: The Python script to encrypt a message. It contains the position encoder logic and the optional "noise" security layer.
* `WatDcrypt.py`: The Python script to decrypt the `msn` (ciphertext) back into the original message.
* `KeyCreator`: The Python script to create key.
* `main.py`:  The Python script to run.

### Current HASH of main.py
42c14f6180caf8d18b324096587ccdca01c0a1a3c96f788dcda43c5ebd09ff3b
