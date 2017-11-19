# atportalen
SU AT Portalens APP

# Vi använder Kivy för att skapa appen.
Finns här: https://kivy.org/#home

Ladda ner här: https://kivy.org/#download

## För Mac:

  brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer

  virtualenv atenv
  
  source atenv/bin/activate
  
  pip install -I Cython==0.25.2
  
  pip install kivy

## För Windows:

  python -m pip install --upgrade pip wheel setuptools
  python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
  python -m pip install kivy.deps.gstreamer
  python -m pip install kivy.deps.angle
  python -m pip install kivy

# Appen ska ha

1. Inloggnings-sida.
2. Sida med
  * Anställning - Ledighet
  * Tjänstgöring - Schema - Legitimation
  * Utbildning - Kurser
  * Forskning - Förbättring
  * Handledning
  * AT-råd - AT-rum
  * Kontakt
  * Regionkalendern
3. Sida som kan presentera texterna från AT-portalen
