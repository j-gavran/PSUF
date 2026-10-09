# Naloga 1: Modeliranje 1-D porazdelitve: razpadi Higgsovega bozona $`H\rightarrow\mu\mu`$

Navodila naloge so v [`navodila.pdf`](navodila.pdf). Za postavitev virtualnega okolja in namestitev knjižnic glej [README](../../README.md) v korenu repozitorija.

## Struktura mape

- [`vaje/`](vaje/) - Jupyter zvezki z vaj ([`vaje1.ipynb`](vaje/vaje1.ipynb), [`vaje2.ipynb`](vaje/vaje2.ipynb), [`gpr_teorija.ipynb`](vaje/gpr_teorija.ipynb))
- [`helpers/`](helpers/) - pomožne skripte za generiranje histogramov, risanje in fitanje; grafi se shranijo v `helpers/plots/`
- [`data/`](data/)
    - `original_histograms/` - že narejeni histogrami
    - `raw_data/` - surovi podatki (`.h5`), ki jih preneseš s `create_histograms.py` ali v `vaje1.ipynb`
    - `generated_histograms/` - tvoji histogrami
- [`extra/`](extra/) - dodatni primeri
    - `torchGPR/` - GPR s knjižnicama PyTorch in GPyTorch
    - `FunctionalDecomposition/` - funkcijska dekompozicija (napisana za Python 2, glej njen [README](extra/FunctionalDecomposition/README.md))

## Zaganjanje kode

Koda je del Python paketa `psuf` (namestitev je opisana v [README](../../README.md)), zato jo uvažaš s polnimi potmi:

```python
from psuf.naloga_1 import DATA_DIR, PLOTS_DIR
from psuf.naloga_1.helpers.fit_CB import CrystalBall
```

`DATA_DIR` kaže na mapo `data/`, `PLOTS_DIR` pa na `helpers/plots/` te naloge. Ker so poti v kodi določene z njima, lahko skripte in zvezke zaganjaš iz katerekoli mape, npr.:

```shell
python -m psuf.naloga_1.helpers.fit_CB
```

Za primer v `extra/torchGPR/` namesti še dodatne knjižnice (v direktoriju repozitorija):

```shell
pip install -r psuf/naloga_1/extra/extra_requirements.txt
```

## Navodila in usmeritve

V nadaljevanju sledijo podrobnejša navodila in usmeritve za lažje reševanje naloge.

### 1. del

1. Iz surovih ("raw") podatkov zgeneriraj svoje histograme (priporočeno!) s pomočjo predpripravljene skripte [`helpers/create_histograms.py`](helpers/create_histograms.py), pri kateri lahko spreminjaš število predalov ("bin"-ov) in $`m_{\mu\mu}`$ interval, ki ga boš opazoval/-a. Histogrami (mejne in sredinske $`x`$ vrednosti predalov, vrednosti in napake) se shranijo v formatu `.npz`. Na voljo imaš že nekaj generiranih histogramov v [`data/original_histograms/`](data/original_histograms/), ki jih lahko uporabiš namesto generacije novih histogramov in nalaganja podatkov.

2. Ko imaš zgenerirane svoje histograme (ali pa uporabiš že narejene), jih lahko izrišeš s pomočjo skripte [`helpers/visualize_data.py`](helpers/visualize_data.py) (ustrezno s prejšnjo točko spremeni ime datotek, ki jih nalagaš).

3. Preveri, če so napake res pravilno upoštevane. Lahko jih namenoma pokvariš in ponoviš prva dva koraka, da vidiš vpliv.

4. Da se spoznaš z osnovnim fitanjem, najprej zgladi histogram simuliranega ozadja ("simulated background") s pomočjo preprostejših matematičnih funkcij in nadaljuj do različnih teoretično podkrepljenih nastavkov (CMS, ATLAS nastavki). Dobiš funkcijo/vrednosti predalov $`m(x_k)`$. Preizkusi primere iz vaj in uporabi [`helpers/atlas_fit_function.py`](helpers/atlas_fit_function.py).

5. Prilagodi funkcijo CB histogramu simuliranega signala, pri čemer upoštevaj še dodatni normalizacijski faktor. Dobiš funkcijo/vrednosti predalov $`s(x_k)`$. Primer je na voljo v [`helpers/fit_CB.py`](helpers/fit_CB.py).

### 2. del

6. Ker simulacija ozadja ni vedno najboljša, se po navadi za oceno ozadja raje vzame izmerjene podatke, pri čemer pa je potrebno izključiti območje, kjer pričakujemo signal ("blinding") - nočemo fitati še signala! Prilagodi torej funkcijo histogramu podatkov, da dobiš dobro oceno za ozadje ("background from data") in pri tem pazi, da pri fitu **ne** upoštevaš območja okrog mase Higgsovega bozona, npr. izključi interval 120 - 130 GeV. Dobiš funkcijo/vrednosti predalov $`b(x_k)`$. V tem koraku preizkusi tudi ML metode regresije (KRR, SVR, GPR, ...) za fitanje ozadja iz podatkov. Pomagaš si lahko s primeri v [`helpers/fit_GPR_simple.py`](helpers/fit_GPR_simple.py), [`helpers/fit_GPR_smooth.py`](helpers/fit_GPR_smooth.py) in [`helpers/fit_GPR_logartihm.py`](helpers/fit_GPR_logartihm.py).

7. Od podatkov odštej čim bolje zglajeno ozadje, ki si ga dobil/-a v prejšnji točki, da dobiš ekstrahiran signal. Če so vrednosti podatkov $`d(x_k)`$, dobimo ekstrahiran signal $`y(x_k)`$ kot $`y(x_k) = d(x_k) - b(x_k)`$.

8. Na ekstrahiran signal fitaj CB funkcijo s prostimi parametri, ki si jih dobil/-a v točki 5 tako, da ji v resnici prilagodiš le nov normalizacijski faktor, npr.: $`\alpha \cdot s(x_k)`$. Optimalno je, da je le-ta blizu 1.

9. Ker je izmerjenega signala še zelo malo, predlagamo, da postopek najprej narediš z umetno napihnjenim signalom - le  tega množi z nekim faktorjem (npr. $`\gamma = 100`$) in ga dodaj podatkom: $`s_\textrm{new}(x_k) = \gamma \cdot s(x_k)`$ in $`d(x_k) = d(x_k) + s_\textrm{new}(x_k)`$. Ker bo signal na ta način lepo izstopal iz ozadja, ga boš lažje izluščil/-a. Primer napihnjenega signala je v skripti [`helpers/create_asimov.py`](helpers/create_asimov.py).
