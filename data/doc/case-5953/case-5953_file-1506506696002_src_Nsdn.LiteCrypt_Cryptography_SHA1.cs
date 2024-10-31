using System;
using System.IO;
using System.Text;

namespace Nsdn.LiteCrypt
{
    public class SHA1 : Hash
    {
        public override string ComputeHashFromFile(string filePath)
        {
            try
            {
                System.Security.Cryptography.SHA1 sha1 = System.Security.Cryptography.SHA1.Create();
                FileStream fs = File.OpenRead(filePath);
                byte[] outputBytes = sha1.ComputeHash(fs);
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
                System.Security.Cryptography.SHA1 sha1 = System.Security.Cryptography.SHA1.Create();
                byte[] inputBytes = Encoding.UTF8.GetBytes(text);
                byte[] outputBytes = sha1.ComputeHash(inputBytes);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }
    }
}