package com.onlinemathtool.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.json.JSONObject;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
import com.onlinemathtool.helper.Helper;
import com.onlinemathtool.model.GridModel;
 
@Controller
public class Grid {
 
	@RequestMapping("/grid")
	public ModelAndView grid() {
		return new ModelAndView("grid");
	}
	
	@RequestMapping(value = "/grid/data", method = RequestMethod.POST)
	@ResponseBody
	public String getGridResults(@RequestBody String gridData, String selectedColumn, String groupBySumColumn) {
		if(gridData !=null && selectedColumn != null) {
			GridModel gridModelObj = new GridModel();
			Map<String, List<ArrayList<String>>> groupByGridData = Helper.getGroupByRawHashMap(gridData, selectedColumn);
			if(groupByGridData != null) {
				if(groupBySumColumn == null || groupBySumColumn.isEmpty() || groupBySumColumn.equals("undefined")) {
					gridModelObj.setGroupByCountGridModelList(groupByGridData);
				}
				else {
					gridModelObj.setGroupBySumGridModelList(groupByGridData, groupBySumColumn);
				}
				JSONObject jsonObject = Helper.getGroupByJsonArrayResult(gridModelObj.getGroupByGridModelList(),selectedColumn, groupBySumColumn);
				if(jsonObject != null) {
					return jsonObject.toString();
				}
			}
		}
		return null;
	}
}