using System;
using System.IO;
using System.Text;

namespace Nsdn.LiteCrypt
{
    public class SHA256 : Hash
    {
        public override string ComputeHashFromFile(string filePath)
        {
            try
            {
                System.Security.Cryptography.SHA256 sha256 = System.Security.Cryptography.SHA256.Create();
                FileStream fs = File.OpenRead(filePath);
                byte[] outputBytes = sha256.ComputeHash(fs);
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
                System.Security.Cryptography.SHA256 sha256 = System.Security.Cryptography.SHA256.Create();
                byte[] inputBytes = Encoding.UTF8.GetBytes(text);
                byte[] outputBytes = sha256.ComputeHash(inputBytes);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }
    }
}