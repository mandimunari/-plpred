setup:
	conda create --file environment.yml || conda env update --file environment.yml

run_exploratory_data_analysis:
	cd notebooks\
 		&& ipython 'ExploratoryDataAnalysis.ipynb' && \
		jupyter nbconvert --to html 'ExploratoryDataAnalysis.ipynb'
