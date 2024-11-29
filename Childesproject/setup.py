import os
import pylangacq
from extract import extract_compounds
from classify import classify_head_position, analyze_head_position
from visualize import plot_head_position
from utils import get_cha_files, log_error

def process_cha_files(folder_path):
    cha_files = get_cha_files(folder_path)

    # Initialize lists to store data
    all_utterances = []

    for cha_file in cha_files:
        try:
            corpus = pylangacq.read_chat(cha_file)
            utterances = [str(utt) for utt in corpus.utterances()]  # Convert Utterance objects to strings
            all_utterances.extend(utterances)
        except Exception as e:
            log_error(cha_file, e)

    # Output sample utterances
    print(f"Sample utterances: {all_utterances[:5]}")

    # Extract compounds
    compounds = extract_compounds(all_utterances)
    print(f"Extracted {len(compounds)} compounds.")

    # Classify head positions
    classified_compounds = classify_head_position(compounds)
    print(f"Classified {len(classified_compounds)} compounds.")

    # Analyze and visualize results
    head_counts = analyze_head_position(classified_compounds)
    print(f"Head position counts: {head_counts}")

    # Visualize results if there are compounds
    if head_counts:
        plot_head_position(head_counts)
    else:
        print("No compounds found to visualize.")

if __name__ == "__main__":
    folder_path = r"C:/Users/miles/Desktop/Brown/Brown/Adam"
    process_cha_files(folder_path)
