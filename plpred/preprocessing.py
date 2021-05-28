from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd

def compute_aa_composition(protein_sequence:str) -> dict:
    """
    Computes the aminoacid composition of a given protein sequence.
    
    Parameters
    -----------
    protein_sequence: str
        sequence of the protein to be processed
    
    Returns
    -------
    aa_composition: dict
        dictionary containins the relative abundance of each aminoacid
    """
    
    analyzer = ProtParam.ProteinAnalysis(str(protein_sequence))
    aa_composition = analyzer.get_amino_acids_percent()
    return aa_composition

def generate_aa_composition_df(file_path:str, membrane_label:int) -> pd.DataFrame:
    """
    Generate the aminoacid composition Pandas dataframe 
    
    Parameters
    -----------
    file_path: str
        FASTA file path with the aminoacid sequences to be processed

    membrane_label: int
        label indicating the protein subcellular location, 0 if not a membrane protein and 1 if is a membrane protein

    Returns
    -------
    df: csv
        csv file that contains the preprocess data
    """

    df = pd.DataFrame()
    handle = open(file_path)
    parser = SeqIO.parse(handle, 'fasta')

    for protein in parser:
        protein_data = compute_aa_composition(protein.seq)
        protein_data['membrane'] = membrane_label
        df = df.append([protein_data], ignore_index=True)
    return df


df_membrane = generate_aa_composition_df(file_path='../data/raw/membrane.fasta', membrane_label=1)
df_cytoplasm = generate_aa_composition_df(file_path='../data/raw/cytoplasm.fasta', membrane_label=0)

df_processed = pd.concat([df_membrane, df_cytoplasm])
df_processed.to_csv('../data/processed/processed.csv', index=False)

if __name__ == "__main__":

    print('Processing FASTA file:membrane proteins')
    df_membrane = generate_aa_composition_df(file_path='../data/raw/membrane.fasta', membrane_label=1)

    print('Processing FASTA file:cytoplasm proteins')
    df_cytoplasm = generate_aa_composition_df(file_path='../data/raw/cytoplasm.fasta', membrane_label=0)

    df_processed = pd.concat([df_membrane, df_cytoplasm])

    print('Saving data frame file')
    df_processed.to_csv('../data/processed/processed.csv', index=False)

