import pandas
import pathlib

matrix = input('\nInput original matrix file: ')
cell = input('\nInput cell file: ')
gene = input('\nInput gene file: ')
outputDir = input('\nEnter output directory name: ') + '/'

cellCount = sum(1 for line in open(cell))
geneCount = sum(1 for line in open(gene))

df = pandas.read_csv(matrix, sep='\t', header=None)
nonZero = df[df > 0].count()[2]

pathlib.Path(outputDir).mkdir(parents=True, exist_ok=True)

with open(matrix, 'r') as fin:
    with open(outputDir + 'matrix.mtx', 'w') as fout:
        fout.write('%%MatrixMarket matrix coordinate real general')
        fout.write('\n%')
        fout.write('\n' + str(geneCount) + ' ' + str(cellCount) + ' ' + str(nonZero) + '\n')
        for line in fin:
            fout.write(line.replace('\t', ' ').replace('_', '-'))

print('\nFinished writing matrix.mtx')

with open(cell, 'r') as fin:
    with open(outputDir + 'barcodes.tsv', 'w') as fout:
        for line in fin:
            fout.write(line.replace('_', '-'))

print('\nFinished writing barcodes.tsv')

with open(gene, 'r') as fin:
    with open(outputDir + 'genes.tsv', 'w') as fout:
        for line in fin:
            fout.write(line.replace('	', '\t').replace('_', '-'))

print('\nFinished writing genes.tsv')
