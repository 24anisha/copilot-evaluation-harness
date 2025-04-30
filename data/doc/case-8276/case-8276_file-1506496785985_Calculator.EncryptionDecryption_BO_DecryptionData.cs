using Calculator.EncryptionDecryption.Interfaces;
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace Calculator.EncryptionDecryption.BO
{
    public class DecryptionData : IEncryptionManager<string>
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

            byte[] cipherTextBytes = Convert.FromBase64String(value);

            var password = new PasswordDeriveBytes(passPhrase, saltValueBytes, hashAlgorithm, passwordIterations);

            byte[] keyBytes = password.GetBytes(keySize / 8);

            var symmetricKey = new RijndaelManaged();

            symmetricKey.Mode = CipherMode.CBC;
            symmetricKey.Padding = PaddingMode.Zeros;
            var decryptor = symmetricKey.CreateDecryptor(keyBytes, initVectorBytes);

            using (var memoryStream = new MemoryStream(cipherTextBytes))
            using (var cryptoStream = new CryptoStream(memoryStream, decryptor, CryptoStreamMode.Read))
            {
                byte[] plainTextBytes = new byte[cipherTextBytes.Length];

                int decryptedByteCount = cryptoStream.Read(plainTextBytes, 0, plainTextBytes.Length);

                string plainText = Encoding.UTF8.GetString(plainTextBytes, 0, decryptedByteCount);
                return plainText.Replace("\0", string.Empty);
            }
        }
    }
}