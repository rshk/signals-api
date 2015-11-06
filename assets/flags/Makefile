WGET = wget
SVG_TARGETS = A.svg B.svg C.svg D.svg E.svg F.svg G.svg H.svg I.svg J.svg K.svg L.svg M.svg N.svg O.svg P.svg Q.svg R.svg S.svg T.svg U.svg V.svg W.svg X.svg Y.svg Z.svg
PNG_TARGETS = A.png B.png C.png D.png E.png F.png G.png H.png I.png J.png K.png L.png M.png N.png O.png P.png Q.png R.png S.png T.png U.png V.png W.png X.png Y.png Z.png

.PHONY: all

all: $(SVG_TARGETS) $(PNG_TARGETS)

clean:
	rm -f $(SVG_TARGETS)
	rm -f $(PNG_TARGETS)

A.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/7/71/ICS_Alpha.svg

B.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/f/f7/ICS_Bravo.svg

C.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/e/e7/ICS_Charlie.svg

D.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/e/eb/ICS_Delta.svg

E.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/0/0b/ICS_Echo.svg

F.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/a/a8/ICS_Foxtrot.svg

G.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/f/fb/ICS_Golf.svg

H.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/0/0f/ICS_Hotel.svg

I.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/8/8e/ICS_India.svg

J.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/a/a0/ICS_Juliet.svg

K.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/a/a8/ICS_Kilo.svg

L.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/7/76/ICS_Lima.svg

M.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/7/73/ICS_Mike.svg

N.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/2/21/ICS_November.svg

O.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/c/c9/ICS_Oscar.svg

P.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/d/d0/ICS_Papa.svg

Q.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/d/d4/ICS_Quebec.svg

R.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/b/bf/ICS_Romeo.svg

S.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/3/36/ICS_Sierra.svg

T.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/1/1e/ICS_Tango.svg

U.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/e/e2/ICS_Uniform.svg

V.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/e/ef/ICS_Victor.svg

W.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/8/88/ICS_Whiskey.svg

X.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/b/ba/ICS_X-ray.svg

Y.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/2/23/ICS_Yankee.svg

Z.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/c/c6/ICS_Zulu.svg

$(PNG_TARGETS): %.png: %.svg
	inkscape -z -w 200 -e $@ $<
