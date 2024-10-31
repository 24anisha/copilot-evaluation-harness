package com.pasodoff.hcp.badapple.util;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Base64;

/**
 * Created by aaron on 15/06/2017.
 */
public class Encryption {

    //private String key = "Bar12345Bar12345"; // 128 bit key
    // TODO: Hard coded encryption key
    private static String key = "KeyOfaKeyOfaKeya"; // 128 bit key
    // TODO: Hard coded initialization vector
    private static String initVector = "VectorMeVectorMe"; // 16 bytes IV

    public static String encrypt(String value) {
        try {
            IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
            SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");

            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
            cipher.init(Cipher.ENCRYPT_MODE, skeySpec, iv);

            byte[] encrypted = cipher.doFinal(value.getBytes());
            return Base64.encodeBase64String(encrypted);
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        return null;
    }

    public static String decrypt(String encrypted) {
        if(encrypted.startsWith("ENC:")){
            encrypted = encrypted.substring(3,encrypted.length());
        }
        try {
            IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
            SecretKeySpec skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");

            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
            cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv);

            byte[] original = cipher.doFinal(Base64.decodeBase64(encrypted));

            return new String(original);
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        return null;
    }

}