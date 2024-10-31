package com.gwell.view.library;

/**
 * Created by dansesshou on 17/5/4.
 */

public class BaseSelectItem<E> {
    private String str;
    private E mark;

    public BaseSelectItem() {
    }

    public BaseSelectItem(String str, E mark) {
        this.str = str;
        this.mark = mark;
    }

    public E getMark() {
        return mark;
    }

    public void setMark(E mark) {
        this.mark = mark;
    }

    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        BaseSelectItem that = (BaseSelectItem) o;

        if (mark != that.mark) return false;
        return str != null ? str.equals(that.str) : that.str == null;

    }

    @Override
    public String toString() {
        return "BaseSelectItem{" +
                "str='" + str + '\'' +
                ", mark=" + mark +
                '}';
    }

}