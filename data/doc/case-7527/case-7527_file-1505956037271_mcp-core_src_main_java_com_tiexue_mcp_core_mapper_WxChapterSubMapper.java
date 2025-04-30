package com.tiexue.mcp.core.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import com.tiexue.mcp.core.entity.WxChapterSub;

public interface WxChapterSubMapper {
    @Insert({
        "insert into wxchaptersub (Id, Content)",
        "values (#{id,jdbcType=INTEGER}, #{content,jdbcType=LONGVARCHAR})"
    })
    int insert(WxChapterSub record);

    int insertSelective(WxChapterSub record);
    
    @Update({" update wxchaptersub set ",
    	" Content=#{content,jdbcType=LONGVARCHAR} ",
    	" where id=#{id,jdbcType=INTEGER}"})
    int updateByBookId(WxChapterSub record);
    
    //获取章节内容
    @Select({" select Id,Content from wxchaptersub where id=#{id}"})
    @ResultMap("AllResultMap")
    WxChapterSub selectByChapterId(@Param("id")Integer id);
    
    
    /**
     * 插入到wxChapterSub
     * @param id
     * @param uniqueflag
     * @return
     */
    @Insert({
    	"INSERT INTO wxchaptersub(Id, Content)",
    	"SELECT #{wxChapterId},Content",
    	"FROM McpChapter WHERE Id =#{mcpChapterId} ",
    	"AND NOT EXISTS (SELECT id FROM wxchaptersub WHERE id=#{wxChapterId});",
    })
    int insertToWxChapterSub(@Param("mcpChapterId")Integer mcpChapterId,@Param("wxChapterId")int wxChapterId);  
    @Update({
    	"UPDATE wxchaptersub a ",
		"INNER JOIN wxchapter c ON a.Id=c.Id",
		"INNER JOIN McpChapter b ON b.UniqueFlag=c.UniqueFlag ",
		"SET ",
		"a.Content=b.Content",
		"WHERE a.Id=#{wxChapterId} ",
    })
    /**
     * 根据bookId批量章节内容
     * @param id
     * @param uniqueflag
     * @return
     */
    int updateToWxChapterSub(@Param("wxChapterId")Integer wxChapterId,@Param("uniqueflag")String uniqueflag);
}