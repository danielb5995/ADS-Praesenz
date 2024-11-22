Datensatz
=========

research_dataset.csv
--------------------

Der Datensatz beschreibt die Nutzung der HRS-Software im Probezeitraum inkl.
der Fortführung der Nutzung über den Testzeitraum hinaus.

Basics:

- Zeitraum: 1. November 2023 bis 31. Oktober 2024
- n of entities = 10.000
- n of attributes = 9 (alle numerisch, größtenteils float)

Liste der Variablen:

- ``sales_calls``: Anzahl Verkaufsgespräche während des Testzeitraums.
- ``interactions``: Kontakte mit dem Kunden (inkl. Verkaufsgespräche) während des Testzeitraums.
- ``economy``: Wirtschaftliche Lage des Kunden.
- ``last_upgrade``: Wann hat der Kunde zuletzt die Software aktualisiert?
- ``discount``: Rabatt, der dem Kunden gewährt wird. Höhe des Discounts wird vom Sales-Mitarbeitenden festgelegt, nach Gefühl, in Bezug auf dessen Einschätzung, ob der Kunde abspringt.
- ``monthly usage``: Monatliche Nutzung der Software durch den Kunden, normalisiert auf 0 bis 1.
- ``ad_spend``: Höhe der Werbeausgaben in Tausend Euro, als Ausgaben des Kunden als Teil der Nutzung der Software.
- ``bugs_reported``: Fehler in der Software, die durch den Kunden gemeldet werden. Potentieller Indikator für Engagement.
- ``did_renews``: Wurde der Nutzungsvertrag am Ende des Testzeitraums verlängert.

Datenqualität:

- Es gibt keine Duplikate oder Missing Values.
