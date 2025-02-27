/*******************************************************************************
 * Copyright 2014 Miami-Dade County
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/
package org.sharegov.cirm.utils;

import mjson.Json;

public class JsonEvaluator implements Mapping<Object, Boolean>
{
	Json jsonExpr;
	
	public JsonEvaluator(String expression)
	{
		jsonExpr = Json.read(expression);
	}
	
	public Boolean eval(Object x)
	{
		if(jsonExpr.has("oneOf"))
		{
			if(x == null)
			{
				return Boolean.FALSE;
			}	
			for(Object s : jsonExpr.at("oneOf").asList())
			{
				Boolean b = x.toString().equals(s.toString());
				if(b)
					return b;
				
			}
			return Boolean.FALSE;
			
		}else
		{
			return Boolean.FALSE;
		}
	}
}