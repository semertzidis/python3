from pycoin.key.BIP32Node import BIP32Node
from pycoin.symbols.btc import network

YEAR = "2016"
BATCH = "1"

mpubkey = 'xpub661MyMwAqRbcH37ey3eoQnHgSXokTBkTbqWSBGdJT4puCX1q8mBB5QHe39L5jhkuE2 SMremPML7LV2MJC2KE8bvvgJXubkW7wfxeGFTMRoJ'

def generate_many(number_of_addresses):
  key = network.parse.bip32(mpubkey)
  key_path_batch = key.subkey_for_path(YEAR + "/" + BATCH)
  for i in range(number_of_addresses):
      subkey = key_path_batch.subkey(i)
      print("{0}".format(subkey.address(1))) # 1 for the internal keypair chain

if __name__ == '__main__':
    generate_many(5)
