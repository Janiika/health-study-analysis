# HÄLSOSTUDIE ANALYS

Ett individuellt analysprojekt på en hälsostudie, del 2.

## Projektets innehåll (från del 1 - inkluderat även i del 2)
- Beskrivande analys
- Simulering kopplad till caset
- Konfidensintervall
- Hypotesprövning
- Stickprovsstorlek och power

## Projektets innehåll (del 2)
Del 2 bygger på del 1 med följande förändringar:
- En del av kod har flyttats från notebook till funktioner och moduler
- En klass `HealthAnalyzer` har skapats
- Korrelation mellan BMI och blodtryck
- Använt linjär regression för att prediktera blodtryck från ålder, vikt och kolesterol
- Multipel regression

## Dataset
Datasetet innehåller deltagarnas information om:
- Ålder
- Kön
- Längd
- Vikt
- Blodtryck
- Kolesterol
- Rökstatus
- Sjukdom

## Miljö
- Python version 3.14
- Bibliotek `pandas`, `numpy`, `matplotlib`, `scipy`, `sklearn`, `statsmodels` (see `requirements.txt`)

## Kör projektet
- pip install -r requirements.txt
- jupyter notebook: `report_del2.ipynb`