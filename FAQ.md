

**Q1: What types of variants can this script handle?**

*A1: This script can handle any variant that is presented in standard VCF format, including SNPs (Single Nucleotide Polymorphisms), insertions, deletions, and CNVs (Copy Number Variations). However, please note that the accuracy and completeness of the annotation may vary depending on the specific variant and the data available from the Ensembl VEP API.*

**Q2: Can I use a different variant annotation API with this script?**

*A2: The current version of the script is designed to use the Ensembl VEP API. If you wish to use a different annotation API, you would need to modify the `get_variant_annotation` function and potentially other parts of the script to accommodate the different API's request format and response structure.*

**Q3: What should I do if the script reports an error?**

*A3: If the script reports an error, first check that your input VCF file is correctly formatted and that your internet connection is working. If the issue persists, you can open an issue on the GitHub repository with a description of the error and the input data that caused it.*

**Q4: The script is running slowly. How can I improve the performance?**

*A4: The performance of the script is largely dependent on the number of variants in your input VCF file and the response time of the VEP API. To improve performance, you might consider running the script on a more powerful machine or splitting your input VCF file into smaller chunks and running the script on each chunk separately.*

**Q5: What does the 'additional_info' column in the output file contain?**

*A5: The 'additional_info' column contains any additional data returned by the VEP API that is not included in the other output columns. This can include various types of information depending on the specific variant, such as regulatory region annotations, variant co-locatedness, etc.*

