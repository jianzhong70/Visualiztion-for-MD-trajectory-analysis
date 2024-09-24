library(bio3d)
library(igraph)
pdb <- read.pdb("7jvz.pdb")
modes <- nma(pdb)
cij <- dccm(modes)
net <- cna(cij, cut.off=0.4)
plot(net, pdb, full = TRUE, vertex.label.cex=0.7)
plot(net, pdb)
vmd.cna(net, pdb, launch = TRUE)


