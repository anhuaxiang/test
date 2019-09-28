import os
import pandas as pd
import cv2
from PIL import Image
import numpy as np
from imgaug import augmenters as iaa
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.layers import Dense, GlobalAveragePooling2D, GlobalMaxPooling2D
from keras.applications import resnet50, vgg16
from keras.models import Model
from keras.optimizers import SGD, Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.image import load_img, array_to_img, img_to_array
import cv2
import sys
import pickle

path = '/home/admin1/Desktop/R2/chest_photo/'
os.chdir(path)


data = pd.read_csv('path_data_label.csv')

le = LabelEncoder()
label_num = le.fit_transform(data['label'])
dic = dict(zip(data['label'], label_num))
dic_inv = dict(zip(dic.values(), dic.keys()))

ran = np.random.rand(len(data)) < 0.8
train = data[ran]
test = data[~ran]
assert (train.label.nunique() == test.label.nunique())
# image shape
img_shape = 224
sometimes = lambda x: iaa.Sometimes(0.5, x)
seq = iaa.Sequential([
    iaa.Crop(px=(0, img_shape * 0.05)),
    iaa.Fliplr(0.5), iaa.Flipud(0.5),
    sometimes(iaa.Affine(
        rotate=(-45, 45)
    ))
])


train_gen = ImageDataGenerator(preprocessing_function=seq.augment_image)

train_gen.std = 255
train_generator = train_gen.flow_from_dataframe(train, x_col='name', \
                                                y_col='label', target_size=(224, 224), \
                                                color_mode='rgb', shuffle=True, \
                                                batch_size=32, class_mode='categorical')

valid_gen = ImageDataGenerator()
valid_generator = valid_gen.flow_from_dataframe(test, x_col='name', \
                                                y_col='label', target_size=(224, 224), \
                                                color_mode='rgb', shuffle=False, \
                                                batch_size=32, class_mode='categorical')

pred_gen = ImageDataGenerator()
pred_generator = pred_gen.flow_from_dataframe(test, x_col='name', \
                                              y_col='label', target_size=(224, 224), \
                                              color_mode='rgb', shuffle=False, \
                                              batch_size=32, class_mode='categorical')


learning_rate = [0.01, 0.001, 0.0001, 0.1]
alg = ['resnet', 'vgg16']
space = {
    'algorithm': hp.choice('algorithm', alg),
    'lr': hp.choice('learning_rate', learning_rate)
}


def fnn(params):
    if params['algorithm'] == 'resnet':
        base_model = resnet50.ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3), pooling=None)
    if params['algorithm'] == 'vgg16':
        base_model = vgg16.VGG16(include_top=False, weights='imagenet',  input_shape=(224, 224, 3), pooling=None)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(train.label.nunique(), activation='softmax')(x)
    final_model = Model(input=base_model.input, output=predictions)

    for xx in final_model.layers[:-1]:
        xx.trainable = False
    es = EarlyStopping(monitor='loss', mode='min',
                       patience=30, verbose=1, )

    sgd = SGD(lr=params['lr'])
    final_model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['acc'])
    mc = ModelCheckpoint('/home/admin1/Desktop/R2/image_recognition/code/best_model.h5',
                         monitor='val_loss', mode='min',
                         save_best_only=True)
    final_model.fit_generator(
        train_generator,
        nb_epoch=5, steps_per_epoch=1000,
        validation_data=valid_generator,
        validation_steps=1 + len(valid_generator.classes) // 32,
        callbacks=[es, mc]
    )

    predict = final_model.predict_generator(pred_generator, \
                                            steps=1 + len(pred_generator.classes) // 32)
    y_pre = np.argmax(predict, axis=1)
    y_true = np.array(pred_generator.classes)
    acc = accuracy_score(y_true, y_pre)

    sys.stdout.flush()
    return {'loss': acc, 'status': STATUS_OK, 'pred_prob_y': predict, 'true_y': y_true, 'pred_y': y_pre,  'model': final_model}


trials = Trials()
best = fmin(fnn, space, algo=tpe.suggest, max_evals=3, trials=trials)


result = trials.results[np.argmin(trials.losses(), axis=0)]
print('Best Learning Rate:', learning_rate[best['learning_rate']])

'''############### predict/deploy '''
final_model = result['model']
#########################  predict/deploy single image
input_image = load_img('/home/admin1/Desktop/image.png')
input_image = img_to_array(input_image)
# resize to 224 x 224
input_image = cv2.resize(input_image, (224, 224))
# normalize
input_image *= 1. / 255
input_image = np.expand_dims(input_image, axis=0)
image_out = final_model.predict(input_image)
# print the top 3 classes in terms of probability for the image
image_out = image_out.reshape(image_out.shape[1])
rank = sorted([(x, pd.Series(i).map(dic_inv)[0]) for (i, x) in enumerate(image_out)], reverse=True)[:3]

######################## predict/deploy batch images
# sample image file
predict_image = pd.DataFrame(test['name'].sample(101)).reset_index(drop=True)
# ignore this label. Use it because generator cannot run w/o data label
predict_image['label'] = str(0)
predict_gen = ImageDataGenerator()
predict_gen.mean = np.array([123.68, 116.779, 103.939], \
                            dtype=np.float32).reshape((1, 1, 3))

predict_generator = predict_gen.flow_from_dataframe(dataframe=predict_image, \
                                                    x_col='name', \
                                                    y_col='label', target_size=(224, 224), \
                                                    color_mode='rgb', shuffle=False, \
                                                    batch_size=32, class_mode='categorical')

predict_result = final_model.predict_generator(predict_generator, \
                                               steps=1 + len(predict_generator.classes) // 32)
###### predict result
predict_result = np.argmax(predict_result, axis=1)

# save dictionary in pkl format file [need it for measurement metric]
e = open('/home/admin1/Desktop/R2/image_recognition/code/label_dict.pkl', 'wb')
pickle.dump(dic, e)
e.close()
f = open('/home/admin1/Desktop/R2/image_recognition/code/model_dict.pkl', 'wb')
pickle.dump(final_result, f)
f.close()
train = pd.DataFrame(train, columns=['name', 'label'])
test = pd.DataFrame(test, columns=['name', 'label'])
train.to_csv('/home/admin1/Desktop/R2/image_recognition/code/train.csv', index=False)
test.to_csv('/home/admin1/Desktop/R2/image_recognition/code/test.csv', index=False)
