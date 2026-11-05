# GPR Data Quality – Independent Learning Exercise

An independent learning exercise prepared in November 2026 to develop a practical understanding of Ground Penetrating Radar (GPR) data processing and metadata documentation, in preparation for an EngD application focused on utility mapping.

## What I did

- Processed a real GSSI example profile using Python and GPRPy.
- Applied dewow, background removal and time-power gain.
- Converted travel time to estimated depth using an assumed wave velocity of 0.1 m/ns.
- Created a simplified illustrative simulation comparing two buried pipes in different assumed soil conditions.
- Developed a 17-field metadata checklist for documenting GPR surveys.

## Files

- **GPR Learning Note:** One-page summary of the exercise, observations and limitations.
- **Python scripts:** Data processing, illustrative simulation and header inspection.
- **Figures:** Raw, processed, depth-converted and simulated radargrams.
- **Metadata checklist:** Proposed fields for improving survey documentation, when available.

## Limitations

This is an educational exercise, not a validated GPR detection or electromagnetic modelling study. The simulated soil conditions use assumed parameters, and the depth conversion has not been field-calibrated.

## Tools

Python, NumPy, Matplotlib and GPRPy.

## Data source

GSSI example dataset distributed with the open-source GPRPy software.

## Author

Shiva Hassanpour  
MSc Urban Planning and Policy Design, Politecnico di Milano
