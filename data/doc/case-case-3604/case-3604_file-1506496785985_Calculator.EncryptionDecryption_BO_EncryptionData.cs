using Calculator.EncryptionDecryption.Interfaces;
using System;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

namespace Calculator.EncryptionDecryption.BO
{
    public class EncryptionData : IEncryptionManager<string>
    {
        public string Manage(string value)
        {
            const string passPhrase = "test";
            const string saltValue = "s@1tValue";
            const string hashAlgorithm = "SHA1";
            const int passwordIterations = 2;
            const string initVector = "@1B2c3D4e5F6g7H8";
            const int keySize = 256;

            byte[] initVectorBytes = Encoding.ASCII.GetBytes(initVector);
            byte[] saltValueBytes = Encoding.ASCII.GetBytes(saltValue);

            byte[] plainTextBytes = Encoding.UTF8.GetBytes(value);

            var password = new PasswordDeriveBytes(passPhrase, saltValueBytes, hashAlgorithm, passwordIterations);

            byte[] keyBytes = password.GetBytes(keySize / 8);

            var symmetricKey = new RijndaelManaged();

            symmetricKey.Mode = CipherMode.CBC;
            symmetricKey.Padding = PaddingMode.Zeros;
            var encryptor = symmetricKey.CreateEncryptor(keyBytes, initVectorBytes);

            using (var memoryStream = new MemoryStream())
            using (var cryptoStream = new CryptoStream(memoryStream, encryptor, CryptoStreamMode.Write))
            {
                cryptoStream.Write(plainTextBytes, 0, plainTextBytes.Length);

                cryptoStream.FlushFinalBlock();

                byte[] cipherTextBytes = memoryStream.ToArray();
                var cipherText = Convert.ToBase64String(cipherTextBytes);

                return cipherText;
            }
        }
    }
}