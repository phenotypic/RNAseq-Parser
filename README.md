# RNAseq-Parser

The scripts in this repository are used to prepare RNA-seq data for bioinformatics analysis using [Seurat](https://github.com/satijalab/seurat). To analyse data, Seurat expects three properly formatted input files: `barcodes.tsv`, `genes.tsv`, and `matrix.mtx`.

Use `parser.py` to reformat three improperly formatted input files (e.g. [this data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192498)).

Use `csv2mex.R` to separate a `.csv` file into three properly formatted files (e.g. [this data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137971)).

## Prerequisites

To run `parser.py` you must have `python3` installed.

To run `csv2mex.R` you must have [RStudio](https://www.rstudio.com) installed. Download through [`brew`](https://brew.sh) by running: `brew install --cask rstudio`

You will need to install any other outstanding requirements:

| Command | Installation |
| --- | --- |
| `pandas` | Install via `pip3` by running `pip3 install pandas` |
| `Matrix`, `Seurat` | From the command line, run `R` then run `install.packages("package_name")`, replacing `package_name` as necessary |

## Usage

Download with:
```
git clone https://github.com/phenotypic/RNAseq-Parser.git
pip3 install -r requirements.txt
```

Run `parser.py` from the same directory with:
```
python3 parser.py
```

Open `csv2mex.R` in RStudio to run the script. Remember to change the project path and input `.csv` file in the script before running.

## Notes

- `csv2mex.R` was originally obtained from [this gist](https://gist.github.com/xie186/332eff13dcac50f101f91494402b4bd1)
