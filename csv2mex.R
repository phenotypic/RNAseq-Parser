library(Matrix)
library(Seurat)

# set project path
path = "~/Downloads/GSE137971_RAW"
setwd(path)

# generate single-cell RNA seq data
count <- read.csv("GSM4095395_1dpa1_DGEmatrix.csv", header=T,row.names = 1)
gbm <- t(count)

# save sparse matrix
sparse.gbm <- Matrix(gbm , sparse = T )
head(sparse.gbm)
## Market Exchange Format (MEX) format
writeMM(obj = sparse.gbm, file="matrix.mtx")

# save genes and cells names
write(x = rownames(gbm), file = "genes.tsv")
write(x = colnames(gbm), file = "barcodes.tsv")

test <- Read10X(data.dir = path, gene.column = 1, unique.features = TRUE)

# Initialize the Seurat object with the raw (non-normalized data).
test_seurat <- CreateSeuratObject(counts = test, project = "test", min.cells = 0, min.features = 0)
