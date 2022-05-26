**DSP – rozšíření aplikace**

Rozšíření aplikace obsahuje přidanou funkcionalitu bota.  Doporučení, zda euro nakoupit nebo ne. Zavolá se příkazem “buy”.

|Funkce|Doporuč nákup|
| :- | :- |
|Popis|<p>Tato funkce doporučí nákup eura na základě jedné z podmínek: </p><p>- euro za poslední 3 dny klesá</p><p>- nestoupá o vice než 10 % z průměru za poslední 3 dny</p><p>V opačném případě nákup nedoporučí. </p>|
|Výstup|Vypíše, zda se nákup doporučuje nebo nedoporučuje s odůvodněním (buďto průměr za poslední 3 dny nebo rozdíl ceny za poslední 3 dny, o kolik se liší od prahu, kdy se již nedá/dá doporučit nákup)|
|Doplnění|Pojmem poslední 3 dny se myslí poslední 3 uložené kurzy. Tzv. pokud se uživatel zeptá v pondělí ráno, bude se doporučení počítat z pátka, čtvrtka a středy minulého týdne.|



