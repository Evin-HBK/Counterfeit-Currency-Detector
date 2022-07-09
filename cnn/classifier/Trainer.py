import os
import matplotlib.image as mpimg
from keras_applications.inception_v3 import layers
from keras_preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf
from keras.layers import Activation, Dense, Flatten , Dropout
import pickle
base_dir = os.getcwd()+'/dataset'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training 500 pictures
train_500_dir = os.path.join(train_dir, '500')

# Directory with our training 2000 pictures
train_2000_dir = os.path.join(train_dir, '2000')

# Directory with our validation 500 pictures
validation_500_dir = os.path.join(validation_dir, '500')

# Directory with our validation 2000 pictures
validation_2000_dir = os.path.join(validation_dir, '2000')
nrows = 4
ncols = 4

fig = plt.gcf()
fig.set_size_inches(ncols * 4, nrows * 4)
pic_index = 100
train_500_fnames = os.listdir(train_500_dir)
train_2000_fnames = os.listdir(train_2000_dir)

next_500_pix = [os.path.join(train_500_dir, fname)
                for fname in train_500_fnames[pic_index - 8:pic_index]
                ]

next_2000_pix = [os.path.join(train_2000_dir, fname)
                for fname in train_2000_fnames[pic_index - 8:pic_index]
                ]

for i, img_path in enumerate(next_500_pix + next_2000_pix):
    # Set up subplot; subplot indices start at 1
    sp = plt.subplot(nrows, ncols, i + 1)
    sp.axis('Off')  # Don't show axes (or gridlines)

    img = mpimg.imread(img_path)
    plt.imshow(img)

plt.show()
# Add our data-augmentation parameters to ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255., rotation_range = 40, width_shift_range = 0.2, height_shift_range = 0.2,shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

test_datagen = ImageDataGenerator( rescale = 1.0/255. )
train_generator = train_datagen.flow_from_directory(train_dir, batch_size = 20, class_mode = 'binary', target_size = (150, 150))
validation_generator = test_datagen.flow_from_directory(validation_dir, batch_size = 20, class_mode = 'binary', target_size = (150, 150))
base_model = InceptionV3(input_shape = (150, 150, 3), include_top = False, weights = 'imagenet')
for layer in base_model.layers:
    layer.trainable = False
x = Flatten()(base_model.output)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.2)(x)

# Add a final sigmoid layer with 1 node for classification output
x = Dense(1, activation='sigmoid')(x)

model = tf.keras.models.Model(base_model.input, x)

model.compile(optimizer = RMSprop(lr=0.0001), loss = 'binary_crossentropy', metrics = ['acc'])
inc_history = model.fit_generator(train_generator, validation_data = validation_generator, steps_per_epoch = 10, epochs = 10)
model.save('classifier.model')