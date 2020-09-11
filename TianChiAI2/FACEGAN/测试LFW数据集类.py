from FACEGAN.LFW数据集 import LFW
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
img_size = 112

transform = transforms.Compose([
    transforms.CenterCrop(img_size),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])


dataset = LFW(load=True, transform=transform)
loader = DataLoader(dataset, batch_size=8, shuffle=True)

print(len(dataset.real_labels))
print(len(set(dataset.real_labels)))
print(dataset.real_labels)
# for i in range(10):
#
for idx, (img, label) in enumerate(loader):
    # wa = Image.fromarray(img[0].numpy(), "RGB")
    # wa.show()
    print(img[0].shape)
    # print(img, label)
    # break

print(len(dataset))