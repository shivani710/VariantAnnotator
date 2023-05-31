# Frequently Asked Questions (FAQ)

## Q1: What is the Variant Annotator?

**A1:** The Variant Annotator is a Python tool designed for processing and annotating genetic variants in VCF (Variant Call Format) files. It adds comprehensive annotations from the Variant Effect Predictor (VEP) REST API, providing additional details about each genetic variant.

## Q2: What types of variants can this script handle?

**A2:** This script can handle any variant that is presented in standard VCF format, including SNPs (Single Nucleotide Polymorphisms), insertions, deletions, and CNVs (Copy Number Variations). However, please note that the accuracy and completeness of the annotation may vary depending on the specific variant and the data available from the Ensembl VEP API.*

## Q3: Can I use a different variant annotation API with this script?

**A3**: The current version of the script is designed to use the Ensembl VEP API. If you wish to use a different annotation API, you would need to modify the `get_variant_annotation` function and potentially other parts of the script to accommodate the different API's request format and response structure.**

## Q4: What should I do if the script reports an error?

**A4: If the script reports an error, first check that your input VCF file is correctly formatted and that your internet connection is working. If the issue persists, you can open an issue on the GitHub repository with a description of the error and the input data that caused it.**

## Q5: The script is running slowly. How can I improve the performance?
**A5: The performance of the script is largely dependent on the number of variants in your input VCF file and the response time of the VEP API. To improve performance, you might consider running the script on a more powerful machine or splitting your input VCF file into smaller chunks and running the script on each chunk separately.

## Q6: What are the prerequisites to run this tool?

**A6:** The tool requires Python3 and two Python libraries - PyVCF and Requests. Moreover, a properly formatted VCF file with the necessary fields is required for annotation.

## Q7: How can I run this tool?

**A7:** Once you have all the prerequisites, set your working directory to the location where your VCF file is stored. Then invoke the `annotate_variants` function in the script with your input VCF file and output CSV file names. Your annotated data will be written to the output CSV file.

## Q8: I have a large VCF file. How can I speed up the annotation process?

**A8:** As of now, the script doesn't support parallel processing. However, future versions of the script will handle parallel processing of VCF files for faster annotation.

## Q9: I am facing a problem while running the script. How can I seek help?

**A9:** If you encounter any problems or bugs, please open an issue on the GitHub repository explaining the problem in detail. Include as much information as possible, such as Python version, error messages, and input data format. 

## Q10: I have a suggestion for improvement or new feature. How can I contribute?

**A10:** We welcome contributions! Please refer to our contribution guidelines on [ReadMe](README.md) for details on how to contribute to this project.

## Q11: How does the tool determine the variant type?

**A11:** The tool determines the variant type based on the reference (REF) and alternate (ALT) alleles. For example, if the length of the REF is 1 and the length of all ALT alleles is 1, the variant is classified as a Single Nucleotide Variant (SNV).

## Q12: What kind of annotations does the tool add to the variants?

**A12:** The tool enriches the variants with several annotations, including gene symbol, most severe consequence, minor allele frequency, and additional annotations from the VEP REST API. It also computes depth of sequence coverage, number of supporting reads, percentage of supporting reads, and variant type.

## Q10: What is the output format of the tool?

**A10:** The tool outputs a CSV file where each row corresponds to a variant and each column corresponds to an annotation. The first row of the file contains the header, which describes the annotations.


