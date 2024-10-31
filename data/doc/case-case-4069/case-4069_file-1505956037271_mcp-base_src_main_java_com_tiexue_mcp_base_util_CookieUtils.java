package com.tiexue.mcp.base.util;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;

public class CookieUtils {
	// 日志
	private static Logger logger = Logger.getLogger(CookieUtils.class);
	public static void addcookie(String cookieName,int maxAge,HttpServletResponse response,String value){
		try {
			// todo:生成登录cookie写到客户端
			Cookie token_cookie = new Cookie(cookieName, value); // 创建一个Cookie对象，并将用户名保存到Cookie对象中
			token_cookie.setMaxAge(maxAge); // 设置Cookie的过期之前的时间，单位为秒
			token_cookie.setPath("/");
			response.addCookie(token_cookie); // 通过response的addCookie()方法将此Cookie对象
		} catch (Exception e) {
			// TODO: handle exception
			logger.error(" addcookie error:"+e.getMessage());
			e.printStackTrace();
		}
		
	}
}