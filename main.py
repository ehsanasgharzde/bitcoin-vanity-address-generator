from bitcoin import BTCVanity, green, yellow


str = input("\nEnter 3 Characters: ")
btcvanity = BTCVanity(str)


if __name__ == '__main__':
    btcvanity.document()

    print(green("\nVanity Bitcoin Address: "), yellow(btcvanity.VADDRESS))
    print(green("Vanity Private Key WIF: "), yellow(btcvanity.VWIF))
