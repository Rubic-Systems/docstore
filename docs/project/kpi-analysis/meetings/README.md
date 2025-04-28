# Meetings Documentation

## Overview
This directory contains meeting transcripts, summaries, and related documentation.

## Directory Structure
- `transcripts/` - Raw meeting transcripts
- `summaries/` - Meeting summaries and action items

## New Meeting Workflow
Follow these steps when processing a new meeting:

1. **Process Transcript**
   - Save raw transcript in `transcripts/YYYY-MM-DD.json`
   - Run formatting script:
     ```bash
     cd transcripts
     python3 format_transcript.py YYYY-MM-DD.json
     ```
   - Verify the JSON structure is correct

2. **Create Meeting Summary**
   - Create new file: `summaries/YYYY-MM-DD-topic.md`
   - Use [Meeting Summary Template](../../../templates/meetings/meeting-summary.md)
   - Include:
     - Date and participants
     - Key topics discussed
     - Action items assigned
     - Decisions made
     - Next steps

3. **Record Decisions**
   - For each significant decision:
     - Add entry to `../../../company/operations/decisions/YYYY-MM.md`
     - Use [Decision Log Template](../../../templates/meetings/decision-log.md)
     - Include context, alternatives considered, and rationale
     - Link to relevant meeting summary
     - Update decision log index if needed

4. **Create/Update Progress Report**
   - If meeting included progress updates:
     - Create/update `../../../company/operations/progress/YYYY-MM.md`
     - Document achievements, challenges, and next steps
     - Link to relevant meeting summaries and decisions

## Guidelines
1. Store raw transcripts in JSON format
2. Include metadata (date, participants, topics)
3. Create summaries for important meetings
4. Link related documents and decisions

## Maintenance
- Archive old transcripts quarterly
- Update summaries as needed
- Review and clean up regularly

## Related Documentation
- [Technical Architecture](../../../project/kpi-analysis/technical/architecture/README.md)
- [Project Planning](../../../project/kpi-analysis/planning/README.md)
- [Decision Logs](../../../company/operations/decisions/README.md)

## Templates
Use the following templates from the [Templates](../../../templates/meetings/) directory:
- [Meeting Agenda](../../../templates/meetings/meeting-agenda.md)
- [Meeting Summary](../../../templates/meetings/meeting-summary.md)
- [Decision Log](../../../templates/meetings/decision-log.md) 