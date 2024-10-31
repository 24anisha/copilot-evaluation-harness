package com.tiexue.mcp.core.dto;

import java.util.Comparator;

public class McpSettlementDetailDto implements Comparable {

	/**
	 * 月度
	 */
	private String monthly;
	/**
	 * 消费金额
	 */
	private float consume;
	/**
	 * 结算金额
	 */
	private Integer divideconsume;

	
	private Integer cpId;
	private Integer cpBId;
	private String bookName;
	/**
	 * 查询开始时间
	 */
	private String startTime;
	/**
	 * 查询结束时间
	 */
	private String endTime;
	public String getMonthly() {
		return monthly;
	}

	public void setMonthly(String monthly) {
		this.monthly = monthly;
	}

	public float getConsume() {
		return consume;
	}

	public void setConsume(float consume) {
		this.consume = consume;
	}

	public Integer getDivideconsume() {
		return divideconsume;
	}

	public void setDivideconsume(Integer divideconsume) {
		this.divideconsume = divideconsume;
	}
	public Integer getCpId() {
		return cpId;
	}

	public void setCpId(Integer cpId) {
		this.cpId = cpId;
	}

	public Integer getCpBId() {
		return cpBId;
	}

	public void setCpBId(Integer cpBId) {
		this.cpBId = cpBId;
	}

	public String getBookName() {
		return bookName;
	}

	public void setBookName(String bookName) {
		this.bookName = bookName;
	}
	
	public String getStartTime() {
		return startTime;
	}

	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

	public String getEndTime() {
		return endTime;
	}

	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	/**
	 * 实现排序
	 */
	@Override
	public int compareTo(Object o){
		McpSettlementDetailDto mcpSettlementDetailDto=(McpSettlementDetailDto)o;
		Integer newConsume=(int)mcpSettlementDetailDto.getConsume();
		Integer temp=((int)this.consume);
		return temp.compareTo(newConsume);
	}
}