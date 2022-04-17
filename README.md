**DSP - Chatbot**

**Obecný popis aplikace**

Aplikace simuluje chování chatbotů. Uživatel zadá příkaz, na který mu bot na základě jeho vstupu odpoví. Skládá se ze dvou částí, klientská a serverová. Obě části musí běžet na jiném hostu.

Serverová část zpracovává dotazy od klientské části. Umí tři, konkrétně vrací serverový čas, aktuální kurz eura vůči české koruně a jak se bot jmenuje. Kurz eura je ze zdroje České národní banky. V případě validního dotazu mu server odpoví zpět, pokud ne, informuje ho o chybě (špatný formát dotazu, chyba při komunikaci po síti)

**Grafické rozhraní**

Grafické rozhraní poskytuje následující:

- Jedno okno ve vzhledu chatu (levá strana odpovědi, pravá strana naše zprávy)
- Odesílat zprávy na server
- Zobrazovat přijaté zprávy ve formě textu
- Zobrazovat přijaté zprávy ve formátu HTML
- Informovat uživatel o výpadku


**Funkce aplikace**

![](useCaseDiagram.png)


|Funkce|<p>**Zpracování vstupu**</p><p></p>|
| :- | :- |
|Popis|<p>Proběhne rozdělení vstupního textu na jednotlivá slova.</p><p>Program vstupy rozlišuje na základě specifických slov pro daný požadavek. Pokud tyto slova nalezne a zároveň neobsahuje slova z jiného požadavku může začít se zpracováním úkolu. </p><p></p>|
|Vstup|<p>Text od uživatele</p><p></p>|
|Výstup|<p>Vrací hodnotu, která odpovídá funkci, kterou si uživatel vyžádal</p><p></p>|
|Chyby|<p>Pokud vstup není dostatečně specifický, poprosí uživatele o upravení dotazu. </p><p></p>|


|Funkce|<p>**Uživatelský vstup**</p><p></p>|
| :- | :- |
|Popis|<p>Vstup od uživatele je pouze v anglickém jazyce. Měl by být dostatečně konkrétní a obsahovat klíčová slova pro daný požadavek. Uživatel se může zeptat, jak by měl dotaz vypadat, pomocí příkazu „Help“. Velká malá písmena nejsou důležitá.</p><p></p>|
|Vstupy|<p>Pro čas: time, o’clock.</p><p>Pro jméno: name, what’s your name.</p><p>Pro kurz €: exchange rate, euro, eur</p><p>Pro kurz € v konkrétní den: date DD.MM.RRRR euro</p><p>Pro kompletní historii €: euro history</p><p></p>|
|Výstup|<p>Vrací hodnotu, která odpovídá funkci, kterou si uživatel vyžádal</p><p></p>|
|Chyby|<p>Pokud vstup není dostatečně specifický, poprosí uživatele o upravení dotazu. </p><p></p>|


|Funkce|<p>**Vrať čas**</p><p></p>|
| :- | :- |
|Popis|<p>Při zavolání této funkce bot vezme čas a pošle ho zpátky uživateli, ve formě HH:MM:SS.</p><p></p>|
|Výstup|<p>Vrací serverový čas</p><p></p>|


|Funkce|<p>**Vrať jméno**</p><p></p>|
| :- | :- |
|Popis|<p>Při zavolání této funkce se bot uživateli představí,</p><p></p>|
|Výstup|<p>Vrátí jméno bota</p><p></p>|


|Funkce|<p>**Vrať kurz** </p><p></p>|
| :- | :- |
|Popis|<p>Tato funkce vrací aktuální kurz eura vůči české koruně ze zdroje České národní banky, kde se kurz každý všední den ve 14:30 aktualizuje. </p><p>Umí zpracovat 3 typy požadavků. Nejaktuálnější kurz, kurz v konkrétní den v historii a kompletní historii od spuštění serveru.</p><p></p>|
|Výstup|<p>Podle požadavku uživatele. </p><p>- Nejaktuálnější kurz (i s datumem)</p><p>- Kurz v historii (pokud je dostupný) jinak hláška, že není dostupný</p><p>- Kompletní historie </p><p></p>|
|Chyby|<p>V případě výpadku ČNB se vrátí nejaktuálnější kurz</p><p></p>|


|Funkce|<p>**Aktualizace kurzu**</p><p></p>|
| :- | :- |
|Popis|<p>Server si každý všední den stáhne kurz eura, ze stránek České národní banky.</p><p></p>|
|Vstupy|<p><https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt></p><p></p>|
|Výstup|<p>Uloží data kurzu ve formě (datum, kurz)</p><p></p>|

