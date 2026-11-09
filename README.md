# GPR Data Quality – Independent Learning Exercise

An independent learning exercise prepared in November 2026 to develop a practical understanding of Ground Penetrating Radar (GPR) data processing and metadata documentation, in preparation for an EngD application focused on utility mapping.

## What I did

- Processed a real GSSI example profile using Python and GPRPy.
- Applied dewow, background removal and time-power gain.
- Converted travel time to estimated depth using an assumed wave velocity of 0.1 m/ns.
- Created a simplified illustrative simulation comparing two buried pipes in different assumed soil conditions.
- Developed a 17-field metadata checklist for documenting GPR surveys, with the source and status of each field.

![Simulated pipes in dry sand and wet clay](fig4_simulated_pipes.png)

## Files

- **GPR Learning Note:** One-page summary of the exercise, observations and limitations.
- **Python scripts:** Data processing, illustrative simulation and header inspection.
- **Figures:** Raw, processed, depth-converted and simulated radargrams.
- **Metadata checklist (`GPR_metadata_form.xlsx`):** 17 proposed fields for survey documentation, filled in for the example file. 10 of 17 fields are missing, including all four ground-condition fields.

## Limitations

This is an educational exercise, not a validated GPR detection or electromagnetic modelling study. The simulated soil conditions use assumed parameters, and the depth conversion has not been field-calibrated.

## Tools

Python, NumPy, Matplotlib and GPRPy.

## Data source

GSSI example dataset distributed with the open-source GPRPy software.

## Acknowledgements

The example dataset and processing functions come from GPRPy (MIT License):
Plattner, A. M. (2020). GPRPy: Open-source ground-penetrating radar processing and visualization software. *The Leading Edge*, 39(5), 332–337. https://doi.org/10.1190/tle39050332.1

The Python scripts were prepared with the help of an AI assistant. I ran, modified and documented them, built the metadata checklist and wrote the learning note.

## Author

Shiva Hassanpour  
MSc Urban Planning and Policy Design, Politecnico di Milano
