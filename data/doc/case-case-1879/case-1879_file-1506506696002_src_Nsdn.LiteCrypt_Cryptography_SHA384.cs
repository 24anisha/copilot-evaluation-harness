using System;
using System.IO;
using System.Text;

namespace Nsdn.LiteCrypt
{
    public class SHA384 : Hash
    {
        public override string ComputeHashFromFile(string filePath)
        {
            try
            {
                System.Security.Cryptography.SHA384 sha384 = System.Security.Cryptography.SHA384.Create();
                FileStream fs = File.OpenRead(filePath);
                byte[] outputBytes = sha384.ComputeHash(fs);
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
                System.Security.Cryptography.SHA384 sha384 = System.Security.Cryptography.SHA384.Create();
                byte[] inputBytes = Encoding.UTF8.GetBytes(text);
                byte[] outputBytes = sha384.ComputeHash(inputBytes);
                return BitConverter.ToString(outputBytes).Replace("-", "").ToLower();
            }
            catch (Exception e)
            {
                return "\nERROR: " + e.Message;
            }
        }
    }
}