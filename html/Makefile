BOOTSTRAP_CSS := https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css

all: index.html

index.html: ../README.md
	pandoc $< -o $@ -t html5 -c $(BOOTSTRAP_CSS) -A .a -B .b

clean:
	rm -f index.html
