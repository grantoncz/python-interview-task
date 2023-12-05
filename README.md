# Úkol 1: Vytvoření Python Mikroslužby pro Zpracování Dat

## Cíl:
Vytvořte mikroslužbu v Pythonu, která provádí zpracování dat. Tato služba by měla simulovat komponentu většího systému.

Pokud je pro Vás tento úkol příliž náročný přejděte na bod **Úkol 1: Fallback**.

## Instrukce:
1. **Popis Projektu:** Máte za úkol vyvinout mikroslužbu v Pythonu, která na vstupu obdrží název pokemona, získá data z externího [Pokémon API](https://pokeapi.co), zpracuje tato data a následně poskytne zpracované výsledky prostřednictvím vlastního API.
2. **Požadavky:**
   - Použijte webový framework v Pythonu, jako je Flask nebo FastAPI.
   - Na vstupu bude 1 path parametr pro název Pokémona
   - Načtěte data z veřejného  [Pokémon API](https://pokeapi.co).
   - Vytvořte endpoint pro poskytování zpracovaných dat.
   - Implementujte logiku zpracování dat tak, aby na výstupu API operace uživatel dostal tato data (přesný formát výstupu je čistě na Vás):
     - **Název**: Jméno Pokémona. 
     - **ID nebo číslo**: Unikátní identifikátor nebo číslo v Pokédexu Pokémona. 
     - **Typy**: Elementární typy Pokémona (např. Oheň, Voda, Tráva). 
     - **Sprite/Obrázek**: Obrázek reprezentující Pokémona. (pouze URL) 
     - **Výška a váha**: Fyzické rozměry Pokémona. 
     - **Schopnosti**: Speciální schopnosti nebo vlastnosti Pokémona.
3. **Bonus (Nepovinné):**
   - Zahrňte ošetření chyb a vhodné reponse kódy.
   - Poskytněte `README.md` s instrukcemi, jak nastavit a spustit mikroslužbu, spolu s vysvětlením implementované logiky.
   - Implementujte pro službu unit testy

## Kritéria Hodnocení:
- Funkčnost: Mikroslužba funguje podle popisu a elegantně zvládá chyby.
- Kvalita kódu: Čistý, čitelný a dobře organizovaný kód.
- Bonus: Jasné instrukce a vysvětlení v `README.md`, přítomnost unit testů

# Úkol 1: Fallback
Tento úkol vypracujte pouze v případě, pokud je pro Vás **Úkol 1** příliš náročný.

## Cíl:
Vytvořte mikroslužbu v Pythonu, která na vstupu umí příjmout parametry, zpracuje je a vrátí jednoduchý výstup.

## Instrukce:
1. **Požadavky:**
   - Použijte webový framework v Pythonu, jako je Flask nebo FastAPI.
   - Na vstupu budou 2 parametry `name` a `age`
   - Vytvořte endpoint pro poskytování zpracovaných dat.
   - zpracujte tyto parametry vhodným způsobem tak, aby program byl schopen vrátit data na výstup dle očekávání
   - na výstupu bude jednoduchá věta informující uživatele, jak se jmenuje a v jakém roce se narodil, například  `Tvoje jmeno je Josef a narodil ses v roce 1990.`
2. **Bonus (Nepovinné):**
   - Zahrňte ošetření chyb a vhodné response kódy.
   - Poskytněte `README.md` s instrukcemi, jak nastavit a spustit mikroslužbu, spolu s vysvětlením implementované logiky.


## Kritéria Hodnocení:
- Funkčnost: Mikroslužba funguje podle popisu a elegantně zvládá chyby.
- Kvalita kódu: Čistý, čitelný a dobře organizovaný kód.
- Bonus: Jasné instrukce a vysvětlení v `README.md`.

# Úkol 2: Dockerization

## Cíl:
Kontejnerizujte projekt Úkolu 1.

## Instrukce:
2. Vytvořte `Dockerfile` pro kontejnerizaci vašeho projektu.
3. Vytvořte/doplňte stručně `README.md`, který vysvětluje, jak sestavit a spustit Docker kontejner.
4. Zaměřte se na vytvoření základního, ale správného `Dockerfile`.

## Kritéria Hodnocení:
- Správné nastavení Dockerfile.
- Schopnost sestavit a spustit kontejner úspěšně.
- Jasnost instrukcí v `README.md`.

# Úkol 3: Použití Gitu a GitHubu

## Cíl:
Demonstrujte základní dovednosti Gitu a GitHubu.

## Instrukce:
1. Vytvořte veřejný repozitář na github.com 
2. Pro Vaši práci z úkolů 1 a 2 vytvořte novou větev nazvanou `my-python-task` nahrajte do ní všechny soubory a vaše řešení nahrajte do Git Hubu do této větve. 
3. Do tohoto veřejného projektu přidejte uživatele `pepa.polach@me.com` jako spolupracujícího. 
4. Vytvořte v Git Hubu nový pull request, aby jste projekt připravili pro zamergování vašich změn do hlavní větve. (pouze request, změny zatim nemergujte)

## Kritéria Hodnocení:
- Správné použití Gitu pro vytváření větví a commitování změn.
- Úspěšné podání pull requestu.
- Porozumění konceptům správy verzí