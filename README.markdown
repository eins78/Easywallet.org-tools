= What is it?

Tools to use with easywallet.org

Currently has a one bot, which makes a new easywallet.org wallet, and stores the information at ~/.iw-console

It asks for your currency of choice, and the range you want to keep the wallet at. It excepts that you have local "bitcoind" instance, where you transfer the funds from your easywallet.

After running the script initially, jsut put it to a cron script to be run regularly, and you will have auto-loading wallet.

The advantages of this setup are:

- When you pay someone, he canät divulge your personal financial information
- When you receive money, the same
- When you receive lots of money, the funds are automatically transferred to more secure location
- When you spend lots of money, your wallet is automatically reloaded from your safer account

