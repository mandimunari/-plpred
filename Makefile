setup:
	conda create --file environment.yml || conda env update --file environment.yml

run_pre_process_data:
	cd plpred\
		&& python 'preprocessing.py'

run_exploratory_data_analysis:
	cd notebooks\
 		&& ipython 'ExploratoryDataAnalysis.ipynb' && \
		jupyter nbconvert --to html 'ExploratoryDataAnalysis.ipynb'

model_training:
	python plpred/training.py