package com.wangxin.chinesepoker.Card;

/**
 * Created by wangxin on 2017/4/9.
 */

import com.wangxin.chinesepoker.Enum.CardSuit;
import com.wangxin.chinesepoker.Iterator.MyList;


/**
 * 牌用享元模式创建
 */
public class CardFactory {

    private static CardFactory cf;
    private static MyList<Card> cards = new MyList<Card>();

    private CardFactory () {
        int i = 0;
        for(i = 0; i < 13; i++) {
            cards.add(new Card(CardSuit.Spade, i + 3)); // 345678910JQKA
            cards.add(new Card(CardSuit.Heart, i + 3));
            cards.add(new Card(CardSuit.Diamond, i + 3));
            cards.add(new Card(CardSuit.Club, i + 3));
        }
        cards.add(new Card(CardSuit.Joker, 16)); // 小王
        cards.add(new Card(CardSuit.Joker, 17)); // 大王

        // 牌的值：(3,4,5,6,7,8,9,10,11(J),12(Q),13(K),14(A),15(2))
        // 小王 16 大王17
    }

    public static CardFactory getInstance() {
        if(cf == null) {
            synchronized (CardFactory.class) {
                if(cf == null)  // 二次检查
                    cf = new CardFactory();
            }
        }
        return cf;
    }

    public Card get(int index) {
        return cards.get(index);
    }
 }