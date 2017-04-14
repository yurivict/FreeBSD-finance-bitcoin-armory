--- armoryengine/Transaction.py.orig	2017-04-09 23:46:09 UTC
+++ armoryengine/Transaction.py
@@ -16,6 +16,7 @@ from armoryengine.BinaryUnpacker import 
 
 from armoryengine.AsciiSerialize import AsciiSerializable
 
+from armoryengine.MultiSigUtils import *
 
 UNSIGNED_TX_VERSION = 1
 
@@ -2780,7 +2781,6 @@ def PyCreateAndSignTx(ustxiList, dtxoLis
 #
 def PyCreateAndSignTx_old(srcTxOuts, dstAddrsVals):
    # This needs to support multisig. Perhaps the funct should just be moved....
-   from armoryengine.MultiSigUtils import *
 
    newTx = PyTx()
    newTx.version    = 1
