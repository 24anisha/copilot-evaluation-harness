package com.tiexue.mcp.task.weixinsync;

import org.apache.log4j.Logger;

import com.tiexue.mcp.core.entity.WxConstants;
import com.tiexue.mcp.core.weixin.WcWxConstant;

import weixin.popular.support.TicketManager;
import weixin.popular.support.TokenManager;

public class WxAppInit {
	private static Logger logger=Logger.getLogger(WxAppInit.class);
	private static WxAppInit wxAppInit;
	/**
	 * 单例实例化时执行一次
	 */
	private WxAppInit(){
		logger.error("启动获取AccessToken");
		//五彩读书城获取token
		// TicketManager 依赖 TokenManager，确保TokenManager.init 先被调用
		TokenManager.init(WxConstants.WxAppId, WxConstants.WxAppSecret);
		// 睡眠一定时间后启动
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		TicketManager.init(WxConstants.WxAppId);
		//五彩读书网获取token
		TokenManager.init(WcWxConstant.wxAppId, WcWxConstant.wxAppSecret);
		// 睡眠一定时间后启动
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		TicketManager.init(WcWxConstant.wxAppId);
	}
	
	/**
	 * 初始化：开始获取微信公共号的accessToken
	 * 单例
	 * @return
	 */
	public static WxAppInit getInstance(){
		if(wxAppInit==null){
			synchronized (WxAppInit.class) {
				if(wxAppInit==null){
					return new WxAppInit();
				}
			}
		}
		return wxAppInit;
	}
	
	/**
	 * 获取公众号的accesstoken
	 * @param appid
	 * @return
	 */
	public static String getAccessToken(String appid){
		return TokenManager.getToken(appid);
	}
}