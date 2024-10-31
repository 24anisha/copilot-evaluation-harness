using System;
using System.Diagnostics;
using System.Management;
using System.Reflection;

namespace Fire
{
    internal class Fire
    {
#if BETA
        public static string Version = "%COMMIT_HASH%/master";
        public static bool Beta = true;
#else
        public static string Version = Assembly.GetEntryAssembly().GetName().Version.ToString();
        public static bool Beta = false;
#endif

        public static void KillProcessAndChildren(int pid)
        {
            if (pid == 0) return;
            var searcher = new ManagementObjectSearcher
                    ("Select * From Win32_Process Where ParentProcessID=" + pid);
            var moc = searcher.Get();
            foreach (var o in moc)
            {
                var mo = (ManagementObject)o;
                KillProcessAndChildren(Convert.ToInt32(mo["ProcessID"]));
            }
            try
            {
                var proc = Process.GetProcessById(pid);
                proc.Kill();
            }
            catch (ArgumentException)
            {
                // Process already exited.
            }
        }
    }
}