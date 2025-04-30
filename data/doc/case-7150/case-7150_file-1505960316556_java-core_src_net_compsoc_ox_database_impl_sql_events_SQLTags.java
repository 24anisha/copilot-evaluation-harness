package net.compsoc.ox.database.impl.sql.events;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import net.compsoc.ox.database.iface.events.Tag;
import net.compsoc.ox.database.iface.events.Tags;

public class SQLTags implements Tags {
    
    private static final String Q_SELECT_ALL = "SELECT * FROM web_tags ORDER BY tag_name ASC";
    
    private final PreparedStatement selectAllTags;

    private Map<Integer, Tag> cache;
    private Map<String, Tag> slugCache;
    
    public SQLTags(Connection connection) throws SQLException {
        this.selectAllTags = connection.prepareStatement(Q_SELECT_ALL);
    }

    public synchronized Tag getTagByID(int id) {
        fetchTagsIfNeeded();
        return cache.get(Integer.valueOf(id));
    }

    @Override
    public synchronized Tag getTagBySlug(String slug) {
        fetchTagsIfNeeded();
        return slugCache.get(slug);
    }

    @Override
    public synchronized List<Tag> getTags() {
        fetchTagsIfNeeded();
        return new ArrayList<>(slugCache.values());
    }
    
    private synchronized void fetchTagsIfNeeded(){
        if(cache == null){
            cache = new LinkedHashMap<>();
            slugCache = new LinkedHashMap<>();
            try {
                ResultSet rs = selectAllTags.executeQuery();
                while (rs.next()){
                    SQLTag tag = new SQLTag(rs);
                    cache.put(tag.key(), tag);
                    slugCache.put(tag.slug(), tag);
                }
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }
    
}