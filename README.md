# Praktikum strojnega učenja v fiziki

[Povezava](https://ucilnica.fmf.uni-lj.si/course/view.php?id=520) do spletne učilnice predmeta.

## Praktični napotki

- Na vajah bomo uporabljali operacijski sistem Linux (npr. [Ubuntu](https://ubuntu.com/desktop)). Za Windows je priporočljiva uporaba [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL), ki vam da dostop do Linux okolja na enostaven način.

- Za programiranje je trenutno najbolj priljubljen editor [VSCode](https://code.visualstudio.com/). Zelo dober tutorial za uporabo VSCode s Pythonom je [tukaj](https://pycon.switowski.com/).

- Celoten predmet je zasnovan na uporabi programskega jezika Pythona, ker se največ uporablja v strojnem učenju. Če še nimaš izkušenj s Pythonom, si lahko pomagaš s [Python tutorialom](https://lectures.scientific-python.org/).

### Računanje na daljavo

Uporabiš lahko računalnik MARVIN na FMF, na katerem lahko poganjate vaše domače naloge. Na spletni učilnici si ustvari račun, geslo dobiš po mailu. Na tem strežniku lahko zaganjaš zahtevnejše izračune v sistemu Linux, tako ti sploh ni treba imeti kode lokalno. Dostopen je preko ssh:
- uporabniki Linux-ov, macOS dostopate preko terminala z `ssh <username>@marvin.fmf.uni-lj.si`
- uporabniki Windows-ov:
    - preko terminala, če imate naložen ssh client
    -  Preprosteje: Naložite si [MobaXterm](https://mobaxterm.mobatek.net/)
- z VSCode lahko dostopate preko [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extensiona

Če želiš zapreti terminal (s tem se zapre tudi ssh), vendar pustiti program teči, uporabi [screen](https://linuxize.com/post/how-to-use-linux-screen/):

```shell
screen -S <session_name>
```

Za izhod iz screena uporabi kombinacijo tipk `Ctrl + A` in nato `Ctrl + D`. Za ponovni vstop v screen uporabi:

```shell
screen -r <session_name>
```

ki ga dobiš z 

```shell
screen -ls
```

### Pridobitev kode iz repozitorija

```shell
git clone https://github.com/j-gavran/PSUF_Hmumu.git
```

### Postavitev virtualnega okolja

Ideja virtualnega okolja je, da se izolira okolje, v katerem se izvajajo programi, od okolja, ki je na računalniku. Tako se lahko v tem "virtualnem" okolju namesti samo tiste knjižnice, ki so potrebne za izvajanje določenih programov.

Virtualno okolje se naloži preko pip-a:

```shell
pip install pip --upgrade
pip install virtualenv
```

in se ga postavi z ukazom:
```shell
python -m venv .venv
```

kjer `.venv` predstavlja ime virtualnega okolja. To okolje se aktivira z ukazom:
```shell
source .venv/bin/activate
```

Za izhod iz okolja se uporabi ukaz:
```shell
deactivate
```

Vse knjižnice si lahko namestiš tudi direktno brez uporabe tega okolja. Če si na Marvinu, je okolje že postavljeno v `/data/virtualenvs/virtenv-py310-PSUF/bin/activate`.

### Namestitev knjižnic

V virtualnem okolju se namestijo knjižnice, ki so potrebne za izvajanje programa, in koda tega repozitorija kot Python paket `psuf`. Oboje se namesti z ukazom (v direktoriju tega repozitorija):

```shell
pip install -e .
```

Zastavica `-e` (*editable*) pomeni, da se spremembe v kodi upoštevajo brez ponovne namestitve. Kodo potem uvažaš s polnimi potmi, npr. `from psuf.naloga_1.helpers.fit_CB import CrystalBall`, ne glede na to, iz katere mape jo zaganjaš.

Če paketa ne moreš namestiti (npr. v skupnem okolju na Marvinu, kjer so knjižnice že nameščene), dodaj repozitorij v Python path (v direktoriju tega repozitorija):

```shell
export PYTHONPATH=$(pwd)
```

### Uporabne bash komande

O komandah se lahko naučiš več z uporabo `man`, npr. `man pwd`. Lahko pa tudi z `<komanda> --help`.

- `pwd` (print working directory) - izpiše trenutno delovno mapo
- `cd <path>` (change directory) - spremeni trenutno delovno mapo na `<path>`
    - `cd .` - trenutna mapa
    - `cd ..` - pojdi eno mapo nazaj
- `ls <path>` (list) - izpiši datoteke na `<path>` poziciji
- `cp <to> <sem>` (copy) - kopiraj `<to>` datoteko `<sem>`
- `mv <to> <sem>` (move) - premakni `<to>` datoteko `<sem>`
    - uporabno tudi za preimenovanje datoteke, npr. `foo.txt` v `bar.txt`: `mv foo.txt bar.txt`
- `rm <file>` oz. `rm -r <foldername>` (remove) - izbriši `<file>` datoteko ali `<foldername>` mapo
- `pico <file>` oz. `nano <file>` - odpre `<file>` datoteko v preprostem urejevalniku
- `touch <file>` - ustvari prazno datoteko `<file>`
- `cat <file>` - izpiše vsebino datoteke `<file>`

### Oddaja poročil

- Obvezno: `pdf` format. 
- Ime datoteke: `psuf_naloga<N>_Ime_Priimek.pdf`.
- Poročilu **priloži vso kodo**, ki si jo uporabil/-a, stisnjeno v eno datoteko (`.zip` ali `.tar.gz`) z enakim imenom, npr.:
    - `zip -r psuf_naloga<N>_Ime_Priimek.zip <mapa_s_kodo>`
    - `tar -czf psuf_naloga<N>_Ime_Priimek.tar.gz <mapa_s_kodo>`
- Zadeva: PSUF naloga `<N>` Ime Priimek na moj mail: [jan.gavranovic@ijs.si](mailto:jan.gavranovic@ijs.si).
