from muse_an_lib import Validate
from muse_an_lib import RandomData
from muse_an_lib import Visualize
dataset = [[1654046931.830125,[18.5546875, 27.34375, 121.09375, 37.59765625, -43.45703125]],
    [1654046931.8340313,[36.62109375, 30.2734375, 146.97265625, 41.015625, -41.9921875]],
    [1654046931.8379376,[33.203125, 29.78515625, 21.97265625, 30.2734375, 33.203125]],
    [1654046931.8418438,[25.390625, 27.83203125, -76.66015625, 31.25, 56.640625]],
    [1654046931.84575,[26.85546875, 26.85546875, 89.35546875, 24.90234375, 33.203125]]]


print(Validate.Valid(dataset))
print(Validate.TimeStamp(dataset))
print(Validate.Values(dataset))
print(Validate.ValuesSpecific(dataset, [0, 4]))

print(RandomData.sig_gen(3, 2, 80, 50, 3))

import matplotlib.pyplot as plt
plt.plot(dataset[0][1])
plt.show()