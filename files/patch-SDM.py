--- SDM.py.orig	2017-04-09 23:46:09 UTC
+++ SDM.py
@@ -18,7 +18,7 @@ from CppBlockUtils import SecureBinaryDa
    
 from armoryengine.ArmoryUtils import BITCOIN_PORT, LOGERROR, hex_to_binary, \
    ARMORY_INFO_SIGN_PUBLICKEY, LOGINFO, BTC_HOME_DIR, LOGDEBUG, OS_MACOSX, \
-   OS_WINDOWS, OS_LINUX, SystemSpecs, subprocess_check_output, LOGEXCEPT, \
+   OS_WINDOWS, OS_LINUX, OS_FREEBSD, SystemSpecs, subprocess_check_output, LOGEXCEPT, \
    FileExistsError, OS_VARIANT, BITCOIN_RPC_PORT, binary_to_base58, isASCII, \
    USE_TESTNET, USE_REGTEST, GIGABYTE, launchProcess, killProcessTree, killProcess, \
    LOGWARN, RightNow, HOUR, PyBackgroundThread, touchFile, secondsToHumanTime, \
@@ -142,7 +142,7 @@ class SatoshiDaemonManager(object):
          if not os.path.exists(self.dbExecutable):
             self.dbExecutable = "./ArmoryDB.exe"
       
-      if OS_LINUX:
+      if OS_LINUX or OS_FREEBSD:
          #if there is no local armorydb in the execution folder, 
          #look for an installed one
          if not os.path.exists(self.dbExecutable):
