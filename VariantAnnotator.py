## Importing modules
import vcf
import csv
import requests
import os

## Setting Base Directory
Base_Dir='.'
os.chdir(Base_Dir)

## Functions


def calculate_read_depth(record):
    """
    Calculate the read depth by summing the counts of forward strand coverage (TCF) and reverse strand coverage (TCR).
    """
    forward_coverage = record.INFO.get('TCF', 0)
    reverse_coverage = record.INFO.get('TCR', 0)
    read_depth = forward_coverage + reverse_coverage
    return read_depth


def calculate_percentage_supporting_reads(supporting_reads, reference_reads):
    """
    Calculate the percentage of reads supporting the variant versus those supporting reference reads.
    """
    total_reads = supporting_reads + reference_reads
    percentage_supporting_reads = (supporting_reads / total_reads) * 100
    return percentage_supporting_reads

def get_variant_type(record):
    """
    Determine the type of variant based on the REF and ALT alleles.
    """
    ref = record.REF
    alts = record.ALT

    if len(ref) == 1 and all(len(alt) == 1 for alt in alts):
        return 'SNV'
    elif all(len(alt) > len(ref) for alt in alts):
        return 'Insertion'
    elif all(len(alt) < len(ref) for alt in alts):
        return 'Deletion'
    elif all(len(record.REF) > 1 and len(alt) > 1 for alt in alts): # Substitution
        return "Substitution"
    elif any(len(alt) != len(ref) for alt in alts):
        return 'Complex'
    else:
        return 'Unknown'

def annotate_variant(record):
    """
    Annotate a single variant with the required information.
    """
    alt = str(record.ALT[0])
    if len(record.REF) == 1 and len(alt) == 1: # SNP or SNV
        hgvs = f"{record.CHROM}:g.{record.POS}{record.REF}>{alt}"
    elif len(record.REF) > 1 and len(alt) == 1: # Deletion
        start = record.POS + 1
        end = record.POS + len(record.REF) - 1
        hgvs = f"{record.CHROM}:g.{start}_{end}del"
    elif len(record.REF) == 1 and len(alt) > 1: # Insertion
        hgvs = f"{record.CHROM}:g.{record.POS}_{record.POS+1}ins{alt[1:]}"
    elif len(record.REF) > 1 and len(alt) > 1: # Substitution
        start = record.POS + 1
        end = record.POS + len(record.REF) - 1
        hgvs = f"{record.CHROM}:g.{start}_{end}delins{alt[1:]}"
    else: # Some complex variant
        hgvs = "Complex variant, not converted to HGVS"
    variant_id = hgvs
    print("VariantID is {}".format(variant_id))
    depth_of_coverage = calculate_read_depth(record)
    supporting_reads = int(record.INFO.get('NR', 0)[0])
    reference_reads = int(record.INFO.get('TC', 0))
    percentage_supporting_reads = calculate_percentage_supporting_reads(supporting_reads, reference_reads)
    variant_type = get_variant_type(record)
    # Retrieve variant annotations from VEP HGVS API
    annotations = get_variant_annotations(hgvs)
    
    return [variant_id, depth_of_coverage, supporting_reads, percentage_supporting_reads, variant_type] + annotations

    

def get_variant_annotations(variant_id):
    url = f"https://rest.ensembl.org/vep/human/hgvs/{variant_id}?"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    try:
        response_data = response.json()
        annotations = []

        if isinstance(response_data, list) and len(response_data) > 0:
            variant_data = response_data[0]
            # print("response data is: {}".format(response_data))
            gene = variant_data.get('transcript_consequences', [{}])[0].get('gene_symbol', '')
            # variant_class = variant_data.get('transcript_consequences', [{}])[0].get('biotype', [''])
            variant_effect = variant_data.get('most_severe_consequence', '')
            minor_allele_frequency = variant_data.get('gnomad_AF', '')
            additional_annotations = variant_data.get('colocated_variants', [{}])[0].get('clin_sig', '')

            annotations = [gene, variant_effect, minor_allele_frequency, additional_annotations]

    except ValueError:
        print(f"Error decoding JSON for {variant_id}: {response.content}, HTTP status code: {response.status_code}")
        return []

    return annotations

def annotate_variants(vcf_file, output_file, delimiter=','):
    """
    Annotate each variant in the VCF file and save the annotated variants in an output CSV or TSV file.
    """
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        
        # Write header row
        writer.writerow(['Variant ID', 'Depth of Sequence Coverage', 'Supporting Reads', 'Percentage of Supporting Reads',
                          'Variant Type','Gene', 'Variant Effect', 'Minor Allele Frequency', 'Additional Annotations'])
        count=0
        for record in vcf_reader:
            #print(record)
            count=count+1
            variant_annotation = annotate_variant(record)
            writer.writerow(variant_annotation)
            print(count)
annotate_variants('test_vcf_data.txt', 'AnnotatedVariants.csv', delimiter=',')
