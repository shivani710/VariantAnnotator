# VariantAnnotator


Variant Annotator is a Python script designed to annotate genetic variants in a VCF (Variant Call Format) file using the Ensembl Variant Effect Predictor (VEP) API. It calculates relevant variant statistics, fetches additional information via API, and writes all the data into an output file in TSV (Tab-Separated Values) format.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [FAQs](#faqs)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Dependencies

This script is written in Python and relies on the following Python libraries:

- `pysam`: A Python module for reading, manipulating and writing genomic data sets. In this script, it is used for parsing the VCF file.
- `requests`: A simple HTTP library for Python, built for human beings. It is used for making HTTP requests to the VEP API.
- `csv`: A module for reading and writing tabular data in CSV format. It is used here for writing the output file.
- `logging`: This module defines functions and classes which implement a flexible event logging system for applications and libraries. It is used for progress reporting and error logging in this script.

## Installation

To install the necessary Python libraries, use the following pip command:

```bash
pip install pysam requests
```

Then, download the Python script itself:

```bash
git clone https://github.com/shivani710/VariantAnnotator.git
```

## Usage

To run the script, use the following command in your terminal:

```bash
python VariantAnnotation.py
```

By default, the script uses 'input.vcf' as the input file and 'output.tsv' as the output file. If you need to use different file paths, you can modify them directly in the script.

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

## FAQs

Please see the FAQ.md file for frequently asked questions.

## Troubleshooting

If you experience any issues while running the script, please check the error message in the console. You can also raise an issue in the GitHub repository with the full error message and the input data that caused it.

## Contributing

We welcome contributions to this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

Please make sure to update the tests as appropriate and ensure that all tests pass before submitting a pull request.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.
