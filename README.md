# open-targets-api-scripts

`graphql_queries` contains examples in R, python and bash using Open Targets Genetics API.

## Example


```
docker run --rm -it -v $PWD:$PWD -w $PWD quay.io/lifebitai/opentargets:latest
cd graphql_queries
chmod u+x papermill.sh
./papermill.sh
```
The above produces 3 files: `1_154453788_C_T_info.csv`,`2_97032743_A_C_info.csv` and `ENSG00000188906_coloc_info.tsv`.

```
head -n2 1_154453788_C_T_info.csv
"pval","beta","betaCILower","betaCIUpper","oddsRatio","oddsRatioCILower","oddsRatioCIUpper","nTotal","overallR2","posteriorProbability","indexVariant.id","indexVariant.rsId","study.studyId","study.pmid","study.pubAuthor","study.pubDate","study.traitReported","input_variant"
1e-15,0.08527,0.06434014,0.10619986,NA,NA,NA,350473,0.799818994276,NA,"1_154422736_C_A","rs4133213","NEALE2_30040_raw",NA,"UKB Neale v2","2018-08-01","Mean corpuscular volume","1_154453788_C_T"
```

```
head -n2 ENSG00000188906_coloc_info.tsv
phenotypeId	qtlStudyId	h3	h4	log2h4h3study.studyId	study.traitReported	study.pubAuthorleftVariant.id	tissue.id	tissue.name
ILMN_1776649	CEDAR	0.1681142704440033	0.8025379149342734	2.255127358738181	NEALE2_1518	Hot drink temperature	UKB Neale v2	12_40120934_C_TMONOCYTE_CD14	Monocyte cd14
```
