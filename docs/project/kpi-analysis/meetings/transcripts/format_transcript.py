#!/usr/bin/env python3
import json
import sys
import traceback
from pathlib import Path

def process_transcript(input_file):
    """Process the raw transcript and format it as JSON"""
    print(f"Opening file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Successfully read {len(lines)} lines from file")
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        raise
    
    # Initialize the JSON structure
    formatted_data = {
        "date": Path(input_file).stem,
        "title": "KPI Analysis Project Discussion",
        "participants": set(),
        "transcript": []
    }
    
    current_speaker = None
    current_timestamp = None
    current_text = []
    
    i = 0
    try:
        while i < len(lines):
            line = lines[i].strip()
            print(f"Processing line {i}: {line[:50]}...")  # Print first 50 chars of line
            
            if not line:
                i += 1
                continue
                
            # Check if this is a timestamp
            if line.count(':') == 2 and all(part.isdigit() for part in line.split(':')):
                current_timestamp = line
                print(f"Found timestamp: {current_timestamp}")
                i += 1
                continue
                
            # Check if this is a speaker name (appears twice in succession)
            if i + 1 < len(lines) and line == lines[i + 1].strip():
                if current_speaker and current_timestamp and current_text:
                    # Save the previous entry
                    entry = {
                        "speaker": current_speaker,
                        "timestamp": current_timestamp,
                        "text": " ".join(current_text)
                    }
                    print(f"Adding entry for {current_speaker} at {current_timestamp}")
                    formatted_data["transcript"].append(entry)
                    current_text = []
                
                current_speaker = line
                formatted_data["participants"].add(line)
                print(f"Found speaker: {current_speaker}")
                i += 2  # Skip the duplicate name
                continue
            
            # Must be text content
            if line:
                current_text.append(line)
                print(f"Added text line: {line[:50]}...")
            i += 1
        
        # Don't forget to add the last entry
        if current_speaker and current_timestamp and current_text:
            entry = {
                "speaker": current_speaker,
                "timestamp": current_timestamp,
                "text": " ".join(current_text)
            }
            print(f"Adding final entry for {current_speaker} at {current_timestamp}")
            formatted_data["transcript"].append(entry)
        
        # Convert participants set to sorted list
        formatted_data["participants"] = sorted(list(formatted_data["participants"]))
        print(f"Found {len(formatted_data['participants'])} participants")
        print(f"Processed {len(formatted_data['transcript'])} transcript entries")
    except Exception as e:
        print(f"Error processing transcript at line {i}: {str(e)}")
        print(f"Current state: speaker={current_speaker}, timestamp={current_timestamp}")
        print(f"Current text buffer: {current_text}")
        traceback.print_exc()
        raise
    return formatted_data

def main():
    if len(sys.argv) != 2:
        print("Usage: format_transcript.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file
    
    try:
        print(f"Starting to process file: {input_file}")
        formatted_data = process_transcript(input_file)
        
        # Create a backup of the original file
        backup_file = input_file + '.bak'
        print(f"Creating backup at: {backup_file}")
        Path(input_file).rename(backup_file)
        
        # Write the formatted JSON
        print(f"Writing formatted JSON to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully formatted transcript: {output_file}")
        print(f"Original file backed up as: {backup_file}")
        
    except Exception as e:
        print(f"Error processing transcript: {str(e)}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 