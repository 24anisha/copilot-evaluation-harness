package com.ref.base.util;

import com.ref.base.exception.BusinessException;
import com.ref.base.constant.CommonConstant.ErrorCode;
import org.apache.commons.lang3.StringUtils;
import sun.misc.BASE64Encoder;

import java.security.MessageDigest;

/**
 * Created by perxin on 2017/3/28.
 */
public class MD5Util {

    public static String encrypt(String str) {
        if (StringUtils.isBlank(str)) {
            return null;
        }
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("MD5");
            BASE64Encoder base64Encoder = new BASE64Encoder();
            String newStr = base64Encoder.encode(md.digest(str.getBytes("utf-8")));
            return newStr;
        }catch (Exception e) {
            throw new BusinessException(ErrorCode.ERROR_CODE_CUSTOM, "md5 encrypt error!");
        }
    }
}