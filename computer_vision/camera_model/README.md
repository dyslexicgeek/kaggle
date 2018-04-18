Use a resnet34 CNN model
This ends up being a multi class classification technique.

But instead of picking the crisply identified test images,
we instead pick the ones which similar probability for multiple
classes. Simply put, subtract the images from the test set,
which have a clear classification.
