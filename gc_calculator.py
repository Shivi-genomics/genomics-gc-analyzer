import matplotlib.pyplot as plt

file_name = "sample_fasta"

with open(file_name, "r") as file:
    lines = file.readlines()

dna_sequence = ""
for line in lines:
    line = line.strip()
    if not line.startswith(">"):
        dna_sequence += line

# Sabhi bases ki counting
a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")
total_length = len(dna_sequence)

if total_length > 0:
    gc_content = ((g_count + c_count) / total_length) * 100
    print("--- Genomic GC Content Analysis ---")
    print(f"Total Sequence Length : {total_length} bp")
    print(f"GC Content            : {gc_content:.2f}%\n")

    # Matplotlib Bar Chart Setup
    bases = ['A', 'T', 'G', 'C']
    counts = [a_count, t_count, g_count, c_count]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    plt.figure(figsize=(6, 4))
    plt.bar(bases, counts, color=colors, edgecolor='black')
    
    plt.xlabel("DNA Bases", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.title("DNA Base Composition Analysis", fontsize=14, fontweight='bold')
    
    # Graph ko portfolio/GitHub ke liye image ke roop mein save karna
    plt.savefig("dna_composition_plot.png")
    print("Graph successfully saved as 'dna_composition_plot.png'!")

    # Screen par graph show karna
    plt.show()