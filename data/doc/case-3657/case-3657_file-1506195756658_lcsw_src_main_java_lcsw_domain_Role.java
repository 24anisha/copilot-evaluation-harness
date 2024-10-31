package lcsw.domain;

import java.sql.Timestamp;

import com.baomidou.mybatisplus.annotations.TableField;
import com.baomidou.mybatisplus.annotations.TableId;
import com.baomidou.mybatisplus.annotations.TableName;

@TableName(value="tbl_role")
public class Role {
	private static final long serialVersionUID = 1L;
	
	@TableId("role_id")
	private Integer roleId;
	
	@TableField("role_name")
	private String roleName;
	
	@TableField("creator_id")
	private Integer creatorId;
	
	@TableField("create_time")
	private Timestamp createTime;
	
	@TableField("role_count")
	private Integer roleCount;
	
	@TableField("remark")
	private String remark;

	public Integer getRoleId() {
		return roleId;
	}

	public void setRoleId(Integer roleId) {
		this.roleId = roleId;
	}

	public String getRoleName() {
		return roleName;
	}

	public void setRoleName(String roleName) {
		this.roleName = roleName;
	}

	public Integer getCreatorId() {
		return creatorId;
	}

	public void setCreatorId(Integer creatorId) {
		this.creatorId = creatorId;
	}

	public Timestamp getCreateTime() {
		return createTime;
	}

	public void setCreateTime(Timestamp createTime) {
		this.createTime = createTime;
	}

	public Integer getRoleCount() {
		return roleCount;
	}

	public void setRoleCount(Integer roleCount) {
		this.roleCount = roleCount;
	}

	public String getRemark() {
		return remark;
	}

	public void setRemark(String remark) {
		this.remark = remark;
	}

	@Override
	public String toString() {
		return "Role [roleId=" + roleId + ", roleName=" + roleName + ", creatorId=" + creatorId + ", createTime="
				+ createTime + ", roleCount=" + roleCount + ", remark=" + remark + "]";
	}

	@Override
	public boolean equals(Object obj) {
		Role r = (Role) obj;
		if(getRoleId().equals(r.getRoleId())){
			return true;
		}
		return false;
	}
}