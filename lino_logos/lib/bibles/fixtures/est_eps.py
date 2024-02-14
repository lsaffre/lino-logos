# -*- coding: utf-8 -*-
# Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""
Loads some random excerps from the edition
found on http://www.piibel.net/ (copyright Eesti Piibli Selts).

"""

from __future__ import unicode_literals

from lino_logos.lib.bibles.loader import *


def objects():

    yield edition("est", "EPS", "Piibel")

    set_book("genesis")

    yield section("Jumal loob ja õnnistab maailma")

    yield verses(
        1, """
1 Alguses lõi Jumal taeva ja maa.
2 Maa oli tühi ja paljas ja pimedus oli sügavuse peal ja Jumala Vaim hõljus vete kohal.
3 Ja Jumal ütles: „Saagu valgus!” Ja valgus sai.
4 Ja Jumal nägi, et valgus oli hea, ja Jumal lahutas valguse pimedusest.
5 Ja Jumal nimetas valguse päevaks ja pimeduse ta nimetas ööks. Siis sai õhtu ja sai hommik - esimene päev.

6 Ja Jumal ütles: „Saagu laotus vete vahele ja see lahutagu veed vetest!”
7 Ja nõnda sündis: Jumal tegi laotuse ja lahutas veed, mis olid laotuse all, vetest, mis olid laotuse peal.
8 Ja Jumal nimetas laotuse taevaks. Siis sai õhtu ja sai hommik - teine päev.

9 Ja Jumal ütles: „Veed kogunegu taeva all ühte paika, et kuiva näha oleks!” Ja nõnda sündis.
10 Ja Jumal nimetas kuiva pinna maaks ja veekogu ta nimetas mereks. Ja Jumal nägi, et see oli hea.
11 Ja Jumal ütles: „Maast tärgaku haljas rohi, seemet kandvad taimed, viljapuud, mille viljas on nende seeme, nende liikide järgi maa peale!” Ja nõnda sündis:
12 maa laskis võrsuda haljast rohtu, seemet kandvaid taimi nende liikide järgi, ja viljapuid, mille viljas on nende seeme, nende liikide järgi. Ja Jumal nägi, et see oli hea.
13 Siis sai õhtu ja sai hommik - kolmas päev.

14 Ja Jumal ütles: „Saagu valgused taevalaotusse eraldama päeva ööst! Tähistagu need seatud aegu, päevi ja aastaid,
15 olgu nad valgusteks taevalaotuses, valgustuseks maale!” Ja nõnda sündis:
16 Jumal tegi kaks suurt valgust: suurema valguse valitsema päeval ja väiksema valguse valitsema öösel, ning tähed.
17 Ja Jumal pani need taevalaotusse, et nad valgustaksid maad
18 ja valitseksid päeval ja öösel ja eraldaksid valguse pimedusest. Ja Jumal nägi, et see oli hea.
19 Siis sai õhtu ja sai hommik - neljas päev.

20 Ja Jumal ütles: „Vesi kihagu elavaist olendeist, ja maa peal lennaku linnud taevalaotuse poole!”
21 Ja Jumal lõi suured mereloomad ja kõiksugu elavad olendid, kellest vesi kihab, nende liikide järgi, ja kõiksugu tiibadega linnud nende liikide järgi. Ja Jumal nägi, et see oli hea.
22 Ja Jumal õnnistas neid ja ütles: „Olge viljakad ja teid saagu palju, täitke mere vesi, ja lindusid saagu palju maa peale!”
23 Siis sai õhtu ja sai hommik - viies päev.

24 Ja Jumal ütles: „Maa toogu esile elavad olendid nende liikide järgi, kariloomad ja roomajad ja metsloomad nende liikide järgi!” Ja nõnda sündis:
25 Jumal tegi metsloomad nende liikide järgi, ja kariloomad nende liikide järgi, ja kõik roomajad maa peal nende liikide järgi. Ja Jumal nägi, et see oli hea.
26 Ja Jumal ütles: „Tehkem inimesed oma näo järgi, meie sarnaseks, et nad valitseksid kalade üle meres, lindude üle taeva all, loomade üle ja kogu maa üle ja kõigi roomajate üle, kes maa peal roomavad!”

27 Ja Jumal lõi inimese oma näo järgi, Jumala näo järgi lõi ta tema, ta lõi tema meheks ja naiseks.

28 Ja Jumal õnnistas neid, ja Jumal ütles neile: „Olge viljakad ja teid saagu palju, täitke maa ja alistage see enestele; ja valitsege kalade üle meres, lindude üle taeva all ja kõigi loomade üle, kes maa peal liiguvad!”

29 Ja Jumal ütles: „Vaata, mina annan teile kõik seemet kandvad taimed kogu maal, ja kõik puud, mis kannavad vilja, milles on nende seeme; need olgu teile roaks!
30 Ja kõigile loomadele maa peal ja kõigile lindudele taeva all ja kõigile roomajaile maa peal, kelles on elav hing, annan ma kõiksugu haljast rohtu toiduks.” Ja nõnda sündis.
31 Ja Jumal vaatas kõike, mis ta oli teinud, ja vaata, see oli väga hea. Siis sai õhtu ja sai hommik - kuues päev.
""")

    yield verses(
        2, """
    1 Nõnda on taevas ja maa ning kõik nende väed valmis saanud.
    2 Ja Jumal oli lõpetanud seitsmendaks päevaks oma töö, mis ta tegi, ja hingas seitsmendal päeval kõigist oma tegudest, mis ta oli teinud.
    3 Ja Jumal õnnistas seitsmendat päeva ja pühitses seda, sest ta oli siis hinganud kõigist oma tegudest, mis Jumal luues oli teinud.
    """)

    # end_section()

    yield section("Aadam ja Eeva")

    yield verses(
        2, """
    4 See on lugu taeva ja maa sündimisest, kui need loodi. Sel ajal, kui Issand Jumal tegi maa ja taeva,
    5 kui ainsatki väljapõõsast ei olnud veel maa peal ja ainsatki väljarohtu ei olnud veel tärganud, sest Issand Jumal ei olnud lasknud vihma sadada maa peale, ja inimest ei olnud põldu harimas,
    6 tõusis udu maast ja kastis kogu mullapinda.
    7 Ja Issand Jumal valmistas inimese, kes põrm on, mullast, ja puhus tema ninasse eluhinguse: nõnda sai inimene elavaks hingeks.

    8 Ja Issand Jumal istutas Eedeni rohuaia päevatõusu poole ja pani sinna inimese, kelle ta oli valmistanud.
    9 Ja Issand Jumal laskis maast tõusta kõiksugu puid, mis olid armsad pealtnäha ja millest oli hea süüa, ja elupuu keset aeda, ning hea ja kurja tundmise puu.
    10 Ja Eedenist sai alguse jõgi, mis kastis rohuaeda, jagunedes sealtpeale neljaks haruks:
    11 esimese nimi on Piison, see voolab ümber kogu Havilamaa, kus on kulda;
    12 selle maa kuld on hea, seal on bedolavaiku ja karneoolikive.
    13 Ja teise jõe nimi on Giihon, see voolab ümber kogu Kuusimaa.
    14 Ja kolmanda jõe nimi on Hiddekel, see voolab hommiku pool Assurit; ja neljas jõgi on Frat.
    15 Ja Issand Jumal võttis inimese ja pani ta Eedeni aeda harima ja hoidma.
    16 Ja Issand Jumal keelas inimest ja ütles: „Kõigist aia puudest sa võid küll süüa,
    17 aga hea ja kurja tundmise puust sa ei tohi süüa, sest päeval, mil sa sellest sööd, pead sa surma surema!”

    18 Ja Issand Jumal ütles: „Inimesel ei ole hea üksi olla; ma tahan teha temale abi, kes tema kohane on.”
    19 Ja Issand Jumal valmistas mullast kõik loomad väljal ja kõik linnud taeva all ning tõi inimese juurde, et näha, kuidas tema neid nimetab. Ja kuidas inimene igat elavat olendit nimetas, nõnda pidi selle nimi olema.
    20 Ja inimene pani nimed kõigile kariloomadele ja lindudele taeva all ja kõigile metsloomadele, aga inimesele ei leidunud abilist, kes tema kohane oleks.
    21 Siis Issand Jumal laskis tulla raske une inimese peale ja see jäi magama; siis ta võttis ühe tema küljeluudest ning sulges selle aseme taas lihaga.
    22 Ja Issand Jumal ehitas küljeluu, mille ta inimesest oli võtnud, naiseks ja tõi tema Aadama juurde.
    23 Ja Aadam ütles: „See on nüüd luu minu luust ja liha minu lihast. Teda peab hüütama mehe naiseks, sest ta on mehest võetud!”

    24 Seepärast jätab mees maha oma isa ja ema ning hoiab oma naise poole, ja nemad on üks liha!
    25 Ja nad olid mõlemad alasti, Aadam ja tema naine, ega häbenenud.
    """)

    set_book("matthew")

    yield section("Jeesuse põlvnemine")

    yield verses(
        1, """
1 Jeesuse Kristuse, Aabrahami poja, Taaveti poja sugupuu:
2 Aabrahamile sündis Iisak, Iisakile sündis Jaakob, Jaakobile
sündisid Juuda ja tema vennad,
3 Juudale sündisid Taamariga Perets ja Serah, Peretsile
sündis Hesron, Hesronile sündis Aram,
4 Aramile sündis Amminadab, Amminadabile sündis Nahson,
Nahsonile sündis Salma,
5 Salmale sündis Raahabiga Boas, Boasele sündis Rutiga Oobed,
Oobedile sündis Iisai,
6 Iisaile sündis kuningas Taavet.Taavetile sündis Uurija naisega Saalomon,
7 Saalomonile sündis Rehabeam, Rehabeamile sündis Abija,
Abijale sündis Aasa,
8 Aasale sündis Joosafat, Joosafatile sündis Jooram,
Jooramile sündis Ussija,
9 Ussijale sündis Jootam, Jootamile sündis Aahas, Aahasele
sündis Hiskija,
10 Hiskijale sündis Manasse, Manassele sündis Aamon, Aamonile
sündis Joosija,
11 Joosijale sündisid Jekonja ja tema vennad Paabeli
vangipõlve ajal.

12 Pärast Paabeli vangipõlve sündis Jekonjale Sealtiel,
Sealtielile sündis Serubbaabel,
13 Serubbaabelile sündis Abihuud, Abihuudile sündis Eljakim,
Eljakimile sündis Assur,
14 Assurile sündis Saadok, Saadokile sündis Ahhim, Ahhimile
sündis Elihuud,
15 Elihuudile sündis Eleasar, Eleasarile sündis Mattan,
Mattanile sündis Jaakob,
16 Jaakobile sündis Joosep, selle Maarja mees, kellest sündis
Jeesus, keda nimetatakse Kristuseks.

17 Niisiis on Aabrahamist Taavetini kokku neliteist sugupõlve
ja Taavetist Paabeli vangipõlveni neliteist sugupõlve ja Paabeli
vangipõlvest Kristuseni samuti neliteist sugupõlve.

Jeesuse sünd
18 Jeesuse Kristuse sündimisega oli aga nõnda. Tema ema
Maarja, kes oli Joosepiga kihlatud, leidis enne enda
kojuviimist, et ta ootab Pühast Vaimust last.
19 Tema mees Joosep aga, kes oli õiglane ega tahtnud teda
avalikult häbistada, võttis nõuks ta salaja minema saata.
20 Aga kui ta seda mõtles, vaata, siis ilmus talle
unenäos Issanda ingel, kes ütles: „Joosep, Taaveti poeg, ära
karda oma naist Maarjat enese juurde võtta, sest laps, keda ta
kannab, on Pühast Vaimust.
21 Ta toob ilmale poja ning sina paned talle nimeks Jeesus,
sest tema päästab oma rahva nende pattudest.”
22 Kõik see sündis, et läheks täide, mida Issand on rääkinud
prohveti kaudu:

23 „Ennäe, neitsi jääb lapseootele ja toob ilmale poja,
ja teda hüütakse nimega Immaanuel”,
see on tõlkes: Jumal on meiega.

24 Kui Joosep unest ärkas, tegi ta nõnda, nagu Issanda ingel
oli teda käskinud. Ta võttis oma naise enese juurde,
25 ent ei puutunud temasse, enne kui Maarja oli poja
ilmale toonud. Ja ta pani lapsele nimeks Jeesus.
    """)
