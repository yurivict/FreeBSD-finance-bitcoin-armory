--- ArmoryQt.py.orig	2017-04-09 23:46:09 UTC
+++ ArmoryQt.py
@@ -1,4 +1,4 @@
-#! /usr/bin/python
+#!/usr/bin/env python
 # -*- coding: UTF-8 -*-
 ################################################################################
 #                                                                              #
@@ -1090,6 +1090,9 @@ class ArmoryMainWindow(QMainWindow):
          elif OS_LINUX:
             tempDir = '/var/log'
             extraFiles = ['/var/log/Xorg.0.log']
+         elif OS_FREEBSD:
+            tempDir = '/var/log'
+            extraFiles = ['/var/log/Xorg.0.log']
          elif OS_MACOSX:
             tempDir = '/var/log'
             extraFiles = ['/var/log/system.log']
@@ -1387,7 +1390,7 @@ class ArmoryMainWindow(QMainWindow):
       if USE_TESTNET or USE_REGTEST:
          return
 
-      if OS_LINUX:
+      if OS_LINUX or OS_FREEBSD:
          out,err = execAndWait('gconftool-2 --get /desktop/gnome/url-handlers/bitcoin/command')
          out2,err = execAndWait('xdg-mime query default x-scheme-handler/bitcoin')
 
@@ -3850,8 +3853,7 @@ class ArmoryMainWindow(QMainWindow):
    def closeExistingBitcoin(self):
       for proc in psutil.process_iter():
          try:
-            if proc.name().lower() in ['bitcoind.exe','bitcoin-qt.exe',\
-                                        'bitcoind','bitcoin-qt']:
+            if proc.name() in ['bitcoind','bitcoin-qt']:
                killProcess(proc.pid)
                time.sleep(2)
                return
