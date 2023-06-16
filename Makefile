pack.zip: outp pack.mcmeta
	-rm assets/minecraft/lang/en_us.json
	python pack.py
	zip -vr pack.zip assets pack.mcmeta
