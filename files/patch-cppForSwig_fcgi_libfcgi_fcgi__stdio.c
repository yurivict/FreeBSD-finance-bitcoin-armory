--- cppForSwig/fcgi/libfcgi/fcgi_stdio.c.orig	2017-04-13 23:40:01 UTC
+++ cppForSwig/fcgi/libfcgi/fcgi_stdio.c
@@ -42,11 +42,11 @@ static const char rcsid[] = "$Id: fcgi_s
 
 extern char **environ;
 
-#ifdef HAVE_FILENO_PROTO
+//#ifdef HAVE_FILENO_PROTO
 #include <stdio.h>
-#else
-extern int fileno(FILE *stream);
-#endif
+//#else
+//extern int fileno(FILE *stream);
+//#endif
 
 extern FILE *fdopen(int fildes, const char *type);
 extern FILE *popen(const char *command, const char *type);
