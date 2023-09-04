# Bitcoin Vanity Address Generator

This Python project provides a Bitcoin Vanity Address Generator, allowing you to create customized Bitcoin addresses with specific prefixes. It consists of two main files:

## Files

1. **bitcoin.py**: Contains the `BTCVanity` class for generating customized vanity Bitcoin addresses.
2. **main.py**: The main script that takes user input for the desired prefix and generates the vanity address.

## Getting Started

To use the Bitcoin Vanity Address Generator, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine or download the source code.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the main script to start the vanity address generation.

5. Enter three characters as a vanity prefix when prompted.

6. The script will generate a customized vanity Bitcoin address and display it, along with the associated private key in Wallet Import Format (WIF).

## Code Structure

### `bitcoin.py`

- Defines the `BTCVanity` class responsible for customized vanity Bitcoin address generation.
- Includes methods for key generation, encoding, and documentation.

### `main.py`

- Imports the `BTCVanity` class and uses it to generate customized vanity Bitcoin addresses.
- Provides colored console output for clarity.
- Calls the `document` method for documentation.

## Usage

- Running the main script allows you to input your desired three-character vanity prefix.
- The script generates a vanity Bitcoin address with the specified prefix.
- The generated address is displayed in green text, and the associated private key is displayed in yellow text.

## Important Notes

- Vanity address generation is a computationally intensive process and may take time, especially for more complex prefixes.
- This code is for educational purposes and demonstrates basic vanity address generation.
