/*
 * SimpleMapEntry
 * 
 * Created on 05.11.2003 Copyright (c) 2003 Statistisches Bundesamt und IVU Traffic Technologies AG
 */
package de.ivu.wahl.util;

import java.util.Map;

/**
 * @author cos@ivu.de, IVU Traffic Technologies AG
 * @param <K> Datentyp f�r Key
 * @param <V> Datentyp f�r Value
 */
public class SimpleMapEntry<K, V> implements Map.Entry<K, V> {
  K _key;
  V _value;

  public SimpleMapEntry(K key, V value) {
    _key = key;
    _value = value;
  }

  @Override
  public int hashCode() {
    return _key.hashCode();
  }

  public K getKey() {
    return _key;
  }

  public V getValue() {
    return _value;
  }

  @Override
  public boolean equals(Object o) {
    SimpleMapEntry<?, ?> other = (SimpleMapEntry<?, ?>) o;
    return _key.equals(other._key)
        && (_value == null ? other._value == null : _value.equals(other._value));
  }

  public V setValue(V value) {
    try {
      return _value;
    } finally {
      _value = value;
    }
  }
}