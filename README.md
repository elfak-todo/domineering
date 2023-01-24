# Domineering igra

Projekat iz predmeta Veštačka inteligencija.

## Pravila igre

Cilj igre je da jedan od igrača (vertikalni ili horizontalni) postavi svoje domine tako da blokira protivničke domine. Igra se najčešće igra na 8x8 tabli, ali je moguće menjati dimenzije table. Igrač koji prvi ne može da postavi svoju dominu gubi.

Modovi igre

- PvP (Person versus Person) - Čovek protiv Čoveka
- PvAI (Person versus Artificial Intelligence) - Čovek protiv veštačke inteligencije

## Tehnologije

Za izradu ove igre korišćen je python programski jezik sa tkinter paketom za izradu korisničkog interfejsa.

## Reč o implementaciji

Za implementaciju igranja poteza od strane računara korišćen je min-max algoritam sa alfa-beta odsecanjem.

Min-max algoritam sa alfa-beta odsecanjem je jedan od najčešće korišćenih algoritama u implementaciji računarskih igrača. Ovaj algoritam se koristi za generisanje poteza računarskog igrača tako što se simulira igru unapred i procenjuju se različiti scenariji.

Min-max algoritam radi tako što se za svaki sloj poteza (trenutni potez igrača i sledeći potez računara) izračunavaju svi mogući potezi i ocena njihove vrednosti. Ocena poteza se računa na osnovu heuristike, što je funkcija koja procenjuje koliko je dobar potez u odnosu na cilj igre.

Alfa-beta odsecanje se koristi za optimizaciju min-max algoritma tako što se preskaču podstabla čiji se rezultat ne može poboljšati. To se radi tako što se za svaki sloj poteza pamti alfa i beta vrednosti. Alfa vrednost predstavlja maksimalnu ocenu poteza za igrača koji trenutno igra, dok beta vrednost predstavlja minimalnu ocenu poteza za igrača koji će sledeći igrati. Ako se alfa vrednost u nekom podstablu poklapa sa beta vrednošću u drugom podstablu, tada se zna da se u tim podstablima ne može poboljšati rezultat, pa se ona preskaču.

## Autori

//TODO Tim

- Andrija Mitić 17805
- Luka Kocić 17714
- Milan Lukić 17728

## Pregled

![Pregled](/assets/game.jpg)
