##produce fake calcium imaging data

from showit import image
import matplotlib.pyplot as plot
from regional import many

from fakearray import calcium_data

data, series, truth = calcium_data(shape=(100,300), n=5, t=50, seed=42, noise=0.5, withparams=True)
base = data.mean().toarray()
image(base);
plot.show()
image(many(truth).mask(dims=data.shape[1:], cmap='rainbow', stroke='black', base=base));
plot.show()
print data
print series
print truth