package org.organicdesign.fp.collections;

import java.util.AbstractMap;
import java.util.Map;

/**
 Implements equals() and hashCode() methods compatible with java.util.Map (which ignores order)
 to make defining unmod Maps easier.  Inherits hashCode() and toString() from
 AbstractUnmodIterable.
 */
public abstract class AbstractUnmodMap<K,V>
        extends AbstractUnmodIterable<UnmodMap.UnEntry<K,V>>
        implements UnmodMap<K,V> {

    /**
     When comparing against a SortedMap, this is correct and O(n) fast, but BEWARE! It is also
     Compatible with {@link AbstractMap#equals(Object)} which unfortunately means equality as defined by this method
     (and java.util.AbstractMap) is not commutative when comparing ordered and unordered maps (it is
     also O(n log n) slow).  The Equator defined by this class prevents comparison with unordered
     Maps.
     */
    @Override public boolean equals(Object other) {
        if (this == other) { return true; }
        if (!(other instanceof Map)) { return false; }

        Map<?, ?> that = (Map<?, ?>) other;
        if (that.size() != size()) { return false; }

        try {
            for (Entry<K, V> e : this) {
                K key = e.getKey();
                V value = e.getValue();
                if (value == null) {
                    if (!(that.get(key) == null && that.containsKey(key))) {
                        return false;
                    }
                } else {
                    if (!value.equals(that.get(key))) {
                        return false;
                    }
                }
            }
        } catch (ClassCastException | NullPointerException unused) {
            return false;
        }
        return true;
    }
}
