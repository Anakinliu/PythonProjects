from CycleGAN.datasets import ImageDataset

d = ImageDataset("dataset")
print(d.files_A)
print(d.files_B)
print(len(d.files_B))
print(len(d.files_A))