--- armoryengine/ArmoryUtils.py.orig	2017-04-09 23:46:09 UTC
+++ armoryengine/ArmoryUtils.py
@@ -133,6 +133,7 @@ parser.set_defaults(enableDetSign=True)
 opsys = platform.system()
 OS_WINDOWS = 'win32'  in opsys.lower() or 'windows' in opsys.lower()
 OS_LINUX   = 'nix'    in opsys.lower() or 'nux'     in opsys.lower()
+OS_FREEBSD = 'freebsd' in opsys.lower()
 OS_MACOSX  = 'darwin' in opsys.lower() or 'osx'     in opsys.lower()
 
 # Pre-10.9 OS X sometimes passes a process serial number as -psn_0_xxxxxx. Nuke!
@@ -336,6 +337,14 @@ elif OS_LINUX:
    ARMORY_HOME_DIR = os.path.join(USER_HOME_DIR, '.armory', SUBDIR)
    BLKFILE_DIR     = os.path.join(BTC_HOME_DIR, 'blocks')
    BLKFILE_1stFILE = os.path.join(BLKFILE_DIR, 'blk00000.dat')
+elif OS_FREEBSD:
+   OS_NAME         = 'FreeBSD'
+   OS_VARIANT      = ('FreeBSD',platform.release(), '') # tuple (platform,version,id)
+   USER_HOME_DIR   = os.getenv('HOME')
+   BTC_HOME_DIR    = os.path.join(USER_HOME_DIR, '.bitcoin', SUBDIR)
+   ARMORY_HOME_DIR = os.path.join(USER_HOME_DIR, '.armory', SUBDIR)
+   BLKFILE_DIR     = os.path.join(BTC_HOME_DIR, 'blocks')
+   BLKFILE_1stFILE = os.path.join(BLKFILE_DIR, 'blk00000.dat')
 elif OS_MACOSX:
    platform.mac_ver()
    OS_NAME         = 'MacOSX'
@@ -739,7 +748,7 @@ def killProcessTree(pid):
    else:
       from subprocess_win import Popen, PIPE
 
-   if not OS_LINUX:
+   if not OS_LINUX and not OS_FREEBSD:
       for child in psutil.Process(pid).get_children():
          killProcess(child.pid)
    else:
@@ -1137,7 +1146,7 @@ except:
    LOGCRIT('   in the current directory (or added to the PATH)')
    LOGCRIT('   Specifically, you need:')
    LOGCRIT('       CppBlockUtils.py     and')
-   if OS_LINUX or OS_MACOSX:
+   if OS_LINUX or OS_FREEBSD or OS_MACOSX:
       LOGCRIT('       _CppBlockUtils.so')
    elif OS_WINDOWS:
       LOGCRIT('       _CppBlockUtils.pyd')
@@ -1171,6 +1180,11 @@ def GetSystemDetails():
             out.CpuStr = line.split(':')[1].strip()
             break
 
+   elif OS_FREEBSD:
+      # Get total RAM
+      out.Memory = long(subprocess_check_output(['sysctl','-n','hw.physmem']))
+      ## Get CPU name
+      out.CpuStr = subprocess_check_output(['sysctl','-n','hw.model'])
 
    elif OS_WINDOWS:
       import ctypes
@@ -1691,7 +1705,7 @@ except:
    LOGCRIT('   in the current directory (or added to the PATH)')
    LOGCRIT('   Specifically, you need:')
    LOGCRIT('       CppBlockUtils.py     and')
-   if OS_LINUX or OS_MACOSX:
+   if OS_LINUX or OS_FREEBSD or OS_MACOSX:
       LOGCRIT('       _CppBlockUtils.so')
    elif OS_WINDOWS:
       LOGCRIT('       _CppBlockUtils.pyd')
