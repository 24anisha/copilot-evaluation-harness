using System;
using System.IO;
using System.Text;

namespace Nsdn.LiteCrypt
{
    public class SHA512 : Hash
    {
        public override string ComputeHashFromFile(string filePath)
        {
            try
            {
                System.Security.Cryptography.SHA512 sha512 = System.Security.Cryptography.SHA512.Create();
                FileStream fs = File.OpenRead(filePath);
                byte[] outputBytes = sha512.ComputeHash(fs);
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
                System.Security.Cryptography.SHA512 sha512 = System.Security.Cryptography.SHA512.Create();
                byte[] inputBytes = Encoding.UTF8.GetBytes(text);
                byte[] outputBytes = sha512.ComputeHash(inputBytes);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }
    }
}