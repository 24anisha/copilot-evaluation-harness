package com.automan.framework.util;

import java.io.FileReader;
import java.util.List;
import java.util.Map;

import com.esotericsoftware.yamlbeans.YamlReader;

public class YamlGather {
	public String fileName;
	
	public String getFileName() {
		return fileName;
	}

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}

	public YamlGather(){
		
	}
	
	public Map readYaml(String fileName){
		try{
//    		YamlReader reader = new YamlReader(new FileReader("/Users/yingchen/Documents/workspace/framework/src/main/java/com/automan/framework/index.yml"));
			YamlReader reader = new YamlReader(new FileReader(fileName));
    		Map map = (Map) reader.read();
    		return map;
    	}catch(Exception e){
    		e.printStackTrace();
    		return null;
    	}
	}
	

	
	
}