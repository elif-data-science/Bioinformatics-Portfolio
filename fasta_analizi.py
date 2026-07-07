def calculate_gc_content(sequence):
    """Bir nükleotit dizisindeki GC oranını hesaplar."""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_count = len(sequence)
    
    if total_count == 0:
        return 0
    
    return (g_count + c_count) / total_count * 100

def parse_fasta(file_path):
    """FASTA formatındaki dosyayı okur ve analiz eder."""
    sequences = {}
    current_id = None
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                if current_id:
                    sequences[current_id] += line
    
    return sequences


if __name__ == "__main__":
    # Örnek bir FASTA verisi simüle edelim
    sample_data = {
        "Seq1_TargetGene": "ATGCGATCGATCGATCGATCGATCGATC",
        "Seq2_MutatedGene": "ATGCGATCGATCGATCGACTCGACTCGC"
    }
    
    print("--- Bioinformatik Dizi Analiz Raporu ---")
    for seq_id, seq in sample_data.items():
        gc_perc = calculate_gc_content(seq)
        print(f"ID: {seq_id}")
        print(f"Uzunluk: {len(seq)} bp")
        print(f"GC İçeriği: %{gc_perc:.2f}\n")
