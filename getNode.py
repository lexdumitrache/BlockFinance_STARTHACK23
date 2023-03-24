import json
import time

from bitcoinrpc.authproxy import AuthServiceProxy

rpc_user = 'bitcoin'
rpc_password = 'bitcoin'
rpc_port = '8332'
rpc_host = 'localhost'


def print_last_block_transactions():
    rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')
    latest_block_hash = rpc_connection.getbestblockhash()
    latest_block_info = rpc_connection.getblock(latest_block_hash)

    for txid in latest_block_info['tx']:
        tx_info = rpc_connection.getrawtransaction(txid, True, latest_block_hash)
        print("Transaction ID: ", txid)
        print("Transaction hex: ", tx_info['hex'])
        dec = bytes.fromhex(tx_info['hex']).decode('utf-8', 'ignore')
        print("Transacrion decripted hex ", dec)
        for vout in tx_info['vout']:
            if 'scriptPubKey' in vout and 'hex' in vout['scriptPubKey']:
                print("ScriptPubKey hex: ", vout['scriptPubKey']['hex'])

    return latest_block_hash


if __name__ == '__main__':
    # endless print the latest block transactions, every minute check for new block
    last_hash = print_last_block_transactions()
    time.sleep(60)
    while True:
        rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')
        test = latest_block_hash = rpc_connection.getbestblockhash()
        if last_hash != test:
            last_hash = print_last_block_transactions()
        time.sleep(60)