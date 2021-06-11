setup:
	conda create --file environment.yml || conda env update --file environment.yml

run_pre_process_data:
	cd plpred\
		&& python 'preprocessing.py'

run_exploratory_data_analysis:
	plpred-preprocess -m data/raw/membrane.fasta \
		-c data/raw/cytoplasm.fasta \
		-o data/processed/processed.csv

model_training:
	plpred-train -p data/processed/processed.csv \
		-o data/models/model.pickle \
		-r

model_test:
	python -m pytest

server:
	plpred-server \
		--host 0.0.0.0 \
		--port n \
		--model data/models/model.pickle