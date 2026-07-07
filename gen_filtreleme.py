import pandas as pd

def filter_significant_genes(data_frame, log2fc_threshold=2.0, p_threshold=0.05):
    """
    Anlamlı şekilde regüle olmuş genleri filtreler.
    (Up-regulated ve Down-regulated)
    """
    # İstatistiksel olarak anlamlı olanlar (p-value < 0.05)
    significant = data_frame[data_frame['p_value'] < p_threshold]
    
    # Up-regulated (İfadesi artanlar)
    up_regulated = significant[significant['log2FoldChange'] >= log2fc_threshold]
    
    # Down-regulated (İfadesi azalanlar)
    down_regulated = significant[significant['log2FoldChange'] <= -log2fc_threshold]
    
    return up_regulated, down_regulated


if __name__ == "__main__":
    raw_data = {
        'gene_id': ['BRCA1', 'TP53', 'EGFR', 'MYC', 'IL6', 'VEGFA'],
        'log2FoldChange': [2.5, -0.4, 3.1, -2.2, 0.1, 1.8],
        'p_value': [0.001, 0.450, 0.0002, 0.015, 0.890, 0.03]
    }
    
    df = pd.DataFrame(raw_data)
    up, down = filter_significant_genes(df)
    
    print("=== Filtrelenmiş Gen Analiz Sonuçları ===")
    print(f"\n[+] Anlamlı Şekilde Artan Genler (Up-regulated):\n{up[['gene_id', 'log2FoldChange']]}")
    print(f"\n[-] Anlamlı Şekilde Azalan Genler (Down-regulated):\n{down[['gene_id', 'log2FoldChange']]}")
