# Spoof_Spoof
This program is used to make a MITM attack using an ARP spoofing. The program give you a list of the different IP target and sniff the transfered packet. 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Disclaimer: Any illicit use of this program is strictly prohibited. It is important to emphasize that users of Snake_Filer are solely responsible for their actions when using this program. I disclaim any liability for abusive or illicit use of the application by third parties. Users are required to comply with the laws and regulations in their jurisdiction when using Snake_Filer.

Spoof_Spoof is an automated MITM attack use for fun and discover the ARP spoofing. You can use it to do an ARP spoofing and sniffing the packet. Also, in the future with this program, perform automated DNS spoofing.
To make it right, you just need the IP target and your MAC adress. To help you choose an IP target, the program make a research in the network using nmap. After printing the different IP adress, make your choice and have
fun with this little MITM attack. 

Dependencies :
--
The program will run correctly only if you have Scapy, multiprocessing and logging modules. It's important to have Nmap application install in your computer or the program will not work.
Running the programm in Kali (in user root) is the best

Using Spoof_Spoof correctly:
--
When you have your IP target, it's important to change the value of the IP in the sniffing command in spoof_spoof.py file. Without that, the sniffing will never work.



References:
----
The program of Hafnium (in youtube) inspired me to make this program. 
