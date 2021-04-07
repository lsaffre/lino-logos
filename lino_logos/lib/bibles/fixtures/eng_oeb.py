# -*- coding: utf-8 -*-
# Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""
Loads the Open English Bible
"""

from lino_logos.lib.bibles.loader import *

def objects():

    yield edition("eng","OEB", "Open English Bible")

    set_book("matthew")

    # yield section("The Good News According to Matthew")

    yield section("The Birth, Parentage and Infancy")

    yield verses(1,"""
1 A genealogy of Jesus Christ, a descendant of David and Abraham.
2 Abraham was the father of Isaac, Isaac of Jacob, Jacob of Judah and his brothers,
3 Judah of Perez and Zerah, whose mother was Tamar, Perez of Hezron, Hezron of Aram,
4 Aram of Aminadab, Aminadab of Nahshon, Nahshon of Salmon,
5 Salmon of Boaz, whose mother was Rahab, Boaz of Obed, whose mother was Ruth, Obed of Jesse,
6 Jesse of David the King. David was the father of Solomon, whose mother was Uriah's widow,
7 Solomon of Rehoboam, Rehoboam of Abijah, Abijah of Asa,
8 Asa of Jehoshaphat, Jehoshaphat of Joram, Joram of Uzziah,
9 Uzziah of Jotham, Jotham of Ahaz, Ahaz of Hezekiah,
10 Hezekiah of Manasseh, Manasseh of Amon, Amon of Josiah,
11 Josiah of Jechoniah and his brothers, at the time of the Exile to Babylon.
12 After the Exile to Babylon — Jechoniah was the father of Salathiel, Salathiel of Zerubbabel,
13 Zerubbabel of Abiud, Abiud of Eliakim, Eliakim of Azor,
14 Azor of Zadok, Zadok of Achim, Achim of Eliud,
15 Eliud of Eleazar, Eleazar of Matthan, Matthan of Jacob,
16 Jacob of Joseph, the husband of Mary, who was the mother of Jesus, who is called ‘Christ’.
17 So the whole number of generations from Abraham to David is fourteen; from David to the Exile to Babylon fourteen; and from the Exile to Babylon to the Christ fourteen.
18 This is how Jesus Christ was born:
His mother Mary was engaged to Joseph, but, before the marriage took place, she found herself to be pregnant by the power of the Holy Spirit.
19 Her husband, Joseph, was a just man and, since he did not want to disgrace her publicly, he resolved to put an end to their engagement privately.
20 He had been thinking this over, when an angel of the Lord appeared to him in a dream.
“Joseph, son of David,” the angel said, “do not be afraid to take Mary for your wife, for her child has been conceived by the power of the Holy Spirit.
21 She will give birth to a son; name him Jesus, for he will save his people from their sins.”
22 All this happened in fulfillment of these words of the Lord in the prophet, where he says —
23 ‘The virgin will conceive and will give birth to a son, and they will give him the name Immanuel’ — a word which means ‘God is with us.’
24 When Joseph woke up, he did as the angel of the Lord had directed him.
25 He made Mary his wife, but they did not sleep together before the birth of her son; and to this son he gave the name Jesus.
    """)

    yield verses(2,"""
1 After the birth of Jesus at Bethlehem in Judea, in the reign of King Herod, some astrologers from the East arrived in Jerusalem, asking:
2 “Where is the newborn king of the Jews? For we saw his star in the east, and have come to worship him.”
3 When King Herod heard of this, he was much troubled, and so too was all Jerusalem.
4 He called together all the chief priests and teachers of the Law in the nation, and questioned them as to where the Christ was to be born.


5 “At Bethlehem in Judea,” was their answer, “for it is said in the prophet —


6 ‘And you, Bethlehem in Judah's land,
     are in no way least among the chief cities of Judah,
   for out of you will come a ruler —
     who will shepherd my people Israel.’”


7 Then Herod secretly sent for the astrologers. He found out from them the time of the appearance of the star.
8 Sending them to Bethlehem he said: “Go and make a careful search for the child. When you have found him, bring word back to me, so that I, too, can go and worship him.”
9 The astrologers heard what the king had to say, and then continued their journey. The star which they had seen in the east led them on, until it reached and stood over the place where the child was.
10 At the sight of the star they were filled with joy.
11 Entering the house, they saw the child with his mother, Mary, and fell at his feet and worshiped him. Then they opened their treasure chests, and offered to the child presents of gold, frankincense, and myrrh.
12 But afterward, having been warned in a dream not to go back to Herod, they returned to their own country by another road.


13 After they had left, an angel of the Lord appeared to Joseph in a dream, and said:

“Get up, take the child and his mother, and seek refuge in Egypt; and stay there until I tell you to return, for Herod is about to search for the child, to put him to death.”
14 Joseph woke up, and taking the child and his mother by night, went into Egypt,
15 and there he stayed until Herod's death; in fulfillment of these words of the Lord in the prophet, where he says —

   ‘Out of Egypt I called my Son.’


16 When Herod found out that the astrologers had tricked him, he flew into a rage. He sent and put to death all the boys in Bethlehem and the whole of that region, who were two years old or under, guided by the time which he had learned from the astrologers.
17 Then were fulfilled these words spoken in the prophet Jeremiah, where he says —


18 ‘A voice was heard in Ramah,
     weeping and mourning loudly;
   Rachel, weeping for her children,
     refusing all comfort for they were dead.’


19 But, on the death of Herod, an angel of the Lord appeared in a dream to Joseph in Egypt, and said:
20 “Get up, take the child and his mother, and go into the Land of Israel, for those who sought to take the child's life are dead.”
21 He woke up, and taking the child and his mother, went into the Land of Israel.
22 But, hearing that Archelaus had succeeded his father Herod as king of Judea, he was afraid to go back there; and having been warned in a dream, he went into the part of the country called Galilee.
23 There he settled in the town of Nazareth, in fulfillment of these words in the prophets — ‘He will be called a Nazarene.’
    """)
    yield section("The Birth, Parentage and Infancy")

    yield verses(1,"""
1 A genealogy of Jesus Christ, a descendant of David and Abraham.
2 Abraham was the father of Isaac, Isaac of Jacob, Jacob of Judah and his brothers,
3 Judah of Perez and Zerah, whose mother was Tamar, Perez of Hezron, Hezron of Aram,
4 Aram of Aminadab, Aminadab of Nahshon, Nahshon of Salmon,
5 Salmon of Boaz, whose mother was Rahab, Boaz of Obed, whose mother was Ruth, Obed of Jesse,
6 Jesse of David the King. David was the father of Solomon, whose mother was Uriah's widow,
7 Solomon of Rehoboam, Rehoboam of Abijah, Abijah of Asa,
8 Asa of Jehoshaphat, Jehoshaphat of Joram, Joram of Uzziah,
9 Uzziah of Jotham, Jotham of Ahaz, Ahaz of Hezekiah,
10 Hezekiah of Manasseh, Manasseh of Amon, Amon of Josiah,
11 Josiah of Jechoniah and his brothers, at the time of the Exile to Babylon.
12 After the Exile to Babylon — Jechoniah was the father of Salathiel, Salathiel of Zerubbabel,
13 Zerubbabel of Abiud, Abiud of Eliakim, Eliakim of Azor,
14 Azor of Zadok, Zadok of Achim, Achim of Eliud,
15 Eliud of Eleazar, Eleazar of Matthan, Matthan of Jacob,
16 Jacob of Joseph, the husband of Mary, who was the mother of Jesus, who is called ‘Christ’.
17 So the whole number of generations from Abraham to David is fourteen; from David to the Exile to Babylon fourteen; and from the Exile to Babylon to the Christ fourteen.
18 This is how Jesus Christ was born:
His mother Mary was engaged to Joseph, but, before the marriage took place, she found herself to be pregnant by the power of the Holy Spirit.
19 Her husband, Joseph, was a just man and, since he did not want to disgrace her publicly, he resolved to put an end to their engagement privately.
20 He had been thinking this over, when an angel of the Lord appeared to him in a dream.
“Joseph, son of David,” the angel said, “do not be afraid to take Mary for your wife, for her child has been conceived by the power of the Holy Spirit.
21 She will give birth to a son; name him Jesus, for he will save his people from their sins.”
22 All this happened in fulfillment of these words of the Lord in the prophet, where he says —
23 ‘The virgin will conceive and will give birth to a son, and they will give him the name Immanuel’ — a word which means ‘God is with us.’
24 When Joseph woke up, he did as the angel of the Lord had directed him.
25 He made Mary his wife, but they did not sleep together before the birth of her son; and to this son he gave the name Jesus.
    """)

    yield verses(2,"""
1 After the birth of Jesus at Bethlehem in Judea, in the reign of King Herod, some astrologers from the East arrived in Jerusalem, asking:
2 “Where is the newborn king of the Jews? For we saw his star in the east, and have come to worship him.”
3 When King Herod heard of this, he was much troubled, and so too was all Jerusalem.
4 He called together all the chief priests and teachers of the Law in the nation, and questioned them as to where the Christ was to be born.


5 “At Bethlehem in Judea,” was their answer, “for it is said in the prophet —


6 ‘And you, Bethlehem in Judah's land,
     are in no way least among the chief cities of Judah,
   for out of you will come a ruler —
     who will shepherd my people Israel.’”


7 Then Herod secretly sent for the astrologers. He found out from them the time of the appearance of the star.
8 Sending them to Bethlehem he said: “Go and make a careful search for the child. When you have found him, bring word back to me, so that I, too, can go and worship him.”
9 The astrologers heard what the king had to say, and then continued their journey. The star which they had seen in the east led them on, until it reached and stood over the place where the child was.
10 At the sight of the star they were filled with joy.
11 Entering the house, they saw the child with his mother, Mary, and fell at his feet and worshiped him. Then they opened their treasure chests, and offered to the child presents of gold, frankincense, and myrrh.
12 But afterward, having been warned in a dream not to go back to Herod, they returned to their own country by another road.


13 After they had left, an angel of the Lord appeared to Joseph in a dream, and said:

“Get up, take the child and his mother, and seek refuge in Egypt; and stay there until I tell you to return, for Herod is about to search for the child, to put him to death.”
14 Joseph woke up, and taking the child and his mother by night, went into Egypt,
15 and there he stayed until Herod's death; in fulfillment of these words of the Lord in the prophet, where he says —

   ‘Out of Egypt I called my Son.’


16 When Herod found out that the astrologers had tricked him, he flew into a rage. He sent and put to death all the boys in Bethlehem and the whole of that region, who were two years old or under, guided by the time which he had learned from the astrologers.
17 Then were fulfilled these words spoken in the prophet Jeremiah, where he says —


18 ‘A voice was heard in Ramah,
     weeping and mourning loudly;
   Rachel, weeping for her children,
     refusing all comfort for they were dead.’


19 But, on the death of Herod, an angel of the Lord appeared in a dream to Joseph in Egypt, and said:
20 “Get up, take the child and his mother, and go into the Land of Israel, for those who sought to take the child's life are dead.”
21 He woke up, and taking the child and his mother, went into the Land of Israel.
22 But, hearing that Archelaus had succeeded his father Herod as king of Judea, he was afraid to go back there; and having been warned in a dream, he went into the part of the country called Galilee.
23 There he settled in the town of Nazareth, in fulfillment of these words in the prophets — ‘He will be called a Nazarene.’
    """)
    yield section("The Birth, Parentage and Infancy")

    yield verses(1,"""
1 A genealogy of Jesus Christ, a descendant of David and Abraham.
2 Abraham was the father of Isaac, Isaac of Jacob, Jacob of Judah and his brothers,
3 Judah of Perez and Zerah, whose mother was Tamar, Perez of Hezron, Hezron of Aram,
4 Aram of Aminadab, Aminadab of Nahshon, Nahshon of Salmon,
5 Salmon of Boaz, whose mother was Rahab, Boaz of Obed, whose mother was Ruth, Obed of Jesse,
6 Jesse of David the King. David was the father of Solomon, whose mother was Uriah's widow,
7 Solomon of Rehoboam, Rehoboam of Abijah, Abijah of Asa,
8 Asa of Jehoshaphat, Jehoshaphat of Joram, Joram of Uzziah,
9 Uzziah of Jotham, Jotham of Ahaz, Ahaz of Hezekiah,
10 Hezekiah of Manasseh, Manasseh of Amon, Amon of Josiah,
11 Josiah of Jechoniah and his brothers, at the time of the Exile to Babylon.
12 After the Exile to Babylon — Jechoniah was the father of Salathiel, Salathiel of Zerubbabel,
13 Zerubbabel of Abiud, Abiud of Eliakim, Eliakim of Azor,
14 Azor of Zadok, Zadok of Achim, Achim of Eliud,
15 Eliud of Eleazar, Eleazar of Matthan, Matthan of Jacob,
16 Jacob of Joseph, the husband of Mary, who was the mother of Jesus, who is called ‘Christ’.
17 So the whole number of generations from Abraham to David is fourteen; from David to the Exile to Babylon fourteen; and from the Exile to Babylon to the Christ fourteen.
18 This is how Jesus Christ was born:
His mother Mary was engaged to Joseph, but, before the marriage took place, she found herself to be pregnant by the power of the Holy Spirit.
19 Her husband, Joseph, was a just man and, since he did not want to disgrace her publicly, he resolved to put an end to their engagement privately.
20 He had been thinking this over, when an angel of the Lord appeared to him in a dream.
“Joseph, son of David,” the angel said, “do not be afraid to take Mary for your wife, for her child has been conceived by the power of the Holy Spirit.
21 She will give birth to a son; name him Jesus, for he will save his people from their sins.”
22 All this happened in fulfillment of these words of the Lord in the prophet, where he says —
23 ‘The virgin will conceive and will give birth to a son, and they will give him the name Immanuel’ — a word which means ‘God is with us.’
24 When Joseph woke up, he did as the angel of the Lord had directed him.
25 He made Mary his wife, but they did not sleep together before the birth of her son; and to this son he gave the name Jesus.
    """)

    yield verses(2,"""
1 After the birth of Jesus at Bethlehem in Judea, in the reign of King Herod, some astrologers from the East arrived in Jerusalem, asking:
2 “Where is the newborn king of the Jews? For we saw his star in the east, and have come to worship him.”
3 When King Herod heard of this, he was much troubled, and so too was all Jerusalem.
4 He called together all the chief priests and teachers of the Law in the nation, and questioned them as to where the Christ was to be born.


5 “At Bethlehem in Judea,” was their answer, “for it is said in the prophet —


6 ‘And you, Bethlehem in Judah's land,
     are in no way least among the chief cities of Judah,
   for out of you will come a ruler —
     who will shepherd my people Israel.’”


7 Then Herod secretly sent for the astrologers. He found out from them the time of the appearance of the star.
8 Sending them to Bethlehem he said: “Go and make a careful search for the child. When you have found him, bring word back to me, so that I, too, can go and worship him.”
9 The astrologers heard what the king had to say, and then continued their journey. The star which they had seen in the east led them on, until it reached and stood over the place where the child was.
10 At the sight of the star they were filled with joy.
11 Entering the house, they saw the child with his mother, Mary, and fell at his feet and worshiped him. Then they opened their treasure chests, and offered to the child presents of gold, frankincense, and myrrh.
12 But afterward, having been warned in a dream not to go back to Herod, they returned to their own country by another road.


13 After they had left, an angel of the Lord appeared to Joseph in a dream, and said:

“Get up, take the child and his mother, and seek refuge in Egypt; and stay there until I tell you to return, for Herod is about to search for the child, to put him to death.”
14 Joseph woke up, and taking the child and his mother by night, went into Egypt,
15 and there he stayed until Herod's death; in fulfillment of these words of the Lord in the prophet, where he says —

   ‘Out of Egypt I called my Son.’


16 When Herod found out that the astrologers had tricked him, he flew into a rage. He sent and put to death all the boys in Bethlehem and the whole of that region, who were two years old or under, guided by the time which he had learned from the astrologers.
17 Then were fulfilled these words spoken in the prophet Jeremiah, where he says —


18 ‘A voice was heard in Ramah,
     weeping and mourning loudly;
   Rachel, weeping for her children,
     refusing all comfort for they were dead.’


19 But, on the death of Herod, an angel of the Lord appeared in a dream to Joseph in Egypt, and said:
20 “Get up, take the child and his mother, and go into the Land of Israel, for those who sought to take the child's life are dead.”
21 He woke up, and taking the child and his mother, went into the Land of Israel.
22 But, hearing that Archelaus had succeeded his father Herod as king of Judea, he was afraid to go back there; and having been warned in a dream, he went into the part of the country called Galilee.
23 There he settled in the town of Nazareth, in fulfillment of these words in the prophets — ‘He will be called a Nazarene.’
    """)

    yield section("The Preparation")

    yield verses(3,"""
1 About that time John the Baptist first appeared, proclaiming in the wilderness of Judea:
2 “Repent, for the kingdom of heaven is at hand.”
3 John was the one who was spoken of in the prophet Isaiah, where he says —

   ‘The voice of one crying aloud in the wilderness:
   “Make ready the way of the Lord,
   make his paths straight.”’


4 John's clothes were made of camels' hair, with a leather strap around his waist, and his food was locusts and wild honey.
5 At that time Jerusalem, and all Judea, as well as the whole district of the Jordan, went out to him
6 and were baptized by him in the Jordan River, confessing their sins.


7 But when John saw many of the Pharisees and Sadducees coming to receive his baptism, he said to them:

“You children of snakes! Who has prompted you to seek refuge from the coming judgment?
8 Let your life, then, prove your repentance;
9 and do not think that you can say among yourselves ‘Abraham is our ancestor,’ for I tell you that out of these stones God is able to raise descendants for Abraham!
10 Already the axe is lying at the root of the trees. Therefore every tree that fails to bear good fruit will be cut down and thrown into the fire.
11 I, indeed, baptize you with water to teach repentance; but he who is coming after me is more powerful than I, and I am not fit even to carry his sandals. He will baptize you with the Holy Spirit and with fire.
12 His winnowing-fan is in his hand, and he will clear his threshing-floor, and store his grain in the barn, but the chaff he will burn with a fire that cannot be put out.”


13 Then Jesus came from Galilee to the Jordan, to John, to be baptized by him.
14 But John tried to prevent him.

“I need to be baptized by you,” he said, “so why have you come to me?”


15 “This is the way it should be for now,” Jesus answered, “because we should do everything that God requires.” So John agreed.


16 After the baptism of Jesus, and just as he came up from the water, the heavens opened, and he saw the Spirit of God coming down like a dove and resting on him,
17 and from the heavens there came a voice which said: “This is my dearly loved son, who brings me great joy.”


    """)

    yield verses(4,"""
    """)

    yield verses(5,"""
    """)
