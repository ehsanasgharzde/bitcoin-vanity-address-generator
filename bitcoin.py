import hashlib
import base58
import binascii
import ecdsa


def green(text):
    """
    ANSI Code to turn strings green.
    """
    return f"\033[92m{text}\033[0m"


def yellow(text):
    """
    ANSI Code to turn strings yellow.
    """
    return f"\033[93m{text}\033[0m"


class BTCVanity():
    def __init__(self, str):
        """
        VPVKEY: Private Key (with costum replacement)
        VPUKEY: Public Key
        VSHA256PUKEY: SHA256 Encoded Public Key
        VRIDEMP160PUKEY: RIDEMP160 Encoded VSHA256PUKEY
        VNBPUKEY: '00' added to the beginning of VRIDEMP160PUKEY
        VNBPVKEY: '80' added to the end of VPVKEY
        VDOUSHA256PU: Double SHA256 Encoded VNBPUKEY
        VDOUSHA256PV: Double SHA256 Encoded VNBPVKEY
        VCHECKSUMPU: VDOUSHA256PU first 4 bytes
        VCHECKSUMPV: VDOUSHA256PV first 4 bytes
        VPREADDRESS: VCHECKSUMPU added to VNBPUKEY
        VPREWIF: VCHECKSUMPV added to VNBPVKEY
        VADDRESS: Base58 Encoded VPREADDRESS
        VWIF: Base58 Encoded VPREWIF
        """
        curve = ecdsa.SECP256k1
        key = ecdsa.SigningKey.generate(curve=curve)
        replacement = "".join(key.to_string().hex()[1:4])
        self.VPVKEY = key.to_string().hex().replace(replacement, str, 1)
        self.VPUKEY = f"04{self.VPVKEY}"
        self.VSHA256PUKEY = hashlib.sha256(
            binascii.unhexlify(self.VPUKEY)).hexdigest()
        self.VRIDEMP160PUKEY = hashlib.new(
            "ripemd160", binascii.unhexlify(self.VSHA256PUKEY)).hexdigest()
        self.VNBPUKEY = f"00{self.VRIDEMP160PUKEY}"
        self.VNBPVKEY = f"80{self.VPVKEY}"
        self.VDOUSHA256PU = self.DouSHA256(self.VNBPUKEY)
        self.VDOUSHA256PV = self.DouSHA256(self.VNBPVKEY)
        self.VCHECKSUMPU = self.VDOUSHA256PU[:8]
        self.VCHECKSUMPV = self.VDOUSHA256PV[:8]
        self.VPREADDRESS = self.VNBPUKEY + self.VCHECKSUMPU
        self.VPREWIF = self.VNBPVKEY + self.VCHECKSUMPV
        self.VADDRESS = base58.b58encode(
            binascii.unhexlify(self.VPREADDRESS)).decode("UTF-8")
        self.VWIF = base58.b58encode(
            binascii.unhexlify(self.VPREWIF)).decode("UTF-8")

    def DouSHA256(self, str):
        DOUSHA256PU = str
        for i in range(1, 3):
            DOUSHA256PU = hashlib.sha256(
                binascii.unhexlify(DOUSHA256PU)).hexdigest()
        return DOUSHA256PU

    def document(self):
        docs = """
        Libraries:
        hashlib
            Hash Encodings Library
            --> Usage: Encoding
        base58
            Base58 Encodings Library
            --> Usage: Encoding
        binascii
            binary and ASCII Library
            --> Usage: Convertion between Binary and ASCII values
        ecdsa
            Ellicptic Curve Digital Signature Algorithm 
            --> Usage: Generate Private Key

        Step 1:
        Creating Private Key with SECP256k1 curve

        Step 2:
        Replacing Private Key [1:4] characters with costum characters

        Step 3:
        Creating Public Key based on previuos Private Key

        Step 4:
        Applying SHA256 Encoding to previous Public Key

        Step 5:
        Applying RIDEMP160 Encoding to previous SHA256 Encoded Public Key

        Step 6:
        Prepending "00" as Network Byte to previous RIDEMP160 Encoded Public Key

        Step 7:
        Applying Double SHA256 to previous Network Byte Public Key

        Step 8:
        Getting a Checksum from previous Double SHA256 Encoded Public Key
        First 4 bytes are the Checksum

        Step 9:
        Adding Checksum to Network Byte Public Key

        Step 10:
        Applying Base58 Encoding to previous Pre Address

        Step 11:
        Adding "80" as Network Byte to Private Key

        Step 12:
        Applying Double SHA256 to previous Network Byte Private Key

        Step 13:
        Getting a Checksum from previous Double SHA256 Encoded Private Key
        First 4 bytes are the Checksum

        Step 14:
        Adding Checksum to Network Byte Private Key

        Step 15:
        Applying Base58 Encoding to previous Pre WIF\n\n"""

        print(docs)
