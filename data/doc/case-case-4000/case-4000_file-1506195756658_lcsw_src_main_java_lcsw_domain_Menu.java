package lcsw.domain;

import com.baomidou.mybatisplus.annotations.TableField;
import com.baomidou.mybatisplus.annotations.TableId;
import com.baomidou.mybatisplus.annotations.TableName;

@TableName("tbl_menu")
public class Menu {
	
	@TableId("menu_id")
	private Integer menuId;
	
	@TableField("menu_name")
	private String menuName;
	
	@TableField("parent_id")
	private Integer parentId;
	
	@TableField("perms")
	private String perms;
	
	@TableField("type")
	private Integer type;
	
	@TableField("group_name")
	private String groupName;

	public Integer getMenuId() {
		return menuId;
	}

	public void setMenuId(Integer menuId) {
		this.menuId = menuId;
	}

	public String getMenuName() {
		return menuName;
	}

	public void setMenuName(String menuName) {
		this.menuName = menuName;
	}

	public Integer getParentId() {
		return parentId;
	}

	public void setParentId(Integer parentId) {
		this.parentId = parentId;
	}

	public String getPerms() {
		return perms;
	}

	public void setPerms(String perms) {
		this.perms = perms;
	}

	public Integer getType() {
		return type;
	}

	public void setType(Integer type) {
		this.type = type;
	}

	public String getGroupName() {
		return groupName;
	}

	public void setGroupName(String groupName) {
		this.groupName = groupName;
	}

	@Override
	public String toString() {
		return "Menu [menuId=" + menuId + ", menuName=" + menuName + ", parentId=" + parentId + ", perms=" + perms
				+ ", type=" + type + ", groupName=" + groupName + "]";
	}

	@Override
	public boolean equals(Object obj) {
		Menu m = (Menu) obj;
		if(getMenuId().equals(m.getMenuId())){
			return true;
		}
		return false;
	}
	
	
}