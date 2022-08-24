start = 0.0001
min = 0.00001
max = 0.001
rampup_epochs = 10
sustain_epochs = 10
decay = .8

def lrfn(epoch):
  if epoch < rampup_epochs:
    return (max - start)/rampup_epochs * epoch + start
  elif epoch < rampup_epochs + sustain_epochs:
    return max
  else:
    return min
    
lr = keras.callbacks.LearningRateScheduler(lambda epoch: lrfn(epoch), verbose=True)


def plot_loss(history):
    minimum = pd.Series(history.history['val_loss']).min()-100 
    maximum = pd.Series(history.history['loss']).max()+100
    
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([minimum, maximum])
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)

  
def ratio_loss(y_true, y_pred):
    return abs(1 - (y_pred / y_true))
  
def root_mean_squared_error(y_true, y_pred):
    from keras import backend as K
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))
