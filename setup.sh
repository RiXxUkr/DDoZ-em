clear
echo '#===========================[Setup]===========================#'
echo "[i] Installing 'Python 3'..."
sudo apt-get install python3
echo ""
echo "[i] Installing 'Python 3 Pip'..."
sudo apt-get install python3-pip
echo ""
echo "[i] Installing 'Python 3 Requirements'..."
sudo pip3 install -r requirements.txt
echo ""
echo '#===========================[Done!]===========================#'
read -p 'Press any key to continue . . . '
