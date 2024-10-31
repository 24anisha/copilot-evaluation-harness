package com.tiexue.mcp.manage.dto;

public class Paging {

	/**
	 * 当前页
	 */
	private Integer pindex;

	/**
	 * 总页数
	 */
	private Integer ptotalpages;
	
	/**
	 * 总记录数
	 */
	private Integer pcount;
	
	/**
	 * 每一页的记录数
	 */
	private Integer psize;

	public Integer getPindex() {
		return pindex;
	}

	public void setPindex(Integer pindex) {
		this.pindex = pindex;
	}

	public Integer getPtotalpages() {
		return ptotalpages;
	}

	public void setPtotalpages(Integer ptotalpages) {
		this.ptotalpages = ptotalpages;
	}

	public Integer getPcount() {
		return pcount;
	}

	public void setPcount(Integer pcount) {
		this.pcount = pcount;
	}

	public Integer getPsize() {
		return psize;
	}

	public void setPsize(Integer psize) {
		this.psize = psize;
	}
	
	/**
	 * 计算总页数
	 * @return
	 */
	public void calcPtotalpages() {
		if (pcount <= 0 || psize <= 0)
			this.ptotalpages = 0;
		else {
			if (pcount == psize)
				this.ptotalpages = 1;
			else if (pcount % psize == 0)
				this.ptotalpages = pcount / psize;
			else
				this.ptotalpages = pcount / psize + 1;
		}

	}
	
	
}