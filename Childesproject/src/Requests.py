# Step 1: Import the tbdb module
import tbdb

# Step 2: Fetch Transcripts from the CHILDES MacWhinney corpus
transcripts = tbdb.getTranscripts({
    "corpusName": "childes", 
    "corpora": [['childes', 'Eng-NA', 'MacWhinney', '010411a']]
})

# Step 3: Print the transcript data
print("Transcripts Data:")
print(transcripts)

# Step 4: Fetch Participants in the same transcript
participants = tbdb.getParticipants({
    "corpusName": "childes",
    "corpora": [['childes', 'Eng-NA', 'MacWhinney', '010411a']]
})

# Step 5: Print the participants data
print("\nParticipants Data:")
print(participants)

# Step 6: Fetch utterances from the same transcript
utterances = tbdb.getUtterances({
    "corpusName": "childes",
    "corpora": [['childes', 'Eng-NA', 'MacWhinney', '010411a']]
})

# Step 7: Print the utterances data
print("\nUtterances Data:")
print(utterances)

# Step 8: Fetch tokens (individual words) from the same transcript
tokens = tbdb.getTokens({
    "corpusName": "childes",
    "corpora": [['childes', 'Eng-NA', 'MacWhinney', '010411a']]
})

# Step 9: Print the tokens data
print("\nTokens Data:")
print(tokens)
