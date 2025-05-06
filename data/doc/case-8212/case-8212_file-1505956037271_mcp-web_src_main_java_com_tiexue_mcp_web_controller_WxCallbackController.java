package com.tiexue.mcp.web.controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.util.Arrays;

import javax.annotation.Resource;
import javax.servlet.ServletInputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.tiexue.mcp.core.entity.WxConstants;
import com.tiexue.mcp.core.service.IWxCallbackService;

@Controller
@RequestMapping("wxcallback")
public class WxCallbackController {
	// 日志
	private Logger logger = Logger.getLogger(WxCallbackController.class);

	@Resource
	IWxCallbackService wxCallbackService;

	@RequestMapping("check")
	public void check(HttpServletRequest request, HttpServletResponse response) {
		try {
			String signature = request.getParameter("signature");
			String timestamp = request.getParameter("timestamp");
			String nonce = request.getParameter("nonce");
			String echostr = request.getParameter("echostr");

			boolean ret = wxCallbackService.checkSignature(signature, timestamp, nonce);
			if (ret == true) {
				response.getWriter().print(echostr);
			} else {
				response.getWriter().print("error");
			}
		} catch (Exception e) {
			// TODO: handle exception
			try {
				response.getWriter().print(e.getMessage());
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
	}

}