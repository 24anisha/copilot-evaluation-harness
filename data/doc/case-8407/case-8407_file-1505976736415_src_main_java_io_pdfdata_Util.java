package io.pdfdata;

import sun.misc.IOUtils;

import java.io.IOException;
import java.io.InputStream;
import java.util.*;

/**
 * @nodoc
 */
public class Util {

    public static <T> Set<T> setFrom (T... ts) {
        HashSet<T> set = new HashSet<>();
        if (ts == null) return set;
        for (T x : ts) set.add(x);
        return set;
    }
    public static <T> Set<T> setFrom (Collection<T> ts) {
        return ts == null ? new HashSet<>() : ((ts instanceof Set) ? (Set)ts : new HashSet<>(ts));
    }
    public static <T> Set<T> union (Set<T>... sets) {
        HashSet<T> union = new HashSet<>();
        for (Set<T> set : sets) {
            for (T x : set) union.add(x);
        }
        return union;
    }


    static Map<String, Object> kvmap(Object... kvs) {
        if (kvs.length % 2 > 0)
            throw new IllegalArgumentException("Must provide even number of arguments to `kvmap`");

        Map<String, Object> m = new HashMap<>();
        for (int i = 0; i < kvs.length; i += 2) {
            if (kvs[i + 1] != null) m.put(String.valueOf(kvs[i]), kvs[i + 1]);
        }

        return m;
    }

    public static byte[] readBytes(InputStream in) throws IOException {
        return IOUtils.readFully(in, -1, false);
    }

    public static String readString(InputStream input) throws IOException {
        try (InputStream is = input) {
            return new Scanner(is, Network.CHARSET_NAME).useDelimiter("\\A").next();
        }
    }
}