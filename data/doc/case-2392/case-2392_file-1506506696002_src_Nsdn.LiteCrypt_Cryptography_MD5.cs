using System;
using System.IO;
using System.Text;

namespace Nsdn.LiteCrypt
{
    public class MD5 : Hash
    {
        public override string ComputeHashFromFile(string filePath)
        {
            try
            {
                System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create();
                FileStream fs = File.OpenRead(filePath);
                byte[] outputBytes = md5.ComputeHash(fs);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }

        public override string ComputeHashFromText(string text)
        {
            try
            {
                System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create();
                byte[] inputBytes = Encoding.UTF8.GetBytes(text);
                byte[] outputBytes = md5.ComputeHash(inputBytes);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }
    }
}