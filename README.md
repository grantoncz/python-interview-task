# Úkol 1: Vytvoření Python Mikroslužby pro Zpracování Dat

## Cíl
Vytvořte mikroslužbu v Pythonu, která na vstupu obdrží neuspořádaná data a na výstupu poskytne strukturovaná data ve formátu JSON. Tato služba bude simulovat komponentu většího systému pro zpracování dat z externích zdrojů.

Pokud je pro Vás tento úkol příliš náročný, přejděte na bod **Úkol 1: Fallback**.

## Instrukce
1. **Popis Projektu:** Vyviňte mikroslužbu v Pythonu, která na vstupu obdrží dotaz ve formě textu, pošle tento dotaz na AI model přes API, získá od něj odpověď, zpracuje tuto odpověď a následně poskytne zpracované výsledky ve formátu JSON prostřednictvím vlastního API. Jako příklad můžete použít dotaz na popis Pokémona, kde AI model generuje neuspořádaný textový popis, který vaše služba transformuje na strukturovaný JSON.
   
2. **Požadavky:**
   - Použijte jakýkoliv webový framework v Pythonu, jako je Flask nebo FastAPI.
   - Vytvořte funkci pro volání AI modelu (např. přes OpenAI API nebo jiné dostupné AI API).
   - Z implementace musí být zřejmé, jak z neuspořádaného textu vytváříte strukturovaná data (např. extrakce informací z textu a jejich uspořádání do JSON).
   - Vytvořte endpoint, který bude přijímat dotazy od uživatelů a vracet odpovědi ve formátu JSON. Žádný specifický model nebo schéma není zadáno a lze tak použít jakékoliv.
   
3. **Bonus (Nepovinné):**
   - Zahrňte vhodný exception handling a v případech, kdy to dává smysl .
   - Poskytněte `README.md` s instrukcemi, jak nastavit a spustit mikroslužbu, spolu s vysvětlením implementované logiky.
   - Implementujte pro službu unit testy.

## Kritéria Hodnocení
- Funkčnost: Mikroslužba funguje podle popisu a elegantně zvládá chyby.
- Kvalita kódu: Čistý, čitelný a dobře organizovaný kód.
- Bonus: Jasné instrukce a vysvětlení v `README.md`, přítomnost unit testů.

# Úkol 1: Fallback
Tento úkol vypracujte pouze v případě, pokud je pro Vás **Úkol 1** příliš náročný.

## Cíl
Vytvořte mikroslužbu v Pythonu, která na vstupu umí příjmout textové parametry, zpracuje je a vrátí jednoduchý výstup ve formátu JSON.

## Instrukce
1. **Požadavky:**
   - Použijte webový framework v Pythonu, jako je Flask nebo FastAPI.
   - Na vstupu bude textový řetězec.
   - Vytvořte endpoint pro zpracování textového řetězce.
   - Zpracujte vstupní řetězec a vrátíte strukturovanou odpověď ve formátu JSON.
   
2. **Bonus (Nepovinné):**
   - Zahrňte ošetření chyb a vhodné response kódy.
   - Poskytněte `README.md` s instrukcemi, jak nastavit a spustit mikroslužbu, spolu s vysvětlením implementované logiky.

## Kritéria Hodnocení
- Funkčnost: Mikroslužba funguje podle popisu a elegantně zvládá chyby.
- Kvalita kódu: Čistý, čitelný a dobře organizovaný kód.
- Bonus: Jasné instrukce a vysvětlení v `README.md`.

(Úkoly 2 a 3 zůstávají nezměněny.)

Tímto přístupem je úkol jasně formulován a zaměřen na specifické technické dovednosti, které chcete u kandidátů vyhodnotit, včetně práce s API, zpracování dat a vytváření webových služeb.

# Úkol 2: Dockerizace

## Cíl

Kontejnerizujte projekt z Úkolu 1.

## Instrukce

1. Vytvořte `Dockerfile` pro kontejnerizaci vašeho projektu.
2. Vytvořte/doplňte stručně `README.md`, který vysvětluje, jak sestavit a spustit Docker kontejner.
3. Zaměřte se na vytvoření základního, ale správného `Dockerfile`.

## Kritéria Hodnocení

- Správné nastavení Dockerfile.
- Schopnost sestavit a spustit kontejner úspěšně.
- Jasnost instrukcí v `README.md`.

# Úkol 3: Použití Gitu a GitHubu

## Cíl

Demonstrujte základní dovednosti Gitu a GitHubu.

## Instrukce

1. Vytvořte veřejný repozitář na GitHub.com.
2. Pro Vaši práci z úkolů 1 a 2 vytvořte novou větev nazvanou `my-python-task`, nahrajte do ní všechny soubory a vaše řešení nahrajte do GitHubu do této větve.
3. Do tohoto veřejného projektu přidejte uživatele `josef.polach@granton.cz` jako spolupracujícího.
4. Vytvořte na GitHubu nový pull request, aby jste projekt připravili pro zamergování vašich změn do hlavní větve. (pouze request, změny zatím nemergujte)

## Kritéria Hodnocení

- Správné použití Gitu pro vytváření větví a commitování změn.
- Úspěšné podání pull requestu.
- Porozumění konceptům správy verzí.
