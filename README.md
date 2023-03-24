# BlockFinance_STARTHACK23

## 1. Wallet and accounts 
- A HD bip85 wallet was set up on our node using Electrum (https://electrum.org)
- 8 different accounts were generated using different bip39 seeds
- all seed phrases where generated using ([link](https://getcoinplate.com/bip39-seed-phrase-mnemonics-generator-offline-online-tool/))

## 2. Vault 
- A vault was set up using Airgap (https://github.com/airgap-it/airgap-vault)

## 3. Node setup 
A full was set up on local server
**(carichiamo il file di con conf???)**

  
## 5. Payment Server
- BTCpay was deployed on cloud using (https://www.lunanode.com)
- payment server was linked to our wallet 
- SSH connection to the server was established 
- blockchain synchronization of the remote server's node is still ongoing 

## 6. Website 
A simple one page ecommerce was created usign BTCpay "app" functionality https://btcpay943121.lndyn.com/apps/2MqxSZgNypVSrqYsLEBt9rR17fhx/pos
<img width="772" alt="Schermata 2023-03-24 alle 04 34 09" src="https://user-images.githubusercontent.com/128647197/227454632-57d9c3f9-3493-465a-a2f9-cd0c3e0898a1.png">

## 7. Invoices 
invoice.py exploit REST api of BTCpayment to POST invoices, invoices are then collected on a sql databese hsoted locally

## 8.Hidden Messages
- secretmessage contains the instructions to collect the message from the genesis block, bitcoincli was used
- getnode.py check for new block on the chain every 60 seconds check and print the ifnormation contained in new blocks. 
