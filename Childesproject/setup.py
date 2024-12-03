# setup.py
import os
import pylangacq
from extract import extract_compounds
from classify import classify_head_position, analyze_head_position
from visualize import plot_head_position
from utils import get_cha_files, log_error

def process_cha_files(folder_path):
    cha_files = get_cha_files(folder_path)

    # Initialize lists to store data
    utterances_by_speaker = {'CHI': [], 'ADU': []}

    for cha_file in cha_files:
        try:
            corpus = pylangacq.read_chat(cha_file)

            # Extract utterances
            for utterance in corpus.utterances():
                participant = utterance.participant
                # Collect child utterances
                if participant == 'CHI':
                    utterances_by_speaker['CHI'].append(str(utterance))
                # Collect adult utterances
                elif participant in {'MOT', 'FAT', 'MAD', 'GRA', 'URS'}:
                    utterances_by_speaker['ADU'].append(str(utterance))
        except Exception as e:
            log_error(cha_file, e)

    # Output sample utterances
    print(f"Sample child utterances: {utterances_by_speaker['CHI'][:5]}")
    print(f"Sample adult utterances: {utterances_by_speaker['ADU'][:5]}")

    # Extract compounds for both child and adult utterances
    compounds_child = extract_compounds(utterances_by_speaker['CHI'])
    compounds_adult = extract_compounds(utterances_by_speaker['ADU'])

    print(f"Extracted {len(compounds_child)} compounds from child utterances.")
    print(f"Extracted {len(compounds_adult)} compounds from adult utterances.")

    # Classify head positions
    classified_compounds_child = classify_head_position(compounds_child)
    classified_compounds_adult = classify_head_position(compounds_adult)

    print(f"Classified {len(classified_compounds_child)} child compounds.")
    print(f"Classified {len(classified_compounds_adult)} adult compounds.")

    # Analyze and visualize results
    head_counts_child = analyze_head_position(classified_compounds_child)
    head_counts_adult = analyze_head_position(classified_compounds_adult)

    print(f"Child head position counts: {head_counts_child}")
    print(f"Adult head position counts: {head_counts_adult}")

    # Visualize results if there are compounds
    if head_counts_child and head_counts_adult:
        plot_head_position(head_counts_child, head_counts_adult)
    else:
        print("No compounds found to visualize.")

if __name__ == "__main__":
    folder_path = r"C:/Users/miles/Desktop/Brown/Brown/Adam"
    process_cha_files(folder_path)
