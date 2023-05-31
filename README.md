# VariantAnnotator: An Extensible Toolkit for Genetic Variant Annotation

The Variant Annotator is a sophisticated software tool designed for bioinformatics research and development. It simplifies the task of processing and annotating genetic variants found in VCF (Variant Call Format) files. VCF is a standard format in bioinformatics for storing gene sequence variations.

## Table of Contents

- [Dependencies](## Dependencies)
- [Features](## Features)
- [Usage](## Instructions for Use)
- [Detailed Functionality](## Detailed Functionality)
- [Output](#output)
- [FAQs](#faqs)
- [Authors](#Authors)
- [Contribution](#contribution)
- [License](#license)

## Dependencies

The toolkit is developed in Python3 and requires the following Python libraries:

* `pyVCF`: A Python library for parsing and manipulating VCF files.
* `requests`: A simple HTTP library for Python, built for human beings. It is used for making HTTP requests to the VEP API.

## Features

This comprehensive toolkit comes with several advanced features that facilitate the exploration and analysis of genetic variants:

1. **Depth of Coverage Calculation**: It calculates the read depth for each variant by summing the forward and reverse strand coverage.

2. **Supporting Reads Percentage**: It computes the percentage of reads supporting the variant versus the total reads.

3. **Variant Typing**: It identifies the type of genetic variant (Single Nucleotide Variant (SNV), Insertion, Deletion, Complex, or Unknown) based on the reference (REF) and alternate (ALT) alleles.

4. **Variant Annotation**: It annotates each genetic variant with HGVS (Human Genome Variation Society) nomenclature.

5. **External API Integration**: It integrates with the Variant Effect Predictor (VEP) REST API to retrieve extensive variant annotations. These annotations significantly enrich the dataset, providing comprehensive insights about each variant.


## Instructions for Use

To use the Variant Annotator, follow these steps:

1. Set your working directory to the location where your VCF file is stored. This is currently preset as `.` within the script.

2. Invoke the `annotate_variants` function in the script with your desired input VCF file and output CSV file names: `annotate_variants('input_file.vcf', 'output_file.csv', delimiter=',')`. The delimiter can be adjusted as needed.

3. The annotated data will then be populated in the designated output file in CSV format.

To run the script, use the following command in your terminal:

```bash
python VariantAnnotator.py
```

By default, the script uses 'test_vcf_data.txt' as the input file and 'AnnotatedVariants.csv' as the output file. If you need to use different file paths, you can modify them directly in the script.


## Detailed Functionality

The `annotate_variants` function is the main driver of the script. It opens a VCF file, processes each variant using the `annotate_variant` function, and then writes the annotated data to an output CSV or TSV file.

In the `annotate_variant` function, a GET request is sent to the VEP REST API using the HGVS nomenclature of the variant as the query. The response is parsed to extract the gene symbol, the most severe consequence of the variant, minor allele frequency, and additional annotations. This information is combined with the variant's ID, depth of sequence coverage, number of supporting reads, percentage of supporting reads, and variant type to provide an enriched view of the variant.

## Cautionary Note

Please ensure that the input VCF file complies with the standard VCF format and includes all necessary fields (CHROM, POS, ID, REF, ALT, etc.) required for effective annotation. The current script does not manage exceptions related to missing or malformed data within the VCF file or network issues related to API requests.

## Output

The output file contains the following columns:

- `variant`: The identifier of the variant.
- `depth`: The total read depth at the variant site.
- `variant_reads`: The number of reads supporting the variant.
- `variant_percentage`: The percentage of reads supporting the variant.
- `gene`: The gene where the variant is located.
- `variant_type`: The type of the variant (substitution, insertion, CNV, etc.).
- `effect`: The predicted effect of the variant (missense, silent, intergenic, etc.).
- `maf`: The minor allele frequency of the variant.
- `additional_info`: Additional information from the VEP annotation, which includes any other details returned by the API.

## Future Development

The ongoing development of the Variant Annotator will focus on improving robustness by managing exceptions more efficiently and supporting parallel processing to facilitate the annotation of large datasets at a faster pace.

## Authors

* Shivani Nanda - [GitHub](https://github.com/shivani710)

## Contribution

We encourage and appreciate contributions from the bioinformatics community. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

Please make sure to update the tests as appropriate and ensure that all tests pass before submitting a pull request.


## License

This project is licensed ____________.

## Contact Information

For further inquiries, feedback, or suggestions, feel free to reach out to the project maintainers. We appreciate your input to make the Variant Annotator a more robust and useful


## FAQs

Please see the FAQ.md file for frequently asked questions.

## Troubleshooting

If you experience any issues while running the script, please check the error message in the console. You can also raise an issue in the GitHub repository with the full error message and the input data that caused it.

