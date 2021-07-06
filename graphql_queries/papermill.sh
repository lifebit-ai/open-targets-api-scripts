# R example retrieving variant info
papermill R.ipynb R_rendered.ipynb -p selected_variant_a '2_97032743_A_C' -p selected_variant_b '1_154453788_C_T'

# python example retrieving colocolization data using ENSEMBL gene ID
papermill python.ipynb python_rendered.ipynb -p gene_id 'ENSG00000188906'