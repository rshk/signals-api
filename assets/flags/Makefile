WGET = wget
SVG_TARGETS = A.svg B.svg C.svg D.svg E.svg F.svg G.svg H.svg I.svg J.svg K.svg L.svg M.svg N.svg O.svg P.svg Q.svg R.svg S.svg T.svg U.svg V.svg W.svg X.svg Y.svg Z.svg 0.svg 1.svg 2.svg 3.svg 4.svg 5.svg 6.svg 7.svg 8.svg 9.svg R1.svg R2.svg R3.svg R4.svg
PNG_TARGETS = A.png B.png C.png D.png E.png F.png G.png H.png I.png J.png K.png L.png M.png N.png O.png P.png Q.png R.png S.png T.png U.png V.png W.png X.png Y.png Z.png 0.png 1.png 2.png 3.png 4.png 5.png 6.png 7.png 8.png 9.png R1.png R2.png R3.png R4.png

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

0.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/a/ac/ICS_Pennant_Zero.svg

1.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/c/c1/ICS_Pennant_One.svg

2.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/c/c0/ICS_Pennant_Two.svg

3.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/6/64/ICS_Pennant_Three.svg

4.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/8/87/ICS_Pennant_Four.svg

5.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/a/ad/ICS_Pennant_Five.svg

6.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/d/da/ICS_Pennant_Six.svg

7.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/b/b8/ICS_Pennant_Seven.svg

8.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/3/30/ICS_Pennant_Eight.svg

9.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/2/2c/ICS_Pennant_Niner.svg

R1.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/6/61/ICS_Repeat_One.svg

R2.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/0/08/ICS_Repeat_Two.svg

R3.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/7/74/ICS_Repeat_Three.svg

R4.svg:
	$(WGET) -O $@ https://upload.wikimedia.org/wikipedia/commons/b/bd/ICS_Repeat_Four.svg


$(PNG_TARGETS): %.png: %.svg
	inkscape -z -w 1000 -e $@ $<
