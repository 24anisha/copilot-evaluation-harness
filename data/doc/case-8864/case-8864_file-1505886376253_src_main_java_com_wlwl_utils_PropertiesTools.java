package com.wlwl.utils;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

/**
 * Properties 工具类 负责加载配置文件信息
 * 
 * @author lion
 * 
 */
public class PropertiesTools {

	/**
	 * 加载配置文件信息,当从指定路径加载不到配置文件时,则使用内部的配置文件
	 * 
	 * @param fileName
	 *            文件名称
	 * @param fileDir
	 *            文件路径
	 * @return
	 * @throws IOException
	 */
	public static Properties loadProperties(String fileName, String fileDir)
			throws IOException {
		Properties prop = new Properties();
		// 加载配置文件
		// 默认使用外部配置文件
		// 外部文件加载不到的情况下,使用内部的配置
		File propFile = new File(fileDir + "/" + fileName);
		if (propFile.exists()) {
			prop.load(new FileInputStream(propFile));
			System.out.println("读取 "+fileName+" 外部配置文件成功!");
		} else {
			prop.load(PropertiesTools.class.getClassLoader()
					.getResourceAsStream(fileName));
			System.out.println("读取 "+fileName+" 内部配置文件成功!");
		}
		return prop;
	}
}