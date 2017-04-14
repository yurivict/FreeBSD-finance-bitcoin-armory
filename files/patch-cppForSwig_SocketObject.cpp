--- cppForSwig/SocketObject.cpp.orig	2017-04-09 23:46:09 UTC
+++ cppForSwig/SocketObject.cpp
@@ -9,6 +9,7 @@
 #include "SocketObject.h"
 #include <cstring>
 #include <stdexcept>
+#include <netinet/in.h>
 
 ///////////////////////////////////////////////////////////////////////////////
 //
