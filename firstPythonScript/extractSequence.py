from Bio import SeqIO

fasta_file = "postGubbins.filtered_polymorphic_sites.fasta" # Input fasta file
wanted_file = "wanted_list.list" # Input interesting sequence IDs, one per line
result_file = "postGubbins.filtered_polymorphic_sites_woRef.fasta" # Output fasta file

wanted = set()
with open(wanted_file) as f:
    for line in f:
        line = line.strip()
        #print(line) #headers
        if line != "":
            wanted.add(line[1:]) # This will add the IDs into the set() named wanted. To make sure, it does not contain duplicate
            #print(f'this is after removal of greater than > symbol: {line[1:]}') #headers

fasta_sequences = SeqIO.parse(open(fasta_file),'fasta') # open and load the fasta sequences
with open(result_file, "w") as f: # write into the output file
    for seq in fasta_sequences: #loop through fasta file
        #print (seq.id) 
        if seq.id in wanted: 
            SeqIO.write([seq], f, "fasta")