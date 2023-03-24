# BlockFinance_STARTHACK23

## 1. Wallet and accounts 
- a HD bip85 wallet was set up on our node using [Electrum](https://electrum.org)
- 8 different accounts for different purpouses (main, accounting, salaries, fundraising, investments, etc...) were generated using different bip39 seeds 
- all seed phrases where generated using [getcoinplate](https://getcoinplate.com/bip39-seed-phrase-mnemonics-generator-offline-online-tool/)

## 2. Vault 
- a vault was set up using [Airgap](https://github.com/airgap-it/airgap-vault)

## 3. Node setup 
- a full [bitcoin node](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/bitcoin.conf) was set up on local server
  
## 5. Payment Server
- BTCpay was deployed on cloud using [lunanode](https://www.lunanode.com)
- payment server was linked to our wallet 
- SSH connection to the server was established 
- blockchain synchronization of the remote server's node is still ongoing 

## 6. Website 
- a simple [one page ecommerce](https://btcpay943121.lndyn.com/apps/2MqxSZgNypVSrqYsLEBt9rR17fhx/pos) was created usign BTCpay "app" functionality 
<img width="772" alt="Schermata 2023-03-24 alle 04 34 09" src="https://user-images.githubusercontent.com/128647197/227454632-57d9c3f9-3493-465a-a2f9-cd0c3e0898a1.png">

## 7. Invoices 
- [invoice.py](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/invoice.py) exploit REST api of BTCpayment to POST invoices, invoices are then collected on a sql databese hosted locally

## 8. Hidden Messages
- [secretmessage](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/secretmessage.txt) contains the instructions to collect the message from the genesis block, bitcoincli was used
- [getnode.py](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/getNode.py) check for new block on the chain every 60 seconds check and print the ifnormation contained in new blocks.

## 9. Paperwallet
- a [paperwallet](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/paperwallet_gift.pdf) was created as a gift for the newborn baby of a fictional employee

## 10. Script
- wrote a script that looks for Bitcoin message in every other Bitcoin block

## 11. Account statements
- provided accounts statements with [transaction lookups](https://github.com/lexdumitrache/BlockFinance_STARTHACK23/blob/main/txLookup.pdf) and CSV exports
