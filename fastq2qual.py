#!/usr/bin/env python
import sys
import os
from Bio import SeqIO

def fastq2qual(infastq,fastq_format):
    seqs = []
    outqual = os.path.splitext(infastq)[0] + ".qual"
    outfasta = os.path.splitext(infastq)[0] + ".fasta"

    inhandle = open(infastq,"rU")
    outhandle_qual = open(outqual,"w")
    outhandle_fasta = open(outfasta,"w")

    for rec in SeqIO.parse(inhandle,fastq_format):
        seqs.append(rec)
    count = SeqIO.write(seqs,outhandle_qual,"qual")
    count = SeqIO.write(seqs,outhandle_fasta,"fasta")
    inhandle.close()
    outhandle_fasta.close()
    outhandle_qual.close()

#    SeqIO.convert(infastq,"fastq",outqual,"qual")

if __name__ == '__main__':
    fastq_format = "fastq-solexa"
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "Usage: fastq2qual fastq_file [fastq-format]"
        sys.exit(1)
    infastq = sys.argv[1]
    if len(sys.argv)>2:
        fastq_format = sys.argv[2]
    fastq2qual(infastq,fastq_format)

